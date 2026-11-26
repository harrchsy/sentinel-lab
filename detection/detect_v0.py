counts = {}

with open("auth.log") as f:
    for line in f:
        if "Connection closed by" in line:
            line = line.strip()
            words = line.split()
            port = words.index("port")
            ip = words[port - 1]
            if ip in counts:
                counts[ip] = counts[ip] + 1
            else:
                counts[ip] = 1
            
for ip, n in counts.items():
    if n >= 3:
        print("ALERT", ip, n)
    else:
        print("ok", ip, n ) 