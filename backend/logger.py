import pandas as pd
import os

EXCEL_FILE = "post_call_analysis.xlsx"

def log_call(name, phone, booking_status, timestamp):
    file_path = "call_logs.xlsx"
    
    # Load existing data or create a new DataFrame
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=["Name", "Phone", "Booking Status", "Timestamp"])
    
    # New row of data
    new_data = {
        "Name": name,
        "Phone": phone,
        "Booking Status": booking_status,
        "Timestamp": timestamp
    }
    
    # Use pd.concat instead of append
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    
    # Save back to Excel
    df.to_excel(file_path, index=False)

