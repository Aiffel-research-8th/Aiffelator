from omni.isaac.lab.managers import RewardTermCfg as RewTerm
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.utils import configclass

from . import mdp
from .mdp import AiffelatorScenes

# specific to this task and env: object_ee_distance, object_is_lifted, object_goal_distance
# Common to all tasks: action_rate_l2, joint_vel_l2


@configclass
class SingleObjectRewardsCfg:
    """Reward terms for the MDP."""
    # (1) reaching the object
    reaching_object = RewTerm(
        func=mdp.object_ee_distance, 
        params={
            "std": 0.1,
            "object_cfg": AiffelatorScenes.Object.PencilCase.get(),
            "ee_frame_cfg": SceneEntityCfg("ee_frame")
        }, 
        weight=1.0
    )

    # (2) pick and lift the object
    # NOTE : picking reward would not be nessacery
    lifting_object = RewTerm(
        func=mdp.object_is_lifted_2, 
        params={
            "minimal_height": 0.055,
            "maximum_height": 0.12,
            "object_cfg": AiffelatorScenes.Object.PencilCase.get()
        }, 
        weight=15.0
    )

    # (3) delivering an object to the goal
    object_goal_tracking = RewTerm(
        func=mdp.object_goal_place_distance,
        params={
            "std": 0.3, 
            "minimal_height": 0.055,
            "robot_cfg": SceneEntityCfg("robot"),
            "object_cfg": AiffelatorScenes.Object.PencilCase.get(),
            "place_cfg": AiffelatorScenes.Place.PencilCase.get()
        },
        weight=16.0,
    )

    object_goal_tracking_fine_grained = RewTerm(
        func=mdp.object_goal_place_distance,
        params={
            "std": 0.3, 
            "minimal_height": 0.055,
            "robot_cfg": SceneEntityCfg("robot"),
            "object_cfg": AiffelatorScenes.Object.PencilCase.get(),
            "place_cfg": AiffelatorScenes.Place.PencilCase.get()
        },
        weight=5.0,
    )
    # Failure penalty
    # # object is out of limits 
    # # TODO
    # # dropping object
    # # TODO
    # Action penalty
    # # penalize the rate of change of the actions using L2 squared kernel.
    action_rate = RewTerm(func=mdp.action_rate_l2, weight=-1e-4)
    # # slower joint velocity
    joint_vel = RewTerm(
        func=mdp.joint_vel_l2,
        weight=-1e-4,
        params={"asset_cfg": SceneEntityCfg("robot")},
    )


@configclass
class MultiObjectRewardsCfg:
    """Reward terms for the MDP."""
    # (1) reaching to the object
    reaching_pencil_case = RewTerm(
        func=mdp.object_ee_distance, 
        params={
            "std": 0.1,
            "object_cfg": AiffelatorScenes.Object.PencilCase.get(),
            "ee_frame_cfg": SceneEntityCfg("ee_frame")
        }, 
        weight=1.0
    )

    reaching_pen = RewTerm(
        func=mdp.object_ee_distance,
        params={
            "std": 0.1,
            "object_cfg": AiffelatorScenes.Object.Pen.get(),
            "ee_frame_cfg": SceneEntityCfg("ee_frame")
        },
        weight=1.0
    )

    # (2) pick and lift the object
    # NOTE : picking reward would not be nessacery
    lifting_pencil_case = RewTerm(
        func=mdp.object_is_lifted_2, 
        params={
            "minimal_height": 0.055,
            "maximum_height": 0.12,
            "object_cfg": AiffelatorScenes.Object.PencilCase.get()
        }, 
        weight=15.0
    )
    lifting_pen = RewTerm(
        func=mdp.object_is_lifted_2, 
        params={
            "minimal_height": 0.04,
            "maximum_height": 0.10,
            "object_cfg": AiffelatorScenes.Object.Pen.get()
        }, 
        weight=15.0
    )

    # (3) delivering an object to the goal
    pencil_case_goal_tracking = RewTerm(
        func=mdp.object_goal_place_distance,
        params={
            "std": 0.3, 
            "minimal_height": 0.055,
            "robot_cfg": SceneEntityCfg("robot"),
            "object_cfg": AiffelatorScenes.Object.PencilCase.get(),
            "place_cfg": AiffelatorScenes.Place.PencilCase.get()
        },
        weight=16.0,
    )

    pencil_case_goal_tracking_fine_grained = RewTerm(
        func=mdp.object_goal_place_distance,
        params={
            "std": 0.3, 
            "minimal_height": 0.055,
            "robot_cfg": SceneEntityCfg("robot"),
            "object_cfg": AiffelatorScenes.Object.PencilCase.get(),
            "place_cfg": AiffelatorScenes.Place.PencilCase.get()
        },
        weight=5.0,
    )
    
    pen_goal_tracking = RewTerm(
        func=mdp.object_goal_place_distance,
        params={
            "std": 0.3, 
            "minimal_height": 0.04,
            "robot_cfg": SceneEntityCfg("robot"),
            "object_cfg": AiffelatorScenes.Object.Pen.get(),
            "place_cfg": AiffelatorScenes.Place.Pen.get()
        },
        weight=16.0,
    )

    pen_goal_tracking_fine_grained = RewTerm(
        func=mdp.object_goal_place_distance,
        params={
            "std": 0.3, 
            "minimal_height": 0.04,
            "robot_cfg": SceneEntityCfg("robot"),
            "object_cfg": AiffelatorScenes.Object.Pen.get(),
            "place_cfg": AiffelatorScenes.Place.Pen.get()
        },
        weight=5.0,
    )
    
    # completed_task = RewTerm( 
    #     func=mdp.complete_task,
    #     params={
    #         "threshold": 0.1,
    #         "robot_cfg": SceneEntityCfg("robot"),
    #         "object_cfgs": [
    #             AiffelatorScenes.Object.PencilCase.get(), 
    #             AiffelatorScenes.Object.Pen.get()
    #         ],
    #         "place_cfgs": [
    #             AiffelatorScenes.Place.PencilCase.get(), 
    #             AiffelatorScenes.Place.Pen.get()
    #         ]
    #     },
    #     weight=32.0,
    # )
    
    # collision_cube = RewTerm(func=mdp.collision_place_cube, weight=-2.0)
    
    # Failure penalty
    # # object is out of limits
    # # TODO
    # # dropping object
    # # TODO
    # Action penalty
    action_rate = RewTerm(func=mdp.action_rate_l2, weight=-1e-4)

    joint_vel = RewTerm(
        func=mdp.joint_vel_l2,
        weight=-1e-4,
        params={"asset_cfg": SceneEntityCfg("robot")},
    )
    
    stagnation_penalty = RewTerm(
        func=mdp.stagnation_penalty,
        params={
            "history_size": 50,
            "penalty": -5.0,
            "position_threshold": 0.02,
            "goal_threshold": 0.02,
            "robot_cfg": SceneEntityCfg("robot"),
            "ee_frame_cfg": SceneEntityCfg("ee_frame"),
            "object_cfgs": [
                AiffelatorScenes.Object.PencilCase.get(), 
                AiffelatorScenes.Object.Pen.get()
            ],
            "place_cfgs": [
                AiffelatorScenes.Place.PencilCase.get(), 
                AiffelatorScenes.Place.Pen.get()
            ]
        },
        weight=1.0
    )
    
    # dropped_objects = RewTerm(
    #     func=mdp.drop_objects,
    #     params={
    #         "object_cfgs": [ AiffelatorScenes.Object.PencilCase.get(), AiffelatorScenes.Object.Pen.get() ]
    #     },
    #     weight=-16.0,
    # )