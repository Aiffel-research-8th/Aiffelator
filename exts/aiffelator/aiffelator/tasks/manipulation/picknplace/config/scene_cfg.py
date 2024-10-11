from omni.isaac.lab.utils import configclass
from omni.isaac.lab.scene import InteractiveSceneCfg
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.managers import SceneEntityCfg

from . import mdp

@configclass
class DeskSingleObjectSceneCfg(InteractiveSceneCfg):

    # load usd
    desk = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.SimpleDesk.SingleObject.usd_path)
    desk.func(mdp.AiffelatorScenes.SimpleDesk.SingleObject.prim_path, desk)

    # franka
    robot = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Franka.usd_path)
    robot.func(mdp.AiffelatorScenes.Franka.prim_path, 
                    robot, 
                    translation=(0.0, 0.0, 1.0),
                    orientation=(0, 0, 0, 0))

    # pencil_case place
    place_pencil_case = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Place.PencilCase.usd_path)
    place_pencil_case.func(mdp.AiffelatorScenes.Place.PencilCase.prim_path, 
                               place_pencil_case, 
                               translation=(-0.4, 0.3, 1.005), 
                               orientation=(0, 0, 0, 0))

@configclass
class DeskMultiObjectSceneCfg(InteractiveSceneCfg):

    # load usd
    desk = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.SimpleDesk.MultiObject.usd_path)
    desk.func(mdp.AiffelatorScenes.SimpleDesk.MultiObject.prim_path, desk)

    # franka
    robot = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Franka.usd_path)
    robot.func(mdp.AiffelatorScenes.Franka.prim_path, 
                    robot, 
                    translation=(0.0, 0.0, 1.0),
                    orientation=(0, 0, 0, 0))

    # pencil_case place
    place_pen = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Place.Pen.usd_path)
    place_pen.func(mdp.AiffelatorScenes.Place.Pen.prim_path, 
                               place_pen,
                               translation=(-0.225, 0.475, 1.005), 
                               orientation=(0, 0, 0, 0))

    # pencil_case place
    place_pencil_case = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Place.PencilCase.usd_path)
    place_pencil_case.func(mdp.AiffelatorScenes.Place.PencilCase.prim_path, 
                               place_pencil_case, 
                               translation=(-0.525, 0.175, 1.005),
                               orientation=(0, 0, 0, 0))
    
@configclass
class BookcaseSingleObjectSceneCfg(InteractiveSceneCfg):

    # load usd
    desk = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.SimpleBookcase.SingleObject.usd_path)
    desk.func(mdp.AiffelatorScenes.SimpleBookcase.SingleObject.prim_path, desk)

    # bookcase
    bookcase = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Bookcase.usd_path)
    bookcase.func(mdp.AiffelatorScenes.Bookcase.prim_path, 
                    bookcase,
                    translation=(-0.65, 0.35, 1.0),
                    orientation=(0.70711, 0, 0, 0.70711))

    # franka
    robot = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Franka.usd_path)
    robot.func(mdp.AiffelatorScenes.Franka.prim_path, 
                    robot, 
                    translation=(0.0, 0.0, 1.0),
                    orientation=(0, 0, 0, 0))

    # pencil_case place
    place_pencil_case = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Place.PencilCase.usd_path)
    place_pencil_case.func(mdp.AiffelatorScenes.Place.PencilCase.prim_path, 
                               place_pencil_case, 
                               translation=(-0.60076, 0.19904, 1.126),
                               orientation=(0, 0, 0, 0))
    
@configclass
class BookcaseMultiObjectSceneCfg(InteractiveSceneCfg):

    # load usd
    desk = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.SimpleBookcase.MultiObject.usd_path)
    desk.func(mdp.AiffelatorScenes.SimpleBookcase.MultiObject.prim_path, desk)

    # bookcase
    bookcase = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Bookcase.usd_path)
    bookcase.func(mdp.AiffelatorScenes.Bookcase.prim_path, 
                    bookcase,
                    translation=(-0.65, 0.35, 1.0),
                    orientation=(0.70711, 0, 0, 0.70711))

    # franka
    robot = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Franka.usd_path)
    robot.func(mdp.AiffelatorScenes.Franka.prim_path, 
                    robot, 
                    translation=(0.0, 0.0, 1.0),
                    orientation=(0, 0, 0, 0))

    # pencil_case place
    place_pen = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Place.Pen.usd_path)
    place_pen.func(mdp.AiffelatorScenes.Place.Pen.prim_path, 
                               place_pen,
                               translation=(-0.60076, 0.19904, 1.466), 
                               orientation=(0, 0, 0, 0))

    # pencil_case place
    place_pencil_case = sim_utils.UsdFileCfg(usd_path=mdp.AiffelatorScenes.Place.PencilCase.usd_path)
    place_pencil_case.func(mdp.AiffelatorScenes.Place.PencilCase.prim_path, 
                               place_pencil_case, 
                               translation=(-0.60076, 0.19904, 1.126),
                               orientation=(0, 0, 0, 0))