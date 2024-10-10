# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""This script demonstrates how to spawn prims into the scene.

.. code-block:: bash

    # Usage
    ./isaaclab.sh -p source/standalone/tutorials/00_sim/spawn_prims.py

"""

"""Launch Isaac Sim Simulator first."""


import argparse

from omni.isaac.lab.app import AppLauncher

# create argparser
parser = argparse.ArgumentParser(description="Tutorial on spawning prims into the scene.")
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
args_cli = parser.parse_args()
# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

"""Rest everything follows."""

import omni.isaac.lab.sim as sim_utils

from mdp import AiffelatorScenes
from omni.isaac.lab.managers import SceneEntityCfg

def design_scene():
    # load usd
    desk = sim_utils.UsdFileCfg(usd_path=AiffelatorScenes.SimpleDesk.SingleObject.usd_path)
    desk.func(AiffelatorScenes.SimpleDesk.SingleObject.prim_path, desk)

    # franka
    robot = sim_utils.UsdFileCfg(usd_path=AiffelatorScenes.Franka.usd_path)
    robot.func(AiffelatorScenes.Franka.prim_path, 
                    robot, 
                    translation=(0.0, 0.0, 1.0),
                    orientation=(0, 0, 0, 0))

    # pencil_case place
    place_pencil_case = sim_utils.UsdFileCfg(usd_path=AiffelatorScenes.Place.PencilCase.usd_path)
    place_pencil_case.func(AiffelatorScenes.Place.PencilCase.prim_path, 
                               place_pencil_case, 
                               translation=(-0.4, 0.3, 1.005), 
                               orientation=(0, 0, 0, 0))


def main():
    """Main function."""

    # Initialize the simulation context
    sim_cfg = sim_utils.SimulationCfg(dt=0.01, device=args_cli.device)
    sim = sim_utils.SimulationContext(sim_cfg)
    # Set main camera
    sim.set_camera_view([2.0, 0.0, 2.5], [-0.5, 0.0, 0.5])

    # Design scene by adding assets to it
    design_scene()

    # Play the simulator
    sim.reset()
    # Now we are ready!
    print("[INFO]: Setup complete...")

    # Simulate physics
    while simulation_app.is_running():
        # perform step
        sim.step()



if __name__ == "__main__":
    # run the main function
    main()
    # close sim app
    simulation_app.close()