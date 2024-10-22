from omni.isaac.lab.utils import configclass
from omni.isaac.lab.scene import InteractiveSceneCfg

from .mdp import AiffelatorScenes

@configclass
class DeskSingleObjectSceneCfg(InteractiveSceneCfg):

    # default env
    plane, light, table = AiffelatorScenes.default_environment()
    # camera set
    # front_camera, right_camera = AiffelatorScenes.camera_set()
    # manipulator
    robot, ee_frame = AiffelatorScenes.manipulator()
    # pencil_case set
    pencil_case, place_pencil_case = AiffelatorScenes.pencil_case_set("desk")

@configclass
class DeskMultiObjectSceneCfg(InteractiveSceneCfg):

    # default env
    plane, light, table = AiffelatorScenes.default_environment()
    # camera set
    #front_camera, right_camera = AiffelatorScenes.camera_set()
    # manipulator
    robot, ee_frame = AiffelatorScenes.manipulator()
    # pencil_case set
    pencil_case, place_pencil_case = AiffelatorScenes.pencil_case_set("desk")
    # pen set
    pen, place_pen = AiffelatorScenes.pen_set("desk")
    
@configclass
class BookcaseMultiObjectSceneCfg(InteractiveSceneCfg):

    # default env
    plane, light, table = AiffelatorScenes.default_environment()
    # camera set
    front_camera, right_camera = AiffelatorScenes.camera_set()
    # manipulator
    robot, ee_frame = AiffelatorScenes.manipulator()
    # pencil_case set
    pencil_case, place_pencil_case = AiffelatorScenes.pencil_case_set("bookcase")
    # pen set
    pen, place_pen = AiffelatorScenes.pen_set("bookcase")