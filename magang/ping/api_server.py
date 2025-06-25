from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import datetime
import csv
import os

app = FastAPI()

class PingResult(BaseModel):
    """
    Represents the ping result for a single IP address.

    Attributes:
        ip (str): The IP address being pinged.
        status (str): The result status of the ping (e.g., "UP", "DOWN").
    """
    ip: str
    status: str

class PingData(BaseModel):
    """
    Represents a full set of ping results sent from the client.

    Attributes:
        timestamp (str): The date and time when the ping was performed.
        hasil (List[PingResult]): A list of ping results.
    """
    timestamp: str
    hasil: List[PingResult]

CSV_FILE = "ping_log.csv"

# Create file with header if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "ip", "status"])

@app.post("/ping-report")
async def receive_ping_report(data: PingData):
    """
    Receive a list of ping results and save them to a CSV file.

    Parameters:
        data (PingData): The ping results including timestamp and status of each IP.

    Returns:
        dict: A confirmation message.
    """
    print(f"\n📥 Received data at {datetime.datetime.now()}:")
    
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        for item in data.hasil:
            print(f"  IP: {item.ip} | Status: {item.status}")
            writer.writerow([data.timestamp, item.ip, item.status])
    
    return {"message": "Data received and saved to CSV"}
