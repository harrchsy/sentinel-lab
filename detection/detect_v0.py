counts = {}
THRESHOLD = 3

with open("auth.log") as f:
    for line in f:
        if "Connection closed by" in line and "authenticating" not in line:
            line = line.strip()
            words = line.split()
            port = words.index("port")
            ip = words[port - 1]
            if ip in counts:
                counts[ip] = counts[ip] + 1
            else:
                counts[ip] = 1
            
for ip, n in counts.items():
    if n >= THRESHOLD:
        print("ALERT", ip, n)
    else:
        print("ok", ip, n ) 