#!/usr/bin/env bash

# install cmake
sudo apt install cmake
sudo apt install python-dev python3-dev
sudo pip install pytest


PYBIND11_VER=2.2.4

wget https://github.com/pybind/pybind11/archive/v2.2.4.tar.gz
tar xvf v2.2.4.tar.gz

cd pybind11-$PYBIND11_VER

mkdir build
cd build
cmake ..
make check -j4
sudo make install
