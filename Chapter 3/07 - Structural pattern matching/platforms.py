import sys

match sys.platform:
    case "windows":
        print("Running on Windows")
    case "darwin" :
        print("Running on macOS")
    case "linux":
        print("Running on Linux")
    case _:
        raise NotImplementedError(f"{sys.platform} not supported!")
