# Introduction
Extractors module is meant for CLI (command line interface) to extract frames from video.
The module consists of concrete implementations of potentially various extracting interfaces.

```text
As of now there is `AV extractor` which is pythonic binding for the FFmpeg.
```

# Usage
```bash
$ python extractors/cli.py --help
usage: cli.py [-h] [--ext EXT] source target

Extract 1 frame per second from video using PyAV.

positional arguments:
  source      Path to folder containing videos to parse.
  target      Path to output folder to save frames

options:
  -h, --help  show this help message and exit
  --ext EXT   Extension to save images (default: .jpg)
```

# Example output
```text
2025-07-01 18:14:16.482 | INFO     | concrete:extract:24 - start processing /Users/macbook/git/food-detection/food-detection/baseline/data/source/3_1.MOV
2025-07-01 18:14:16.680 | SUCCESS  | concrete:extract:52 - saved /Users/macbook/git/food-detection/food-detection/baseline/data/frames/18_14_16.jpg
2025-07-01 18:14:17.138 | SUCCESS  | concrete:extract:52 - saved /Users/macbook/git/food-detection/food-detection/baseline/data/frames/18_14_17.jpg
2025-07-01 18:14:17.576 | SUCCESS  | concrete:extract:52 - saved /Users/macbook/git/food-detection/food-detection/baseline/data/frames/18_14_17.jpg
2025-07-01 18:14:18.015 | SUCCESS  | concrete:extract:52 - saved /Users/macbook/git/food-detection/food-detection/baseline/data/frames/18_14_17.jpg
2025-07-01 18:14:18.446 | SUCCESS  | concrete:extract:52 - saved /Users/macbook/git/food-detection/food-detection/baseline/data/frames/18_14_18.jpg
2025-07-01 18:14:18.881 | SUCCESS  | concrete:extract:52 - saved /Users/macbook/git/food-detection/food-detection/baseline/data/frames/18_14_18.jpg
2025-07-01 18:14:19.315 | SUCCESS  | concrete:extract:52 - saved /Users/macbook/git/food-detection/food-detection/baseline/data/frames/18_14_19.jpg
```