import gymnasium as gym

from .pick_place_env_cfg import SingleTablePickAndPlaceEnvCfg
from . import agents

gym.register(
    id="Isaac-SingleTablePickAndPlace-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": SingleTablePickAndPlaceEnvCfg,
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:PickAndPlacePPORunnerCfg"
    },
)