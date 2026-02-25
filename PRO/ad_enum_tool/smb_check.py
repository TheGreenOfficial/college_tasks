import socket

def is_smb_open(target):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, 445))
        s.close()
        return True
    except:
        return False
