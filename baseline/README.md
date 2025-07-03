# Intro
The baseline represents a sequence of steps to address the `food detection` problem using a custom dataset.
For simplicity and reproducibility, the baseline focuses on demonstrating a minimal working solution, which can be further extended and optimized later. 

## Prerequisites
- create a dedicated virtual environment and install nessessary libraries
```bash
$ pip install -r requirements.txt
```
- create a folder for storing data on various stages (source videos, extracted frames, annotated frames)
```bash
$ mkdir data && mkdir data/source && mkdir data/frames && mkdir data/annotated

Note:
    source - stands for source videos;
    frames - stands for retireved frames from source videos;
    annotated - stands for annotated frames;  
```

## Pipeline Step 1: retrieve frames from videos
It was introduced a CLI which stands for retriving frames from source videos;
For more details navigate to `extractors` folder;
```bash
--> extract frames
$ python extractors/cli.py <VideosFolderPath>  <ExtractedFolderPath>

e.g.:
$ python extractors/cli.py data/source  data/frames
```

## Pipeline  Step 2: annotate retrieved frames
It was used open sourced annotation tool `label studio`, to perform frames labelling;
For more details navigate to `annotations` folder;
```bash
--> start label studio locally
$ label-studio
```

## Pipeline Step 3: model training and testing
It was used Google Colab to perform model training and testing;
For mode details open `yolo_training_on_custom_datataset.ipynb` notebook;
