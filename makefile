all: spammodule.c
	gcc -shared -o sample.so spammodule.c -I/opt/homebrew/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Versions/3.9/include/python3.9/

mult: mult.cpp mult.hpp
	g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC mult.cpp -o libcppmult.so
