cmake_minimum_required(VERSION 3.10)
project(MyProject LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

# Create an executable from solution.cpp
add_executable(solution solution.cpp)
