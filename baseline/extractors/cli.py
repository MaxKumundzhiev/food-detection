import argparse
from pathlib import Path

from concrete import PyAVExtractor
from enums import ExtensionToSave


def main():
    parser = argparse.ArgumentParser(description="Extract 1 frame per second from video using PyAV.")
    parser.add_argument("source", type=Path, help="Path to folder containing videos to parse.")
    parser.add_argument("target", type=Path, help="Path to output folder to save frames")
    parser.add_argument("--ext", type=str, default="jpg", help="Extension to save images (default: .jpg)")

    args = parser.parse_args()
    extractor = PyAVExtractor()

    if not args.source.exists() or not args.source.is_dir():
        raise ValueError("Source folder not found or is not directory")
    
    if not args.target.exists() or not args.target.is_dir():
        raise ValueError("Target folder not found or is not directory")

    to_process = [f for f in args.source.iterdir() if f.is_file()]
    [extractor.extract(source=video, target=args.target, extension_to_save=ExtensionToSave(args.ext)) for video in to_process]


if __name__ == "__main__":
    main()

