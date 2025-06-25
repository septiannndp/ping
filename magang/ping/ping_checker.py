import subprocess
from datetime import datetime

def ping(ip: str) -> bool:
    """Return true if and only if ip can be pinged.
    
    >>> ping("1.1.1.1")
    True
    >>> ping("10.0.56.78")
    False
    """
    try:
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def check_ip() -> dict:
    """Check and return ping results as a dictionary."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    daftar_ip = [
        '192.168.45.12', '8.8.8.8', '10.0.56.78', '172.16.34.201',
        '1.1.1.1', '100.64.23.5', '45.33.32.156', '208.67.222.222',
        '8.26.4.199', '9.9.9.9'
    ]

    hasil = []
    for ip in daftar_ip:
        status = "UP" if ping(ip) else "DOWN"
        print(f"Sedang ping IP: {ip}, status: {status}")
        hasil.append({"ip": ip, "status": status})

    return {"timestamp": timestamp, "hasil": hasil}