cmake_minimum_required(VERSION 2.8.12)
project(env)
set (CMAKE_CXX_STANDARD 14)

set(Python_ADDITIONAL_VERSIONS 3.7)
find_package(pybind11 REQUIRED)
find_package(Python 3.7 REQUIRED)

pybind11_add_module(env main.cpp card.hpp card.cpp game.cpp game.hpp dancing_link.cpp)
# add_executable(main main.cpp game.cpp game.hpp)
