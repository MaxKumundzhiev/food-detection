# Report
The very first suggestion is to read the `Репорт.pdf` file. aftermath, u might want get familiar with the rest of the documentation;


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
For more details navigate to `yolo_training_on_custom_datataset.ipynb` notebook;



## Inference results
<img width="534" alt="Screenshot 2025-07-04 at 00 27 21" src="https://github.com/user-attachments/assets/a532ab29-2055-48f3-88bc-1e9cb355584a" />

<img width="536" alt="Screenshot 2025-07-04 at 00 27 35" src="https://github.com/user-attachments/assets/61c46901-af4e-4a27-828c-171385d2248f" />

<img width="539" alt="Screenshot 2025-07-04 at 00 27 58" src="https://github.com/user-attachments/assets/c658cf90-c199-41b9-b245-c7280d9c0308" />



