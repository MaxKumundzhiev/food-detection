# Extractors CLI

The **Extractors CLI** is a command-line tool for extracting frames from video files.  
It is designed to be modular and extensible, supporting multiple backend implementations.

### ✅ Currently supported extractors:
- **AV Extractor**
```text
Extracts 1 frame per second from the input video and save to target directory.
Implemented as pythonic binding around FFmpeg.
```
---

## 🧪 Usage
```bash
python cli.py --help
usage: cli.py [-h] [--ext EXT] source target

Extract 1 frame per second from videos using PyAV.

positional arguments:
  source        Path to the folder containing videos
  target        Path to the folder where extracted frames will be saved

options:
  -h, --help    Show this help message and exit
  --ext EXT     File extension for saved images (default: .jpg)
```

## 📦 Example usage
```text
$ python cli.py .../data/source .../data/frames

2025-07-01 18:14:16.482 | INFO     | concrete:extract:24 - Start processing /path/to/source/3_1.MOV
2025-07-01 18:14:16.680 | SUCCESS  | concrete:extract:52 - Saved /path/to/frames/18_14_16.jpg
2025-07-01 18:14:17.138 | SUCCESS  | concrete:extract:52 - Saved /path/to/frames/18_14_17.jpg
2025-07-01 18:14:18.446 | SUCCESS  | concrete:extract:52 - Saved /path/to/frames/18_14_18.jpg
...
```