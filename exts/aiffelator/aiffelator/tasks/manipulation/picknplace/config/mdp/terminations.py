# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Common functions that can be used to activate certain terminations for the lift task.

The functions can be passed to the :class:`omni.isaac.lab.managers.TerminationTermCfg` object to enable
the termination introduced by the function.
"""

from __future__ import annotations

import torch
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.utils.math import combine_frame_transforms

if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv

from .scenes import AiffelatorScenes


def object_reached_goal(
    env: ManagerBasedRLEnv,
    command_name: str = "object_pose",
    threshold: float = 0.02,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
) -> torch.Tensor:
    """Termination condition for the object reaching the goal position.

    Args:
        env: The environment.
        command_name: The name of the command that is used to control the object.
        threshold: The threshold for the object to reach the goal position. Defaults to 0.02.
        robot_cfg: The robot configuration. Defaults to SceneEntityCfg("robot").
        object_cfg: The object configuration. Defaults to SceneEntityCfg("object").

    """
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
    return distance < threshold

def is_reached(env, threshold, robot_cfg, object_cfg, place_cfg):
    robot: RigidObject = env.scene[robot_cfg.name]
    object: RigidObject = env.scene[object_cfg.name]
    # compute the desired position in the world frame
    des_pos_b = AiffelatorScenes.place_position(name=place_cfg.name, num_envs=env.num_envs, device=object.device)
    des_pos_w, _ = combine_frame_transforms(robot.data.root_state_w[:, :3], robot.data.root_state_w[:, 3:7], des_pos_b)
    # distance of the end-effector to the object: (num_envs,)
    distance = torch.norm(des_pos_w - object.data.root_pos_w[:, :3], dim=1)

    # rewarded if the object is lifted above the threshold
    return distance < threshold

def object_reached_goal_place(
    env: ManagerBasedRLEnv,
    threshold: float = 0.02,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    place_cfg: SceneEntityCfg = SceneEntityCfg("place")
) -> torch.Tensor:
    # extract the used quantities (to enable type-hinting)
    return is_reached(
        env=env, 
        threshold=threshold, 
        robot_cfg=robot_cfg, 
        object_cfg=object_cfg, 
        place_cfg=place_cfg
    )

def multi_object_reached_goal_place(
    env: ManagerBasedRLEnv,
    threshold: float = 0.02,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    object_cfgs: list[SceneEntityCfg] = [SceneEntityCfg("object")],
    place_cfgs: list[SceneEntityCfg] = [SceneEntityCfg("place")]
) -> torch.Tensor:
    
    all_result = torch.full((env.num_envs,), True, device=env.device) # torch.tensor(True, device=env.device)

    for object, place in zip(object_cfgs, place_cfgs):
        result = is_reached(
            env=env, 
            threshold=threshold, 
            robot_cfg=robot_cfg, 
            object_cfg=object, 
            place_cfg=place
        )
        all_result &= result

    # rewarded if the object is lifted above the threshold
    return all_result