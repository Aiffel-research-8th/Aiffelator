import gymnasium as gym

from .pick_place_env_cfg import SingleObjectPickAndPlaceEnvCfg
from . import agents

gym.register(
    id="Isaac-Aiffelator-SingleObject-PickAndPlace-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": SingleObjectPickAndPlaceEnvCfg,
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:SingleTablePickAndPlacePPORunnerCfg"
    },
)