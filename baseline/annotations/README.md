# 🏷️ Annotation Workflow with Label Studio

For the annotations it was used [Label Studio](https://labelstud.io/) service.

## 🧠 Annotation Approach
1. Define classes by manually inspecting the source videos.
2. Annotate the extracted frames using the Label Studio UI.
3. Export annotations in YOLO format to `data/annotated/` for training.

## 🗂️ Label Classes
The following categories will be used when annotating objects:
- напиток
- соус
- жидкое
- салат
- мясо
- хлеб

## 🗂️ Output format (compiled with YOLO (with images))
```text
└── project-2-at-2025-07-02-07-58-190786e0
    ├── classes.txt
    ├── images
    │   ├── 208cd0d8-18_19_18.jpg
    │   ├── 47d72ed9-18_17_08.jpg
    │   ├── 47e625d4-18_16_56.jpg
    │   ├── 59faaf2b-18_19_16.jpg
    │   ├── 6a10bd94-18_18_33.jpg
    │   ├── 6ff973c0-18_19_04.jpg
    │   ├── 791c8c06-18_18_27.jpg
    │   ├── 80492958-18_18_45.jpg
    │   ├── 9234277f-18_19_17.jpg
    │   ├── ae042cf0-18_19_15.jpg
    │   ├── d0ff47c6-18_16_55.jpg
    │   ├── dfe77fd8-18_18_25.jpg
    │   ├── e53b6df7-18_18_41.jpg
    │   └── fe929997-18_17_29.jpg
    ├── labels
    │   ├── 208cd0d8-18_19_18.txt
    │   ├── 47d72ed9-18_17_08.txt
    │   ├── 47e625d4-18_16_56.txt
    │   ├── 59faaf2b-18_19_16.txt
    │   ├── 6a10bd94-18_18_33.txt
    │   ├── 6ff973c0-18_19_04.txt
    │   ├── 791c8c06-18_18_27.txt
    │   ├── 80492958-18_18_45.txt
    │   ├── 9234277f-18_19_17.txt
    │   ├── ae042cf0-18_19_15.txt
    │   ├── d0ff47c6-18_16_55.txt
    │   ├── dfe77fd8-18_18_25.txt
    │   ├── e53b6df7-18_18_41.txt
    │   └── fe929997-18_17_29.txt
    └── notes.json

where classes.txt
  жидкое
  мясо
  напиток
  салат
  соус
  хлеб
```
---

## 🚀 Run Label Studio (Locally)
```bash
$ label-studio
--> Once running, open http://localhost:8080 in your browser.
```

## 🐳 Run Label Studio in Docker
```bash
$ docker pull heartexlabs/label-studio:latest

$ docker run -it -p 8080:8080 \
  -v "$(pwd)/my_label_studio_data:/label-studio/data" \
  heartexlabs/label-studio:latest

--> Once running, open http://localhost:8080 in your browser.
--> This mounts local data to Label Studio’s internal storage so your work is persisted.
```



## ✍️ Labeling Process
<img width="1680" alt="Screenshot 2025-07-01 at 19 14 39" src="https://github.com/user-attachments/assets/afdd0213-0e97-435a-8fe8-1f3ba941de80" />
