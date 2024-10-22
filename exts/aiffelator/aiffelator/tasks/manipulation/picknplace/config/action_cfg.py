from omni.isaac.lab.utils import configclass
from omni.isaac.lab.managers.action_manager import ActionTerm, ActionTermCfg
from dataclasses import MISSING

from . import mdp

@configclass
class ActionsCfg:
    """Action specifications for the MDP."""

    arm_action: mdp.JointPositionActionCfg = mdp.JointPositionActionCfg(
        asset_name="robot", joint_names=["panda_joint.*"], scale=0.5, use_default_offset=True
    )
    
    gripper_action = mdp.BinaryJointPositionActionCfg(
            asset_name="robot",
            joint_names=["panda_finger.*"],
            open_command_expr={"panda_finger_.*": 0.04},
            close_command_expr={"panda_finger_.*": 0.0},
        )