import subprocess

def is_host_up(target):
    try:
        output = subprocess.run(
            ["ping", "-c", "1", "-W", "1", target],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return output.returncode == 0
    except:
        return False
