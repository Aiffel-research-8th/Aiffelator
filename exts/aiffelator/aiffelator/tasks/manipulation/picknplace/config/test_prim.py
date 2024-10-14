# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""This script demonstrates how to use the interactive scene interface to setup a scene with multiple prims.

.. code-block:: bash

    # Usage
    ./isaaclab.sh -p source/standalone/tutorials/02_scene/create_scene.py --num_envs 32

"""

"""Launch Isaac Sim Simulator first."""


import argparse

from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="Tutorial on using the interactive scene interface.")
parser.add_argument("--num_envs", type=int, default=2, help="Number of environments to spawn.")
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
args_cli = parser.parse_args()

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest everything follows."""

import torch

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.scene import InteractiveScene, InteractiveSceneCfg
from omni.isaac.lab.sim import SimulationContext
from omni.isaac.lab.utils import configclass

##
# Pre-defined configs
##
from omni.isaac.lab_assets import CARTPOLE_CFG  # isort:skip

import omni.isaac.lab.sim as sim_utils

from mdp import AiffelatorScenes
from dataclasses import MISSING

@configclass
class DeskSingleObjectSceneCfg(InteractiveSceneCfg):
    
    # default env
    plane, light, table, bookcase = AiffelatorScenes.default_environment()
    # camera set
    front_camera, right_camera = AiffelatorScenes.camera_set()
    # manipulator
    robot, ee_frame = AiffelatorScenes.manipulator()
    # pencil_case set
    pencil_case, place_pencil_case = AiffelatorScenes.pencil_case_set("desk")

@configclass
class DeskMultiObjectSceneCfg(InteractiveSceneCfg):
    
    # default env
    plane, light, table, bookcase = AiffelatorScenes.default_environment()
    # camera set
    front_camera, right_camera = AiffelatorScenes.camera_set()
    # manipulator
    robot, ee_frame = AiffelatorScenes.manipulator()
    # pencil_case set
    pencil_case, place_pencil_case = AiffelatorScenes.pencil_case_set("desk")
    # pen set
    pen, place_pen = AiffelatorScenes.pen_set("desk")

@configclass
class BookcaseMultiObjectSceneCfg(InteractiveSceneCfg):

    # default env
    plane, light, table, bookcase = AiffelatorScenes.default_environment()
    # camera set
    front_camera, right_camera = AiffelatorScenes.camera_set()
    # manipulator
    robot, ee_frame = AiffelatorScenes.manipulator()
    # pencil_case set
    pencil_case, place_pencil_case = AiffelatorScenes.pencil_case_set("bookcase")
    # pen set
    pen, place_pen = AiffelatorScenes.pen_set("bookcase")


def run_simulator(sim: sim_utils.SimulationContext, scene: InteractiveScene):
    """Runs the simulation loop."""
    # Extract scene entities
    # Define simulation stepping
    sim_dt = sim.get_physics_dt()
    count = 0
    # Simulation loop
    while simulation_app.is_running():

        # Apply random action
        # -- write data to sim
        scene.write_data_to_sim()
        # Perform step
        sim.step()
        # Increment counter
        count += 1
        # Update buffers
        scene.update(sim_dt)


def main():
    """Main function."""
    # Load kit helper
    sim_cfg = sim_utils.SimulationCfg(device=args_cli.device)
    sim = SimulationContext(sim_cfg)
    # Set main camera
    sim.set_camera_view([2.5, 0.0, 4.0], [0.0, 0.0, 2.0])
    # Design scene
    scene_cfg = DeskMultiObjectSceneCfg(num_envs=args_cli.num_envs, env_spacing=2.0)
    scene = InteractiveScene(scene_cfg)
    # Play the simulator
    sim.reset()
    # Now we are ready!
    print("[INFO]: Setup complete...")
    # Run the simulator
    run_simulator(sim, scene)


if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()