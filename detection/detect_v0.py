with open("auth.log") as f:
    for line in f:
        if "Connection closed by" in line:
            line = line.strip()
            words = line.split()
            port = words.index("port")
            ip = words[port - 1]
            print(ip)