import platform, sys

def main(args):
    print("Python:", sys.version)
    print("Platform:", platform.system())
    print("Architecture:", platform.architecture()[0])
    print("Path:", sys.executable)
