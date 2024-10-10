from omni.isaac.lab.utils import configclass
from omni.isaac.lab.envs import ManagerBasedRLEnvCfg

from config.reward_cfg import FlatTableOneObjRewardsCfg
from config.termination_cfg import TerminationsCfg


@configclass
class SingleTablePickAndPlaceEnvCfg(ManagerBasedRLEnvCfg):
    # TODO 전체 Term Module 등록

    # MDP settings
    rewards: FlatTableOneObjRewardsCfg = FlatTableOneObjRewardsCfg()
    terminations: TerminationsCfg = TerminationsCfg()

    def __post_init__(self):
        """Post initialization."""
        pass
