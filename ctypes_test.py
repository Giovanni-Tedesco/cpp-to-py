# ctypes_test.py
import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path().absolute() / "libcppmult.so"
    c_lib = ctypes.CDLL('./clib/build/libcppfad.dylib')

    x, y = 6, 2.3
    answer = c_lib.cppmult(x, ctypes.c_float(y))
    print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")
