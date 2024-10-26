from omni.isaac.lab.utils import configclass
from omni.isaac.lab.managers import EventTermCfg as EventTerm
from omni.isaac.lab.managers import SceneEntityCfg

from . import mdp
from .mdp import AiffelatorScenes

@configclass
class SingleObjectEventCfg:
    """Configuration for events."""

    reset_all = EventTerm(func=mdp.reset_scene_to_default, mode="reset")

    # reset_pencil_case_position = EventTerm(
    #     func=mdp.reset_root_state_uniform,
    #     mode="reset",
    #     params={
    #         "pose_range": AiffelatorScenes.Object.PencilCase.pose_range,
    #         "velocity_range": {},
    #         "asset_cfg": SceneEntityCfg("pencil_case"),
    #     },
    # )

@configclass
class MultiObjectEventCfg:
    """Configuration for events."""

    reset_all = EventTerm(func=mdp.reset_scene_to_default, mode="reset")

    # reset_pencil_case_position = EventTerm(
    #     func=mdp.reset_root_state_uniform,
    #     mode="reset",
    #     params={
    #         "pose_range": AiffelatorScenes.Object.PencilCase.pose_range,
    #         "velocity_range": {},
    #         "asset_cfg": SceneEntityCfg("pencil_case"),
    #     },
    # )
    
    # reset_pen_position = EventTerm(
    #     func=mdp.reset_root_state_uniform,
    #     mode="reset",
    #     params={
    #         "pose_range": AiffelatorScenes.Object.Pen.pose_range,
    #         "velocity_range": {},
    #         "asset_cfg": SceneEntityCfg("pen"),
    #     },
    # )