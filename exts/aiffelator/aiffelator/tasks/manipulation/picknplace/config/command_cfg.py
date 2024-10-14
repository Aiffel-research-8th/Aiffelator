from dataclasses import MISSING

from omni.isaac.lab.utils import configclass

from . import mdp

@configclass
class SingleObjectCommandsCfg:
    """Command terms for the MDP."""
    
    # UniformPoseCommandCfg는 uniform pose command generator
    # object_pose = mdp.UniformPoseCommandCfg( # CommandTermCfg 하위 클래스
    #     asset_name="robot",
    #     body_name=MISSING,  # will be set by agent env cfg
    #     resampling_time_range=(5.0, 5.0),
    #     debug_vis=True,
    #     ranges=mdp.UniformPoseCommandCfg.Ranges(
    #         pos_x=(0.4, 0.6), pos_y=(-0.25, 0.25), pos_z=(0.25, 0.5), 
    #         roll=(0.0, 0.0), pitch=(0.0, 0.0), yaw=(0.0, 0.0)
    #     ),
    # )

    # no commands for this mdp
    null = mdp.NullCommandCfg()