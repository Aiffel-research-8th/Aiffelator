from omni.isaac.lab.utils import configclass
from omni.isaac.lab.managers import EventTermCfg as EventTerm
from omni.isaac.lab.managers import SceneEntityCfg

from . import mdp

@configclass
class SingleObjectEventCfg:
    """Configuration for events."""

    reset_all = EventTerm(func=mdp.reset_scene_to_default, mode="reset")

    pencil_case_position = EventTerm(
        func=mdp.reset_root_state_uniform,
        mode="reset",
        params={
            "pose_range": {"x": (0.34492, 0.36121), "y": (0.00125, 0.28943), "z": (1.03803, 1.03803)},
            "velocity_range": {},
            "asset_cfg": SceneEntityCfg("pencil_case"),
        },
    )

@configclass
class MultiObjectEventCfg:
    """Configuration for events."""

    reset_all = EventTerm(func=mdp.reset_scene_to_default, mode="reset")

    pencil_case_position = EventTerm(
        func=mdp.reset_root_state_uniform,
        mode="reset",
        params={
            "pose_range": {"x": (0.34492, 0.36121), "y": (0.00125, 0.28943), "z": (1.03803, 1.03803)},
            "velocity_range": {},
            "asset_cfg": SceneEntityCfg("pencil_case"),
        },
    )
    
    pen_position = EventTerm(
        func=mdp.reset_root_state_uniform,
        mode="reset",
        params={
            "pose_range": {"x": (-0.31933, 0.00456), "y": (-0.49667, -0.41844), "z": (1.00951, 1.00951)},
            "velocity_range": {},
            "asset_cfg": SceneEntityCfg("pen"),
        },
    )