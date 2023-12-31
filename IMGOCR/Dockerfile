# main environment deploy
FROM nvidia/cuda:11.7.1-cudnn8-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install --fix-missing -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential libgl1 ffmpeg libsm6 libxext6 wget git

RUN wget http://security.ubuntu.com/ubuntu/pool/main/o/openssl/openssl_1.1.1f-1ubuntu2_amd64.deb
RUN dpkg -i openssl_1.1.1f-1ubuntu2_amd64.deb

# install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install flask
RUN pip install opencc==1.1.1
RUN pip install paddlepaddle-gpu==2.5.1
RUN pip install paddleocr

# make port 9487 available to the world outside this container
EXPOSE 9487

# run app.py when the container launches
CMD ["python3", "app.py"]