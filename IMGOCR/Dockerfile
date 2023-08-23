# Use an official Python runtime as a parent image
FROM nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install --fix-missing -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential libgl1 ffmpeg libsm6 libxext6 wget git

RUN wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.19_amd64.deb
RUN dpkg -i libssl1.1_1.1.1f-1ubuntu2.19_amd64.deb

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install flask
RUN pip install opencc
RUN pip install paddlepaddle-gpu==2.5.1
RUN pip install paddleocr

# Make port 80 available to the world outside this container
EXPOSE 9487

# Run app.py when the container launches
CMD ["python3", "app.py"]