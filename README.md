# Formi_assignment

Architecture Diagram
       The system consists of three main components:
       1. Frontend (React.js): A user interface where customers can book tables by filling out a form.
       2. Backend (FastAPI): Handles API requests from the frontend and saves booking data into an Excel sheet.
       3. Excel Sheet: Acts as a simple database to store booking records.

Flow:
User submits booking form → Frontend sends POST request → Backend processes request and writes to Excel → Booking saved confirmation sent back to frontend.

API Documentation
     POST /book-table
     1. Description: Saves the booking data received from the frontend form into an Excel sheet.
     2. Request Body: JSON object with the following fields:
              name (string) — Customer's name
              phone (string) — Customer's phone number
              guests (integer) — Number of guests
              location (string) — Desired restaurant location
              time (string) — Booking time
              Response: JSON with a success message or error details.
