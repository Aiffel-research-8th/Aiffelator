from omni.isaac.lab.utils import configclass
from omni.isaac.lab.envs import ManagerBasedRLEnvCfg

from .config.reward_cfg import SingleObjectRewardsCfg, MultiObjectRewardsCfg
from .config.termination_cfg import SingleObjectTerminationsCfg, MultiObjectTerminationsCfg
from .config.scene_cfg import DeskSingleObjectSceneCfg, DeskMultiObjectSceneCfg
from .config.observation_cfg import DeskSingleObjectObservationsCfg, DeskMultiObjectObservationsCfg
from .config.action_cfg import ActionsCfg
from .config.command_cfg import SingleObjectCommandsCfg, MultiObjectCommandsCfg
from .config.event_cfg import SingleObjectEventCfg, MultiObjectEventCfg


@configclass
class SingleObjectPickAndPlaceEnvCfg_V0(ManagerBasedRLEnvCfg):
    # TODO 전체 Term Module 등록

    # MDP settings
    scene: DeskSingleObjectSceneCfg = DeskSingleObjectSceneCfg(num_envs=32, env_spacing=3)
    observations: DeskSingleObjectObservationsCfg = DeskSingleObjectObservationsCfg()
    actions: ActionsCfg = ActionsCfg()
    commands: SingleObjectCommandsCfg = SingleObjectCommandsCfg()
    resets: SingleObjectEventCfg = SingleObjectEventCfg()
    
    rewards: SingleObjectRewardsCfg = SingleObjectRewardsCfg()
    terminations: SingleObjectTerminationsCfg = SingleObjectTerminationsCfg()

    def __post_init__(self):
        """Post initialization."""
        # general settings
        self.decimation = 2
        self.episode_length_s = 5.0
        # simulation settings
        self.sim.dt = 0.01  # 100Hz
        self.sim.render_interval = self.decimation

        self.sim.physx.bounce_threshold_velocity = 0.2
        self.sim.physx.bounce_threshold_velocity = 0.01
        self.sim.physx.gpu_found_lost_aggregate_pairs_capacity = 1024 * 1024 * 4
        self.sim.physx.gpu_total_aggregate_pairs_capacity = 16 * 1024
        self.sim.physx.friction_correlation_distance = 0.00625

@configclass
class SingleObjectPickAndPlaceEnvCfg_V0_PLAY(SingleObjectPickAndPlaceEnvCfg_V0):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # make a smaller scene for play
        self.scene.num_envs = 16
        self.scene.env_spacing = 3
        # disable randomization for play
        self.observations.policy.enable_corruption = False

@configclass
class MultiObjectPickAndPlaceEvnCfg_V0(ManagerBasedRLEnvCfg):
    
    scene: DeskMultiObjectSceneCfg = DeskMultiObjectSceneCfg(num_envs=32, env_spacing=3)
    observations: DeskMultiObjectObservationsCfg = DeskMultiObjectObservationsCfg()
    actions: ActionsCfg = ActionsCfg()
    commands: MultiObjectCommandsCfg = MultiObjectCommandsCfg()
    resets: MultiObjectEventCfg = MultiObjectEventCfg()

    rewards: MultiObjectRewardsCfg = MultiObjectRewardsCfg()
    terminations: MultiObjectTerminationsCfg = MultiObjectTerminationsCfg()
    
    def __post_init__(self):

        self.decimation = 2
        self.episode_length_s = 15.0 # multi pick and place 고려

        self.sim.dt = 0.01  # 100Hz
        self.sim.render_interval = self.decimation

        self.sim.physx.bounce_threshold_velocity = 0.2
        self.sim.physx.bounce_threshold_velocity = 0.01
        self.sim.physx.gpu_found_lost_aggregate_pairs_capacity = 1024 * 1024 * 4
        self.sim.physx.gpu_total_aggregate_pairs_capacity = 16 * 1024
        self.sim.physx.friction_correlation_distance = 0.00625
        
@configclass
class MultiObjectPickAndPlaceEvnCfg_V0_PLAY(MultiObjectPickAndPlaceEvnCfg_V0):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # make a smaller scene for play
        self.scene.num_envs = 16
        self.scene.env_spacing = 3
        # disable randomization for play
        self.observations.policy.enable_corruption = False