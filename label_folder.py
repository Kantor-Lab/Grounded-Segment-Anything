# Run grounded_sam_demo for entire folder, take folder path as input

import os
import argparse
import grounded_sam_demo

if __name__ == "__main__":

    parser = argparse.ArgumentParser("Grounded-Segment-Anything Demo", add_help=True)
    parser.add_argument("--config", type=str, required=True, help="path to config file")
    parser.add_argument(
        "--grounded_checkpoint", type=str, required=True, help="path to checkpoint file"
    )
    parser.add_argument(
        "--sam_checkpoint", type=str, required=True, help="path to checkpoint file"
    )
    parser.add_argument("--text_prompt", type=str, required=True, help="text prompt")
    parser.add_argument(
        "--input_dir", "-o", type=str, default="images", required=True, help="input directory"
    )

    parser.add_argument("--box_threshold", type=float, default=0.3, help="box threshold")
    parser.add_argument("--text_threshold", type=float, default=0.25, help="text threshold")

    parser.add_argument("--device", type=str, default="cpu", help="running on cpu only!, default=False")
    args = parser.parse_args()

    print("Input directory: ", args.input_dir)
    output_dir = os.path.join(os.path.dirname(args.input_dir), 'outputs')
    print("Output directory: ", output_dir)
    for file in os.listdir(args.input_dir):
        # Skip if file exists in output directory
        if os.path.exists(os.path.join(output_dir, file)):
            print("Skipping file: ", file)
            continue
        if file.endswith(".png"):
            input_img = os.path.join(args.input_dir, file)
            print("Input image: ", input_img)
            grounded_sam_demo.main(['--config', args.config, '--grounded_checkpoint', args.grounded_checkpoint, '--sam_checkpoint', args.sam_checkpoint, '--input_image', input_img, '--text_prompt', args.text_prompt, '--box_threshold', str(args.box_threshold), '--text_threshold', str(args.text_threshold), '--device', args.device])
        else:
            continue