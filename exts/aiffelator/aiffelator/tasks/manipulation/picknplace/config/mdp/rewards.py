# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import torch
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.sensors import FrameTransformer
from omni.isaac.lab.utils.math import combine_frame_transforms

if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv

from .scenes import AiffelatorScenes
from .terminations import multi_object_reached_goal_place


def object_is_lifted(
    env: ManagerBasedRLEnv, minimal_height: float, object_cfg: SceneEntityCfg = SceneEntityCfg("object")
) -> torch.Tensor:
    """Reward the agent for lifting the object above the minimal height."""
    object: RigidObject = env.scene[object_cfg.name]
    return torch.where(object.data.root_pos_w[:, 2] > minimal_height, 1.0, 0.0)

def object_is_lifted_2(
    env: ManagerBasedRLEnv, minimal_height: float, maximum_height: float, object_cfg: SceneEntityCfg = SceneEntityCfg("object")
) -> torch.Tensor:
    """Reward the agent for lifting the object above the minimal height."""
    object: RigidObject = env.scene[object_cfg.name]
    rewards = torch.where(object.data.root_pos_w[:, 2] > minimal_height, 1.0, 0.0)
    rewards += rewards * (object.data.root_pos_w[:, 2] * 10)
    return torch.clip(rewards, min=0.0, max=1.0+(maximum_height * 10))

def object_ee_distance(
    env: ManagerBasedRLEnv,
    std: float,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame")
) -> torch.Tensor:
    """Reward the agent for reaching the object using tanh-kernel."""
    # extract the used quantities (to enable type-hinting)
    object: RigidObject = env.scene[object_cfg.name]
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # Target object position: (num_envs, 3)
    object_pos_w = object.data.root_pos_w
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    # Distance of the end-effector to the object: (num_envs,)
    object_ee_distance = torch.norm(object_pos_w - ee_w, dim=1)
    return 1 - torch.tanh(object_ee_distance / std)

def object_goal_distance(
    env: ManagerBasedRLEnv,
    std: float,
    minimal_height: float,
    command_name: str,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    object_cfg: SceneEntityCfg = SceneEntityCfg("object")
) -> torch.Tensor:
    """Reward the agent for tracking the goal pose using tanh-kernel."""
    # extract the used quantities (to enable type-hinting)
    robot: RigidObject = env.scene[robot_cfg.name]
    object: RigidObject = env.scene[object_cfg.name]
    command = env.command_manager.get_command(command_name)
    # compute the desired position in the world frame
    des_pos_b = command[:, :3]
    des_pos_w, _ = combine_frame_transforms(robot.data.root_state_w[:, :3], robot.data.root_state_w[:, 3:7], des_pos_b)
    # distance of the end-effector to the object: (num_envs,)
    distance = torch.norm(des_pos_w - object.data.root_pos_w[:, :3], dim=1)
    # rewarded if the object is lifted above the threshold
    return (object.data.root_pos_w[:, 2] > minimal_height) * (1 - torch.tanh(distance / std))

def object_goal_place_distance(
    env: ManagerBasedRLEnv,
    std: float,
    minimal_height: float,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    place_cfg: SceneEntityCfg = SceneEntityCfg("place")
) -> torch.Tensor:

    # extract the used quantities (to enable type-hinting)
    robot: RigidObject = env.scene[robot_cfg.name]
    object: RigidObject = env.scene[object_cfg.name]
    # compute the desired position in the world frame
    des_pos_b = AiffelatorScenes.place_position(name=place_cfg.name, num_envs=env.num_envs, device=env.device)
    des_pos_w, _ = combine_frame_transforms(robot.data.root_state_w[:, :3], robot.data.root_state_w[:, 3:7], des_pos_b)
    # distance of the end-effector to the object: (num_envs,)
    distance = torch.norm(des_pos_w - object.data.root_pos_w[:, :3], dim=1)
    # rewarded if the object is lifted above the threshold
    return (object.data.root_pos_w[:, 2] > minimal_height) * (1 - torch.tanh(distance / std))

def drop_objects(env: ManagerBasedRLEnv, object_cfgs: list[SceneEntityCfg]) -> torch.Tensor:
    result = torch.tensor(0.0, device=env.device)
    rate = 1/len(object_cfgs)
    for object_cfg in object_cfgs:
        object: RigidObject = env.scene[object_cfg.name]
        is_dropped = object.data.root_pos_w[:, 2] < -0.05
        result = result + (is_dropped * rate)
    return result

