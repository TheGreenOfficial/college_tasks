import sys
from network_check import is_host_up
from smb_check import is_smb_open
from smb_enum import enumerate_shares
from formatter import print_results
from datastore import EnumResult

def usage():
    print("Usage: python3 main.py <target-ip>")
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        usage()

    target = sys.argv[1]
    result = EnumResult(target)

    if not is_host_up(target):
        print("Host is not reachable")
        sys.exit(0)

    result.host_up = True

    if not is_smb_open(target):
        print("SMB service not available")
        print_results(result)
        sys.exit(0)

    result.smb_open = True
    enumerate_shares(target, result)
    print_results(result)

if __name__ == "__main__":
    main()
