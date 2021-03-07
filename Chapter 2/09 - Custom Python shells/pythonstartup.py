# python startup file

import atexit
import os

try:
    import readline
except ImportError:
    print("Completion unavailable: readline module not available")
else:
    import rlcompleter

    # tab completion
    readline.parse_and_bind("tab: complete")

    # Path to history file in user's home directory.
    # Can use your own path.
    history_file = os.path.join(os.environ["HOME"], ".python_shell_history")
    try:
        readline.read_history_file(history_file)
    except IOError:
        pass

    atexit.register(readline.write_history_file, history_file)
    del os, history_file, readline, rlcompleter
