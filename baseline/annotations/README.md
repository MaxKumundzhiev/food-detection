# Introduction
For annotations we gonna use the "Label Studio" service.

# Run "Label Studio" service locally
```bash
$ label-studio
-> navigate to localhost:8080
```


# Run "Label Studio" service locally in container
```bash
$ docker pull heartexlabs/label-studio:latest
$ docker run -it -p 8080:8080 \
  -v "$(pwd)/my_label_studio_data:/label-studio/data" \
  heartexlabs/label-studio:latest
```


# Approach
1. Define the list of classes based on manual inspection of the source videos.
2. Annotate retrieved frames.
3. Export in YOLO format for further model training (expected location `data/annotated/`)


# Classes to be used for labelling
- напиток
- соус
- жидкое
- салат
- мясо
- хлеб

# Labelling Process
<img width="1680" alt="Screenshot 2025-07-01 at 19 14 39" src="https://github.com/user-attachments/assets/afdd0213-0e97-435a-8fe8-1f3ba941de80" />
