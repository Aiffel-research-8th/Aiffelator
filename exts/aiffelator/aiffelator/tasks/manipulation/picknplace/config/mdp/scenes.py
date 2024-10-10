from omni.isaac.lab.utils import configclass
from omni.isaac.lab.scene import InteractiveSceneCfg
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.managers import SceneEntityCfg

class AiffelatorScenes:
    
    class SimpleDesk:
        class SingleObject:
            usd_path = "../env/simple_desk_1prim.usd"
            prim_path = "/World"
        class MultiObject:
            usd_path = "../env/simple_desk_2prim.usd"
            prim_path = "/World"
        
    class SimpleBookcase:
        class SingleObject:
            usd_path = "../env/simple_bookcase_1prim.usd"
            prim_path = "/World"
        class MultiObject:
            usd_path = "../env/simple_bookcase_2prim.usd"
            prim_path = "/World"

    class Franka:
        usd_path = "../env/franka.usd"
        prim_path = "/World/robot"
    
    class Place:
        class Pen:
            usd_path = "../env/place_pen.usd"
            prim_path = "/World/place_pen"
        class PencilCase:
            usd_path = "../env/place_pencil_case.usd"
            prim_path = "/World/place_pencil_case"
    
    class Bookcase:
        usd_path = "../env/bookcase.usd"
        prim_path = "/World/bookcase"