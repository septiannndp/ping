import subprocess
import time
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

def check_ip() -> str:
    """Check and print whether IP in daftar_ip can be pinged or not."""
    print(f"\nMenjalankan pengecekan ping pada {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    daftar_ip = [
        '192.168.45.12', '8.8.8.8', '10.0.56.78', '172.16.34.201',
        '1.1.1.1', '100.64.23.5', '45.33.32.156', '208.67.222.222',
        '8.26.4.199', '9.9.9.9'
    ]

    for ip in daftar_ip:
        if ping(ip):
            print(f"Sedang ping IP: {ip}, status: UP")
        else:
            print(f"Sedang ping IP: {ip}, status: DOWN")

# Set the daily target time for the ping check (24-hour format: "HH:MM")
waktu_pengecekan = "08:41"

print("Program dimulai. Menunggu waktu pengecekan...")

while True:
    now = datetime.now()
    jam = int(waktu_pengecekan[:2])
    menit = int(waktu_pengecekan[3:5])

    if now.hour == jam and now.minute == menit:
        check_ip()
        print("Pengecekan selesai. Program tidur selama 23 jam 58 menit...\n")
        time.sleep(23 * 3600 + 58 * 60)  # Sleep for 23 hours and 58 minutes (86300 seconds)
    else:
        time.sleep(10)  # Check every 10 seconds until the scheduled time