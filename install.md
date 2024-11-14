# Installation of urdformer

> ***Note**: We provide a more detailed installation process based on the official, and restrictions are imposed on the versions of some libraries.*

- Create an new python3.9 environment
```bash
conda create -n urdformer python=3.9
conda activate urdformer
```

- Install all the required packages:
```bash
pip install -r requirements.txt
```

- Install pytorch and cuda(pytorch2.1.2+cuda12.1). 
```bash
pip uninstall torch torchvision -y 
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia -y
```

- Download all the checkpoints

[Option 1] You can either use the download script (this may take about 10 mins):
```bash
python download.py
```
[Option 2] or steps as below:
[Download link](https://drive.google.com/drive/folders/1FPlE1ui2jqjOcaflBZ-9K11YBV_1mD_f?usp=sharing)
First create two folders to save pretrained models:
```bash
mkdir checkpoints
mkdir backbones
```

(a) Download URDFormer checkpoints for both global scenes and parts (`global.pth`, `part.pth`), and place them under `checkpoints`

(b) Download backbone checkpoint (`mae_pretrain_hoi_vit_small.pth`) and place it under `backbones`

(c) Download Finetuned GroudingDINO models (`kitchen_souped.pth` and `object_souped.pth`) with modelsoup method for object-level and scene-level, and place them
under `grounding_dino`

After this step, your folder will look like:
```bash
urdformer/
├── backbones/
│   ├── mae_pretrain_hoi_vit_small.pth
├── checkpoints/
│   ├── global.pth
│   └── part.pth
├── grounding_dino/
│   ├── kitchen_souped.pth
│   └── object_souped.pth
...
```
- Install packages required for running GroundingDINO
```bash
pip install -U openmim
mim install mmengine
mim install "mmcv==2.1.0"  

cd grounding_dino
pip install -v -e .
cd ..
```

- Other setting
  
1. reinstall numpy
   
```
pip install numpy==1.26.4 --force-reinstall
```

2. You may encounter the following problems:

```
.../libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by ...)
```

> &emsp; Establish symbolic link to solve this problem

```
ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 {anaconda3_path}/envs/urdformer/lib/python3.9/site-packages/torch/lib/../../../../libstdc++.so.6
```

change {anaconda3_path} to you anaconda3 install path