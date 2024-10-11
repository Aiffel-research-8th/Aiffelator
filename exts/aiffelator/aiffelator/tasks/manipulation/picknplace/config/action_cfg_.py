from omni.isaac.lab.utils import configclass
from omni.isaac.lab.managers.action_manager import ActionTerm, ActionTermCfg
from dataclasses import MISSING

from . import mdp

@configclass
class ActionsCfg:
    """Action specifications for the MDP."""

    arm_action: mdp.JointPositionActionCfg = mdp.JointPositionActionCfg( # ActionTermCfg 하위 클래스, isaaclab 에서 제공하는 joint position action
        asset_name="robot", joint_names=["panda_joint.*"], scale=0.5, use_default_offset=True # 에셋 이름, 조인트 이름, scale 설정, scale은 각 조인트의 action의 정도를 기술
    )
    # asset_name 장면 구성 파일에 정의된 이름(InteractiveSceneCfg/DeskSingleObjectSceneCfg)
    
    gripper_action = mdp.BinaryJointPositionActionCfg(
            asset_name="robot",
            joint_names=["panda_finger.*"], # 엔드 이펙터
            open_command_expr={"panda_finger_.*": 0.04}, # 열림
            close_command_expr={"panda_finger_.*": 0.0}, # 닫힘
        )