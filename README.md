# IMG-Optical-Character-Recognition-Tool-Docker

IMG Optical Character Recognition Tool with Dockerfile Implemented.

## Docker Image Build

```
docker build -t imgocr .
```

## Run Docker Container

```
docker run --name imgocrflask --gpus all -p 9487:9487 imgocr
```
