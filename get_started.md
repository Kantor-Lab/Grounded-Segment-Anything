## Setup
Follow the setup intsructions in the README

## Grounded SAM Demo
You can test this model with your image and text prompt. It automatically saves your segmented image, generated bounding boxes, mask image in a directory called `outputs` at the same level as the parent directory of your input image. 
```
export CUDA_VISIBLE_DEVICES=0
python grounded_sam_demo.py \
  --config GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py \
  --grounded_checkpoint groundingdino_swint_ogc.pth \
  --sam_checkpoint sam_vit_h_4b8939.pth \
  --input_image /your/img/path \
  --box_threshold 0.3 \
  --text_threshold 0.25 \
  --text_prompt "your prompt" \
  --device "cuda"
```

## Generate masks for a folder of images
This script wraps around the above demo script to label all images in a folder. Be sure to match the image extensions for your use case. It automatically saves your segmented image, generated bounding boxes, mask image in a directory called `outputs` at the same level as the input directory. 
```export CUDA_VISIBLE_DEVICES=0                                                
python label_folder.py \
  --config GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py \
  --grounded_checkpoint groundingdino_swint_ogc.pth \
  --sam_checkpoint sam_vit_h_4b8939.pth \
  --input_dir ./path/to/folder \
  --box_threshold 0.3 \
  --text_threshold 0.25 \
  --text_prompt "your prompt" \
  --device "cuda"
```