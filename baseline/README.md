# Intro
The baseline represents a sequence of steps to formulate the `food detection` problem using a custom dataset.
For simplicity and reproducibility, the baseline focuses on demonstrating a minimal working solution, which can be further extended and optimized later. 

# Prerequisites
- create a dedicated virtual environment and install nessessary libraries
```bash
$ pip install -r requirements.txt
```
- create a parent data folder for child source | frames | annotated folder
```bash
$ mkdir data && mkdir data/source && mkdir data/frames && mkdir data/annotated

source - stands for source videos;
frames - stands for retireved frames from source videos;
annotated - stands for annotated frames;  
```

# Step 1: retrieve frames from videos
It was introduced a CLI which stands for retriving frames from source videos;
For more details navigate to `extractors` folder;
```bash
$ python extractors/cli.py <SourceFolderPath>  <TargetFolderPath>
```

# Step 2: annotate retrieved frames
It was used label studio open sourced annotation tool to perform frames labelling;
For more details navigate to `annotations` folder;
```bash
$ label-studio
```

# Step 3: model training and testing
It was used Google Colab to perform model training and testing;
For mode details open `yolo_training_on_custom_datataset.ipynb` notebook;