def get_distance(env, robot_cfg, object_cfg, place_cfg):
    robot: RigidObject = env.scene[robot_cfg.name]
    object: RigidObject = env.scene[object_cfg.name]
    # compute the desired position in the world frame
    des_pos_b = AiffelatorScenes.place_position(name=place_cfg.name, num_envs=env.num_envs, device=object.device)
    des_pos_w, _ = combine_frame_transforms(robot.data.root_state_w[:, :3], robot.data.root_state_w[:, 3:7], des_pos_b)
    # distance of the end-effector to the object: (num_envs,)
    return torch.norm(des_pos_w - object.data.root_pos_w[:, :3], dim=1)

def complete_task(
    env: ManagerBasedRLEnv,
    threshold: float,
    robot_cfg: SceneEntityCfg,
    object_cfgs: list[SceneEntityCfg],
    place_cfgs: list[SceneEntityCfg]
) -> torch.Tensor:
    
    result = torch.full((env.num_envs,), 0.0, device=env.device)
    goal_in = torch.full((env.num_envs,), True, device=env.device)
    for object, place in zip(object_cfgs, place_cfgs):
        distance = get_distance(
            env=env,
            robot_cfg=robot_cfg,
            object_cfg=object,
            place_cfg=place
        )
        diff = threshold - distance
        goal_in &= diff > 0
        result += torch.where(diff > 0, diff, 0.0)
    each_reward = result / (threshold * len(object_cfgs))
    all_goal_in_reward = goal_in * 2
    return each_reward + all_goal_in_reward

def collision_place_cube(env: ManagerBasedRLEnv) -> torch.Tensor:
    place_cube_pencil_case_cfg = AiffelatorScenes.Place.Cube.get("pencil_case")
    place_cube_pencil_case: RigidObject = env.scene[place_cube_pencil_case_cfg.name]
    pencil_case_cube_distance = torch.norm(torch.tensor(AiffelatorScenes.Place.Cube.pos[1], device=env.device) - place_cube_pencil_case.data.root_pos_w[:, :3], dim=1)
    
    place_cube_pen_cfg = AiffelatorScenes.Place.Cube.get("pen")
    place_cube_pen: RigidObject = env.scene[place_cube_pen_cfg.name]
    pen_cube_distance = torch.norm(torch.tensor(AiffelatorScenes.Place.Cube.pos[0], device=env.device) - place_cube_pen.data.root_pos_w[:, :3], dim=1)

    return torch.abs(torch.tanh(pencil_case_cube_distance)) + torch.abs(torch.tanh(pen_cube_distance))

def stagnation_penalty(
    env: ManagerBasedRLEnv,
    history_size: int,
    penalty: float,
    position_threshold: float,
    goal_threshold: float,
    robot_cfg: SceneEntityCfg,
    ee_frame_cfg: SceneEntityCfg,
    object_cfgs: list[SceneEntityCfg],
    place_cfgs: list[SceneEntityCfg]
) -> torch.Tensor:
    """
    엔드이펙터가 특정 위치에서 오래 머무를 때 페널티를 부여하는 함수
    
    Args:
        env: 환경 인스턴스
        history_size: 저장할 이전 위치의 개수
        penalty: 페널티 크기
        position_threshold: 위치 변화를 감지할 임계값
        ee_frame_cfg: 엔드이펙터 프레임 설정
    
    Returns:
        torch.Tensor: 각 환경에 대한 페널티 값
    """
    
    if not hasattr(env, 'ee_position_history'):
        env.ee_position_history = torch.zeros((history_size, env.num_envs, 3), device=env.device)
    
    
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # End-effector position: (num_envs, 3)
    ee_pos = ee_frame.data.target_pos_w[..., 0, :]
    #ee_pos = env.scene.get_link_state(ee_frame_cfg.name)[0]
    
    
    env.ee_position_history = torch.roll(env.ee_position_history, -1, dims=0)
    env.ee_position_history[-1] = ee_pos
    
    
    max_position_change = torch.max(
        torch.norm(
            env.ee_position_history - env.ee_position_history[-1].unsqueeze(0),
            dim=2
        ),
        dim=0
    )[0]
    
    is_not_finished = ~multi_object_reached_goal_place(
        env,
        goal_threshold,
        robot_cfg,
        object_cfgs,
        place_cfgs
    )
    
    penalties = torch.zeros(env.num_envs, device=env.device)
    penalties[(max_position_change < position_threshold) & is_not_finished] = penalty
    
    return penalties