import argparse
from pathlib import Path

from concrete import PyAVExtractor

def main():
    parser = argparse.ArgumentParser(description="Extract 1 frame per second from video using PyAV.")
    parser.add_argument("source", type=Path, help="Path to folder containing videos to parse.")
    parser.add_argument("target", type=Path, help="Path to output folder to save frames")
    parser.add_argument("--ext", type=str, default=".jpg", help="Extension to save images (default: .jpg)")

    args = parser.parse_args()
    extractor = PyAVExtractor()

    # check source exists
    # check target exists
    # for video in source:
        # call video processing
    extractor.extract(source=args.source, target=args.target, extension_to_save=args.ext)



if __name__ == "__main__":
    main()

