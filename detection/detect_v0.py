counts = {}
auth_counts = {}
THRESHOLD = 3
ALLOWLIST = ["192.168.64.1", "127.0.0.1"]

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
            if ip in ALLOWLIST:
                continue
            if ip in counts:
                counts[ip] = counts[ip] + 1
            else:
                counts[ip] = 1

        if "Connection closed by" in line and "authenticating" in line:
            ip = get_ip(line)
            if ip in ALLOWLIST:
                continue
            if ip in auth_counts:
                auth_counts[ip] = auth_counts[ip] + 1
            else:
                auth_counts[ip] = 1

for ip, n in counts.items():
    if n >= THRESHOLD:
        print("ALERT", "recon", ip, n)
    else:
        print("ok", "recon", ip, n ) 

for ip, n in auth_counts.items():
    if n >= THRESHOLD:
        print("ALERT", "auth", ip, n)
    else:
        print("ok", "auth", ip, n ) 



