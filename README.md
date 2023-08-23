# IMG-Optical-Character-Recognition-Tool-Docker

IMG Optical Character Recognition Tool with Dockerfile Implemented.

## Download Repository

```
git clone https://github.com/toby0622/IMG-Optical-Character-Recognition-Tool-Docker
```

## Move To Program Folder

```
cd IMG-Optical-Character-Recognition-Tool-Docker
cd IMGOCR
```

## Docker Image Build

```
docker build -t imgocr .
```

## Run Docker Container (Initial Setup)

```
# if having multiple GPUs, specific graphics card can be selected
docker run --name imgocrflask --gpus all -p 9487:9487 imgocr
```

## Start Docker Container

```
docker start imgocrflask
```
