from omni.isaac.lab.utils import configclass
from omni.isaac.lab.managers import ObservationGroupCfg as ObsGroup
from omni.isaac.lab.managers import ObservationTermCfg as ObsTerm
from omni.isaac.lab.managers import SceneEntityCfg

from . import mdp

@configclass
class DeskSingleObjectObservationsCfg:

    @configclass
    class PolicyCfg(ObsGroup):

        joint_pos = ObsTerm(func=mdp.joint_pos_rel)
        joint_vel = ObsTerm(func=mdp.joint_vel_rel)
        pencil_case_position = ObsTerm(
            func=mdp.object_position_in_robot_root_frame, 
            params={
                "object": SceneEntityCfg("pencil_case")
            }
        )
        target_object_position = ObsTerm(
            func=mdp.generated_commands, 
            params={"command_name": "object_pose"}
        )
        actions = ObsTerm(func=mdp.last_action)

        def __post_init__(self):
            self.enable_corruption = True
            self.concatenate_terms = True

    # observation groups
    policy: PolicyCfg = PolicyCfg()

@configclass
class DeskMultiObjectObservationsCfg:

    @configclass
    class PolicyCfg(ObsGroup):

        joint_pos = ObsTerm(func=mdp.joint_pos_rel)
        joint_vel = ObsTerm(func=mdp.joint_vel_rel)
        pencil_case_position = ObsTerm(
            func=mdp.object_position_in_robot_root_frame, 
            params={
                "object": SceneEntityCfg("pencil_case")
            }
        )
        pen_position = ObsTerm(
            func=mdp.object_position_in_robot_root_frame, 
            params={
                "object": SceneEntityCfg("pen")
            }
        )
        target_object_position = ObsTerm(
            func=mdp.generated_commands, 
            params={"command_name": "object_pose"}
        )
        actions = ObsTerm(func=mdp.last_action)

        def __post_init__(self):
            self.enable_corruption = True
            self.concatenate_terms = True

    # observation groups
    policy: PolicyCfg = PolicyCfg()

@configclass
class BookcaseSingleObjectObservationsCfg:

    @configclass
    class PolicyCfg(ObsGroup):

        joint_pos = ObsTerm(func=mdp.joint_pos_rel)
        joint_vel = ObsTerm(func=mdp.joint_vel_rel)
        pencil_case_position = ObsTerm(
            func=mdp.object_position_in_robot_root_frame, 
            params={
                "object": SceneEntityCfg("pencil_case")
            }
        )
        target_object_position = ObsTerm(
            func=mdp.generated_commands, 
            params={"command_name": "object_pose"}
        )
        actions = ObsTerm(func=mdp.last_action)

        def __post_init__(self):
            self.enable_corruption = True
            self.concatenate_terms = True

    # observation groups
    policy: PolicyCfg = PolicyCfg()

@configclass
class BookcaseMultiObjectObservationsCfg:

    @configclass
    class PolicyCfg(ObsGroup):

        joint_pos = ObsTerm(func=mdp.joint_pos_rel)
        joint_vel = ObsTerm(func=mdp.joint_vel_rel)
        pencil_case_position = ObsTerm(
            func=mdp.object_position_in_robot_root_frame, 
            params={
                "object": SceneEntityCfg("pencil_case")
            }
        )
        pen_position = ObsTerm(
            func=mdp.object_position_in_robot_root_frame, 
            params={
                "object": SceneEntityCfg("pen")
            }
        )
        target_object_position = ObsTerm(
            func=mdp.generated_commands, 
            params={"command_name": "object_pose"}
        )
        actions = ObsTerm(func=mdp.last_action)

        def __post_init__(self):
            self.enable_corruption = True
            self.concatenate_terms = True

    # observation groups
    policy: PolicyCfg = PolicyCfg()