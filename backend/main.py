from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import pandas as pd
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:3000"] to be strict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Booking(BaseModel):
    name: str
    phone: str
    guests: int
    location: str
    time: str

@app.post("/book-table")
def book_table(booking: Booking):
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../post_call_analysis.xlsx"))

    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Phone", "Booking Status", "Timestamp"])

    new_row = {
        "Name": booking.name,
        "Phone": booking.phone,
        "Booking Status": f"{booking.guests} seats at {booking.location} at {booking.time}",
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(file_path, index=False)

    return {"message": "Booking saved successfully"}
