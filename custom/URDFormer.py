from ..get_bbox import evaluate as evaluate_bbox
from ..get_texture import get_texture
from ..demo import evaluate as evaluate_demo
import argparse
from yacs.config import CfgNode as CN

class URDFormer:
    
    def __init__(self, cfgs):
        
        self.cfgs = cfgs
        
    def generate_urdf(self):
        
        # Get bounding boxes of parts and ojects
        evaluate_bbox(self.args)
        
        # Get texture about parts
        get_texture(self.cfgs)
        
        # Get urdf model prediction
        evaluate_demo(self.args, with_texture=self.args.texture, headless=self.args.headless)
        
if __name__=="__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-scene_type', '--scene_type', default='cabinet', type=str)
    parser.add_argument('-image_path', '--image_path', default='images', type=str)
    parser.add_argument('--texture', action='store_true', help='adding texture')
    parser.add_argument('--headless', action='store_true', help='option to run in headless mode')
    parser.add_argument('--random', '--random', action='store_true', help='use random meshes from partnet?')
    args = parser.parse_args()
    
    # cfg = CN.load_cfg('urdformer.yaml')
    urdfomrer = URDFormer(args)
    urdfomrer.generate_urdf(args)