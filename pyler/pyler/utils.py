import os
import subprocess

import sys
import time


def user_input(*args, **kwargs):
    return input(*args, **kwargs)


def default_open(something_to_open):
    """
    Open given file with default user program.
    From https://github.com/carlos-jenkins/nested/blob/
        c38bf1d17bdf52c8f4051e044069327532c0ef88/src/lib/nested/utils.py#L68
    """
    if sys.platform.startswith('linux'):
        subprocess.Popen(['xdg-open', something_to_open])

    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', something_to_open])

    elif sys.platform.startswith('win'):
        os.startfile(something_to_open)

    time.sleep(0.3)


def convert_time(timing):
    """
    Convert a timing in s to ms, us or ns, depending on value
    """
    if timing < 1e-6:
        return f"{timing * 1e9:.4f} ns"
    elif timing < 1e-3:
        return f"{timing * 1e6:.4f} us"
    elif timing < 1:
        return f"{timing * 1e3:.4f} ms"
    else:
        return f"{timing:.4f} s"
