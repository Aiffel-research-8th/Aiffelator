import torch

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg
from omni.isaac.lab.sim.spawners.from_files.from_files_cfg import GroundPlaneCfg
from omni.isaac.lab.assets import RigidObjectCfg
from omni.isaac.lab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg
from omni.isaac.lab_assets.franka import FRANKA_PANDA_CFG

from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import FrameTransformerCfg
from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import OffsetCfg
from omni.isaac.lab.sensors import CameraCfg

class AiffelatorScenes:

    class Place:
        class Pen:
            usd_path = "omniverse://localhost/Projects/aiffelator/place_pen.usd"
            name = "place_pen"
            prim_path = "{ENV_REGEX_NS}/place_pen"
            pos = (0.03, -0.5, 0.01), (-0.65, -0.2, 0.075) # desk, bookcase
            rot = [0, 0, 0, 0]
            scale = (1.0, 1.0, 1.0)
            pose_range = {"x": (-0.08, 0.03), "y": (-0.5, -0.35), "z": (0.01, 0.01)}

        class PencilCase:
            usd_path = "omniverse://localhost/Projects/aiffelator/place_pencil_case.usd"
            name = "place_pencil_case"
            prim_path = "{ENV_REGEX_NS}/place_pencil_case"
            pos = (0.03, 0.5, 0.01), (-0.65, 0.2,0.415) # desk, bookcase
            rot = [0, 0, 0, 0]
            scale = (1.0, 1.0, 1.0)
            pose_range = {"x": (-0.08, 0.03), "y": (0.35, 0.5), "z": (0.01, 0.01)}

    class Table:
        usd_path = "{ISAAC_NUCLEUS_DIR}/Props/Mounts/SeattleLabTable/table_instanceable.usd"
        name = "Table"
        prim_path = "{ENV_REGEX_NS}/Table"
        pos = [0.5, 0, 0]
        rot = [0.70711, 0, 0, 0.70711]
        scale = (1.5, 1.0, 1.0)
    
    class Bookcase:
        usd_path = "omniverse://localhost/NVIDIA/Assets/ArchVis/Commercial/Storage/WhiteHome02.usd"
        name = "Bookcase"
        prim_path = "{ENV_REGEX_NS}/Bookcase"
        pos = [-0.7, 0, -1.05]
        rot = [0.70711, 0, 0, 0.70711]
        scale = (1.5, 1.0, 1.0)

    class Object:
        class PencilCase:
            usd_path = "omniverse://localhost/Projects/aiffelator/pencil_case.usd"
            name = "PencilCase"
            prim_path = "{ENV_REGEX_NS}/PencilCase"
            pos = [0.5, 0.3, 0.037]
            rot = [1, 0, 0, 0]
            scale = (0.002, 0.002, 0.002)
            pose_range = {"x": (0.32, 0.45), "y": (0.18, 0.45), "z": (0.037, 0.037)}

        class Pen:
            usd_path = "omniverse://localhost/Projects/aiffelator/pen.usd"
            name = "Pen"
            prim_path = "{ENV_REGEX_NS}/Pen"
            pos = [0.5, -0.3, 0.01]
            rot = [0.70711, 0.70711, 0, 0]
            scale = (0.001, 0.001, 0.001)
            pose_range = {"x": (0.32, 0.45), "y": (-0.45, -0.18), "z": (0.01, 0.01)}

    @staticmethod
    def ground_plane() -> AssetBaseCfg:
        return AssetBaseCfg(
            prim_path="/World/GroundPlane",
            init_state=AssetBaseCfg.InitialStateCfg(pos=[0, 0, -1.05]),
            spawn=GroundPlaneCfg(),
        )
    
    @staticmethod
    def light() -> AssetBaseCfg:
        return AssetBaseCfg(
            prim_path="/World/light",
            spawn=sim_utils.DomeLightCfg(color=(0.75, 0.75, 0.75), intensity=3000.0),
        )

    @staticmethod
    def table() -> AssetBaseCfg:
        return AssetBaseCfg(
            prim_path=AiffelatorScenes.Table.prim_path,
            init_state=AssetBaseCfg.InitialStateCfg(
                pos=AiffelatorScenes.Table.pos, 
                rot=AiffelatorScenes.Table.rot
            ),
            spawn=sim_utils.UsdFileCfg(
                usd_path=AiffelatorScenes.Table.usd_path,
                scale=AiffelatorScenes.Table.scale
            )
        )

    @staticmethod
    def bookcase() -> AssetBaseCfg:
        return  AssetBaseCfg(
            prim_path=AiffelatorScenes.Bookcase.prim_path,
            init_state=AssetBaseCfg.InitialStateCfg(
                pos=AiffelatorScenes.Bookcase.pos, 
                rot=AiffelatorScenes.Bookcase.rot
            ),
            spawn=sim_utils.UsdFileCfg(
                usd_path=AiffelatorScenes.Bookcase.usd_path,
                scale=AiffelatorScenes.Bookcase.scale
            ),
        )

    @staticmethod
    def camera(prim_name: str, pos: tuple[float, float, float], rot: tuple[float, float, float, float]) -> CameraCfg:
        prefix = "{ENV_REGEX_NS}"
        return CameraCfg(
            prim_path=f"{prefix}/{prim_name}",
            update_period=0.1,
            height=480,
            width=640,
            data_types=["rgb", "distance_to_image_plane"],
            spawn=sim_utils.PinholeCameraCfg(
                focal_length=24.0, focus_distance=400.0, horizontal_aperture=20.955, clipping_range=(0.1, 1.0e5)
            ),
            offset=CameraCfg.OffsetCfg(
                pos=pos, 
                rot=rot, # 0, 47, 90
                convention="opengl"
            )
        )

    @staticmethod
    def front_camera() -> CameraCfg:
        return AiffelatorScenes.camera(
            prim_name="front_cam",
            pos=(3.0, 0.0, 3.0), 
            rot=(0.64846, 0.28196, 0.28196, 0.64846) # 0, 47, 90
        )

    @staticmethod
    def right_camera() -> CameraCfg:
        return AiffelatorScenes.camera(
            prim_name="right_cam",
            pos=(2.6, 1.5, 2.8), 
            rot=(0.42998, 0.21975, 0.35343, 0.8012) # -30, 41, 135
        )

    @staticmethod
    def franka_panda() -> ArticulationCfg:
        return FRANKA_PANDA_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

    @staticmethod
    def pencil_case() -> RigidObjectCfg:
        return RigidObjectCfg(
            prim_path=AiffelatorScenes.Object.PencilCase.prim_path,
            init_state=RigidObjectCfg.InitialStateCfg(
                pos=AiffelatorScenes.Object.PencilCase.pos, 
                rot=AiffelatorScenes.Object.PencilCase.rot
            ),
            spawn=sim_utils.UsdFileCfg(
                usd_path=AiffelatorScenes.Object.PencilCase.usd_path,
                scale=AiffelatorScenes.Object.PencilCase.scale,
                rigid_props=RigidBodyPropertiesCfg(
                    solver_position_iteration_count=16,
                    solver_velocity_iteration_count=1,
                    max_angular_velocity=1000.0,
                    max_linear_velocity=1000.0,
                    max_depenetration_velocity=5.0,
                    disable_gravity=False,
                ),
            ),
        )
    
    @staticmethod
    def pen() -> RigidObjectCfg:
        return RigidObjectCfg(
        prim_path=AiffelatorScenes.Object.Pen.prim_path,
        init_state=RigidObjectCfg.InitialStateCfg(
            pos=AiffelatorScenes.Object.Pen.pos, 
            rot=AiffelatorScenes.Object.Pen.rot
        ),
        spawn=sim_utils.UsdFileCfg(
            usd_path=AiffelatorScenes.Object.Pen.usd_path,
            scale=AiffelatorScenes.Object.Pen.scale,
            rigid_props=RigidBodyPropertiesCfg(
                solver_position_iteration_count=16,
                solver_velocity_iteration_count=1,
                max_angular_velocity=1000.0,
                max_linear_velocity=1000.0,
                max_depenetration_velocity=5.0,
                disable_gravity=False,
            ),
        ),
    )

    @staticmethod
    def place_pencil_case(pos: tuple[float, float, float]) -> RigidObjectCfg:
        return RigidObjectCfg(
            prim_path=AiffelatorScenes.Place.PencilCase.prim_path,
            init_state=RigidObjectCfg.InitialStateCfg(
                pos=pos, 
                rot=AiffelatorScenes.Place.PencilCase.rot
            ),
            spawn=sim_utils.UsdFileCfg(
                usd_path=AiffelatorScenes.Place.PencilCase.usd_path,
                scale=AiffelatorScenes.Place.PencilCase.scale,
                rigid_props=RigidBodyPropertiesCfg(
                    solver_position_iteration_count=16,
                    solver_velocity_iteration_count=1,
                    max_angular_velocity=1000.0,
                    max_linear_velocity=1000.0,
                    max_depenetration_velocity=5.0,
                    disable_gravity=False,
                ),
            ),
        )
    
    @staticmethod
    def place_pen(pos: tuple[float, float, float]) -> RigidObjectCfg:
        return RigidObjectCfg(
        prim_path=AiffelatorScenes.Place.Pen.prim_path,
        init_state=RigidObjectCfg.InitialStateCfg(
            pos=pos, 
            rot=AiffelatorScenes.Place.Pen.rot
        ),
        spawn=sim_utils.UsdFileCfg(
            usd_path=AiffelatorScenes.Place.Pen.usd_path,
            scale=AiffelatorScenes.Place.Pen.scale,
            rigid_props=RigidBodyPropertiesCfg(
                solver_position_iteration_count=16,
                solver_velocity_iteration_count=1,
                max_angular_velocity=1000.0,
                max_linear_velocity=1000.0,
                max_depenetration_velocity=5.0,
                disable_gravity=False,
            ),
        ),
    )

    @staticmethod
    def end_effector_frame() -> FrameTransformerCfg:
        return FrameTransformerCfg(
            prim_path="{ENV_REGEX_NS}/Robot/panda_link0",
            debug_vis=False,
            target_frames=[
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/panda_hand",
                    name="end_effector",
                    offset=OffsetCfg(
                        pos=[0.0, 0.0, 0.1034],
                    ),
                ),
            ],
        )
    
    @staticmethod
    def place_position(name: str, device: torch.cuda.device) -> torch.Tensor:
        if name == AiffelatorScenes.Place.PencilCase.name:
            position = torch.tensor([AiffelatorScenes.Place.PencilCase.pos[0]], device=device)
        elif name == AiffelatorScenes.Place.Pen.name:
            position = torch.tensor([AiffelatorScenes.Place.Pen.pos[0]], device=device)
        else:
            raise ValueError(f"name({name}) is only [{AiffelatorScenes.Place.PencilCase.name}, {AiffelatorScenes.Place.Pen.name}]")
        return position
    
    @staticmethod
    def default_environment():
        return (
            AiffelatorScenes.ground_plane(), 
            AiffelatorScenes.light(),
            AiffelatorScenes.table(),
            #AiffelatorScenes.bookcase()
        )
    
    @staticmethod
    def camera_set():
        return (AiffelatorScenes.front_camera(),
                AiffelatorScenes.right_camera())
    
    @staticmethod
    def manipulator():
        return (AiffelatorScenes.franka_panda(),
                AiffelatorScenes.end_effector_frame())
    
    @staticmethod
    def pencil_case_set(type: str):
        if type == "desk":
            place = 0
        elif type == "bookcase":
            place = 1
        else:
            raise ValueError("type is only desk or bookcase")
        pos = AiffelatorScenes.Place.PencilCase.pos[place]
        return (AiffelatorScenes.pencil_case(),
                AiffelatorScenes.place_pencil_case(pos))
    
    @staticmethod
    def pen_set(type: str):
        if type == "desk":
            place = 0
        elif type == "bookcase":
            place = 1
        else:
            raise ValueError("type is only desk or bookcase")
        pos = AiffelatorScenes.Place.Pen.pos[place]
        return (AiffelatorScenes.pen(),
                AiffelatorScenes.place_pen(pos))