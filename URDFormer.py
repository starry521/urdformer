from get_bbox import evaluate as evaluate_bbox
from get_texture import get_texture
from demo import evaluate as evaluate_demo
from yacs.config import CfgNode as CN

class URDFormer:
    
    def __init__(self, cfgs):
        
        self.cfgs = cfgs
        
    def generate_urdf(self):
        
        # Get bounding boxes of parts and ojects
        evaluate_bbox(self.cfgs)
        
        if self.cfgs.texture:
            # Get texture about parts
            get_texture(self.cfgs)
        
        # Get urdf model prediction
        evaluate_demo(self.cfgs, with_texture=self.cfgs.texture, headless=self.cfgs.headless)
        
if __name__=="__main__":
    
    with open('config/urdformer.yaml', "r") as file:
        cfgs = CN.load_cfg(file)
    urdformer = URDFormer(cfgs)
    urdformer.generate_urdf()