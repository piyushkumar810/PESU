# -----------------------------------------about sys 
'''-> the sys module in python provides access to system-specifix information and functions.
'''
import sys
print("sys imported, version: ", sys.version)  # it will show the version 
print("sys platform : ", sys.platform)         #
print() 

# ----------------------------------command line argument(sys.argv)
# this will show you current argv
print("current sys arg ", sys.argv)   #.argv-> it will show you the path name and the argument which you passed
# simulate running a script with argument 
saved_argv=sys.argv.copy()
sys.argv=["demo.py","one","two","three"]
print("simulated sys.argv : ",sys.argv)
# restore
sys.argv=saved_argv
print()

# ---------------------------(sys.path)
print(f"showing only first 8 entries only {sys.path[:8]}")

# -----------------------------(sys.exit) -> want to kill the program
print()
try:
    print("about to call sys.exit(0)")
    sys.exit(0)
except SystemExit as e:
    print("caught system exit with code : ", e.code)

print("kernal still alive - exit was caught safely")
print()

# ------------------------------ file i/o
# sys.stdin -> 
# sys.stout ->
import io
print()
print("pleasr enter your name ")
user_input=sys.stdin.readline().rstrip("\n")
sys.stdout.write("hello ")
sys.stdout.write(user_input +"\n")
print()

# ------------------- if you want to see error stream (stderr)
# ------------------- what ever module you loaded (sys.module)
# ------------------- get size of (sys.getsizeof(obj))
print("some loaded module (first 10):")
print(list(sys.modules.keys())[:10])
obj=list(range(100))
print("\n size of list(range(100)): ",sys.getsizeof(obj),"bytes")