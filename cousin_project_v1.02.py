import tkinter as tk
from tkinter import filedialog
import gspread
import json

# Initialize Google Sheets API
gc = gspread.service_account(filename='client_secret.json')

# Create the root window
root = tk.Tk()
root.title("Google Sheets JSON Converter")

# Function to load JSON file to Google Sheets
def load_json_to_sheets():
    # Open file dialog to select JSON file
    json_file = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    
    if json_file:
        # Read JSON data
        with open(json_file) as f:
            json_data = json.load(f)
        
        # Open Google Sheets document
        sh = gc.open('Test')
        worksheet = sh.sheet1

        # Clear existing data
        worksheet.clear()

        # Append data to Google Sheets
        worksheet.append_rows(json_data)
        
        # Show success message
        tk.messagebox.showinfo("Success", "JSON data loaded to Google Sheets!")

# Function to save Google Sheets to JSON file
def save_sheets_to_json():
    # Open Google Sheets document
    sh = gc.open('Test')
    worksheet = sh.sheet1

    # Get all records from the worksheet
    data = worksheet.get_all_records()

    # Open file dialog to select JSON file
    json_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    
    if json_file:
        # Write data to JSON file
        with open(json_file, "w") as f:
            json.dump(data, f)
        
        # Show success message
        tk.messagebox.showinfo("Success", "Google Sheets data saved to JSON!")

# Function to save Google Sheets and JSON file with specified filename
def save_with_filename():
    # Open Google Sheets document
    sh = gc.open('Test')
    worksheet = sh.sheet1

    # Get all records from the worksheet
    data = worksheet.get_all_records()

    # Get the specified filename from the entry field
    filename = filename_entry.get()

    if filename:
        # Save Google Sheets data
        worksheet.clear()
        worksheet.append_rows(data)

        # Save JSON file
        json_file = f"{filename}.json"
        with open(json_file, "w") as f:
            json.dump(data, f)

        # Show success message
        tk.messagebox.showinfo("Success", "Google Sheets and JSON files saved with specified filename!")

# Create button to load JSON file to Google Sheets
load_button = tk.Button(root, text="Load JSON to Sheets", command=load_json_to_sheets)
load_button.pack(pady=10)

# Create button to save Google Sheets to JSON file
save_sheets_button = tk.Button(root, text="Save Sheets to JSON", command=save_sheets_to_json)
save_sheets_button.pack(pady=10)

# Create entry field for specifying filename
filename_label = tk.Label(root, text="Filename:")
filename_label.pack()

filename_entry = tk.Entry(root)
filename_entry.pack()

# Create button to save Google Sheets and JSON file with specified filename
save_button = tk.Button(root, text="Save with Filename", command=save_with_filename)
save_button.pack(pady=10)

root.mainloop()
