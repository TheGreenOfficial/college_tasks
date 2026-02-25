import subprocess
from datastore import ShareInfo

def run_smbclient(target, command):
    try:
        p = subprocess.run(
            ["smbclient", "-N", f"//{target}/IPC$", "-c", command],
            capture_output=True,
            text=True,
            timeout=5
        )
        return p.stdout
    except:
        return ""

def list_shares(target):
    try:
        p = subprocess.run(
            ["smbclient", "-N", "-L", f"//{target}"],
            capture_output=True,
            text=True,
            timeout=5
        )
        shares = []
        for line in p.stdout.splitlines():
            if "Disk" in line:
                name = line.split()[0]
                shares.append(name)
        return shares
    except:
        return []

def check_share_access(target, share_name):
    info = ShareInfo(share_name)

    try:
        p = subprocess.run(
            ["smbclient", "-N", f"//{target}/{share_name}", "-c", "ls"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if p.returncode == 0:
            info.listable = True
            info.readable = True
    except:
        pass

    try:
        p = subprocess.run(
            ["smbclient", "-N", f"//{target}/{share_name}", "-c", "mkdir test_enum"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if p.returncode == 0:
            info.writable = True
            subprocess.run(
                ["smbclient", "-N", f"//{target}/{share_name}", "-c", "rmdir test_enum"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
    except:
        pass

    return info

def enumerate_shares(target, result):
    shares = list_shares(target)
    for share in shares:
        info = check_share_access(target, share)
        result.shares.append(info)
