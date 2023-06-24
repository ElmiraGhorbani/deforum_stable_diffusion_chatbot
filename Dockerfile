FROM python:3.9-slim

USER root:root

ENV PYTHONUNBUFFERED TRUE

RUN apt-get update && apt-get upgrade --yes

RUN apt install -y wget \
    git \
    python-dev \
    pkg-config \
    vim \
    curl \
    build-essential

RUN pip install --upgrade --force-reinstall pip
RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY scripts scripts
COPY run.sh .
RUN chmod +x run.sh

SHELL ["/bin/bash", "-c", "source /root/.bashrc"]
CMD ["./run.sh"]
