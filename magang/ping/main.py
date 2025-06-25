import time
import requests
from datetime import datetime
from ping_checker import check_ip

# Target check time (24-hour format)
waktu_pengecekan = "10:06"

# API endpoint (replace with your real one)
API_ENDPOINT = "http://127.0.0.1:8000/ping-report"

# Optional: Bearer Token (if your API requires it)
# API_HEADERS = {
#     "Authorization": "Bearer YOUR_TOKEN_HERE",
#     "Content-Type": "application/json"
# }

# If no token required:
API_HEADERS = {
    "Content-Type": "application/json"
}

print("Program started. Waiting for scheduled ping...")

while True:
    now = datetime.now()
    jam = int(waktu_pengecekan[:2])
    menit = int(waktu_pengecekan[3:5])

    if now.hour == jam and now.minute == menit:
        data = check_ip()

        try:
            response = requests.post(API_ENDPOINT, json=data, headers=API_HEADERS)
            print(f"Data sent to API. Response code: {response.status_code}")
            print("Response body:", response.text)
        except Exception as e:
            print(f"Failed to send data to API: {e}")

        print("Sleeping for 23 hours and 58 minutes...\n")
        time.sleep(23 * 3600 + 58 * 60)
    else:
        time.sleep(10)