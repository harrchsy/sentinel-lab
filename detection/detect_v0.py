counts = {}
THRESHOLD = 3

def get_ip(line):
    line = line.strip()
    words = line.split()
    port = words.index("port")
    ip = words[port - 1]
    return ip

with open("auth.log") as f:
    for line in f:
        if "Connection closed by" in line and "authenticating" not in line:
            ip = get_ip(line)
            if ip in counts:
                counts[ip] = counts[ip] + 1
            else:
                counts[ip] = 1
            
for ip, n in counts.items():
    if n >= THRESHOLD:
        print("ALERT", ip, n)
    else:
        print("ok", ip, n ) 
