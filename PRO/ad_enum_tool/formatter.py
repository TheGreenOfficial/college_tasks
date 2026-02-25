def print_results(result):
    print("\nTarget:", result.target)
    print("Host Reachable:", result.host_up)
    print("SMB Available:", result.smb_open)

    if not result.shares:
        print("\nNo accessible shares found")
        return

    print("\nShares:")
    for s in result.shares:
        perms = []
        if s.readable:
            perms.append("READ")
        if s.writable:
            perms.append("WRITE")
        if s.listable:
            perms.append("LIST")

        if not perms:
            perms.append("NO ACCESS")

        print(f" - {s.name}: {', '.join(perms)}")
