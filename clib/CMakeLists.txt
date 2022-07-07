cmake_minimum_required (VERSION 3.1)
project (helloworld)

set (CMAKE_CXX_FLAGS "--std=gnu++11 ${CMAKE_C_FLAGS}")
file (GLOB SOURCE_FILES "source/*.cpp")

set (CMAKE_INCLUDE_PATH ${CMAKE_INCLUDE_PATH} /usr/local/lib/boost_1_58_0/boost)
set (CMAKE_LIBRARY_PATH ${CMAKE_LIBRARY_PATH} /usr/local/lib/boost_1_58_0/stage/lib)

set (Boost_NO_BOOST_CMAKE ON)   
set (BOOST_NO_SYSTEM_PATHS ON)
set (BOOST_ROOT /usr/local/lib/boost_1_58_0)
set (BOOST_INCLUDEDIR /usr/local/lib/boost_1_58_0/boost)
set (BOOST_LIBRARYDIR /usr/local/lib/boost_1_58_0/stage/lib)

set (Boost_USE_STATIC_LIBS OFF)
set (Boost_USE_MULTITHREADED ON)
set (Boost_USE_STATIC_RUNTIME OFF)
find_package (Boost 1.58.0 )


add_executable (helloworld ./src/cppmath.cpp)

target_include_directories(helloworld PRIVATE include)
target_include_directories(helloworld PRIVATE src)
target_include_directories(helloworld PRIVATE /opt/homebrew/opt/python@3.9/Frameworks/Python.framework/Versions/3.9/include/python3.9)

include_directories (${Boost_INCLUDE_DIRS})
target_link_libraries(helloworld ${Boost_LIBRARIES})


include_directories ("source")