from omni.isaac.lab.utils import configclass
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.managers import TerminationTermCfg as DoneTerm
from . import mdp

# specific to this task and env: -
# Common to all tasks: time_out, joint_pos_out_of_manual_limit


@configclass
class SingleObjectTerminationsCfg:
    """Termination terms for the MDP."""

    # TODO Termination Term 구현
    # (1) Time out
    time_out = DoneTerm(func=mdp.time_out, time_out=True)
    
    # (2) Final Goal is achived
    object_reached_goal = DoneTerm( 
        func=mdp.object_reached_goal_place,
        params={"threshold": 0.02,
                "robot_cfg": SceneEntityCfg("robot"),
                "object_cfg": SceneEntityCfg("pencil_case"),
                "place_cfg": SceneEntityCfg("place_pencil_case")
                },
    )