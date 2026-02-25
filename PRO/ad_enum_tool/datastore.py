class ShareInfo:
    def __init__(self, name):
        self.name = name
        self.readable = False
        self.writable = False
        self.listable = False

class EnumResult:
    def __init__(self, target):
        self.target = target
        self.host_up = False
        self.smb_open = False
        self.shares = []
