from omni.isaac.lab.utils import configclass
from omni.isaac.lab.envs import ManagerBasedRLEnvCfg

from .config.reward_cfg import SingleObjectRewardsCfg
from .config.termination_cfg import SingleObjectTerminationsCfg
from .config.scene_cfg import DeskSingleObjectSceneCfg
from .config.observation_cfg import DeskSingleObjectObservationsCfg
from .config.action_cfg import ActionsCfg
from .config.command_cfg import SingleObjectCommandsCfg
from .config.event_cfg import SingleObjectEventCfg


@configclass
class SingleObjectPickAndPlaceEnvCfg(ManagerBasedRLEnvCfg):
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
