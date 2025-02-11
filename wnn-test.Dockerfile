# Build with one of the following:
# docker build -t my-images/wnn-test -f wnn-test.Dockerfile .
# podman build --format docker -t my-images/wnn-test -f wnn-test.Dockerfile .

FROM ubuntu
MAINTAINER Andrew Nguyen 

RUN apt update && apt install -y \
        git \
        gcc \
        cmake \
        ninja-build \ 
        python3 \ 
        python3-pip \ 
        python3-venv \
        vim

# Uses default user (root) and sets the default workdir as /root
ENV USER root
ENV HOME /root

WORKDIR ${HOME}

# Create and activate a venv
RUN python3 -m venv ${HOME}/venv
ENV PATH="${HOME}/venv/bin:$PATH"

# install pybind
RUN pip install "pybind11[global]" pandas numpy scipy tqdm requests unlzw3

# build wzero library
RUN git clone https://github.com/A-H-Nguyen/wzero.git ${HOME}/wzero
RUN cd ${HOME}/wzero/models/wrappers/ && cmake -G Ninja . && ninja
