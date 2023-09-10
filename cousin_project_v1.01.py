import tkinter as tk
from tkinter import messagebox
import gspread
import json

# Initialize Google Sheets API
gc = gspread.service_account(filename='client_secret.json')
sh = gc.open('Test')
worksheet = sh.sheet1

# Fetch the data
data = worksheet.get_all_records()

# Create the root window
root = tk.Tk()
root.title("SCUM Economy Editor")

# Create a frame for the entries
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create a frame inside the canvas to hold the entries
entries_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=entries_frame, anchor='nw')

# Function to update the Google Sheets and the JSON file
def update():
    # Create a new list of dictionaries based on the entries
    new_data = []
    for entry in entries:
        new_data.append({
            "CATEGORY": entry[0].get(),
            "ITEM": entry[1].get(),
            "Item Code?": entry[2].get(),
            "OFFICIAL  Player 'BUY' PRICE": entry[3].get(),
            "GUN RUNNERS: PLAYER BUY PRICE": entry[4].get(),
            "OFFICIAL Player SELL PRICE (100% Quality)": entry[5].get()
        })

    # Update the Google Sheets
    worksheet.clear()
    worksheet.append_rows(new_data)

    # Update the JSON file
    with open("economy_override.json", "w") as f:
        json.dump(new_data, f)

    messagebox.showinfo("Success", "Data updated successfully!")

# Create entries for each item
entries = []
for i, item in enumerate(data):
    category_entry = tk.Entry(entries_frame)
    category_entry.insert(0, item['CATEGORY'])
    category_entry.grid(row=i, column=0)

    item_entry = tk.Entry(entries_frame)
    item_entry.insert(0, item['ITEM'])
    item_entry.grid(row=i, column=1)

    item_code_entry = tk.Entry(entries_frame)
    item_code_entry.insert(0, item['Item Code?'])
    item_code_entry.grid(row=i, column=2)

    official_buy_entry = tk.Entry(entries_frame)
    official_buy_entry.insert(0, item["OFFICIAL  Player 'BUY' PRICE"])
    official_buy_entry.grid(row=i, column=3)

    gun_runners_buy_entry = tk.Entry(entries_frame)
    gun_runners_buy_entry.insert(0, item['GUN RUNNERS: PLAYER BUY PRICE'])
    gun_runners_buy_entry.grid(row=i, column=4)

    official_sell_entry = tk.Entry(entries_frame)
    official_sell_entry.insert(0, item['OFFICIAL Player SELL PRICE (100% Quality)'])
    official_sell_entry.grid(row=i, column=5)

    entries.append((category_entry, item_entry, item_code_entry, official_buy_entry, gun_runners_buy_entry, official_sell_entry))
# Create a button to update the data
update_button = tk.Button(entries_frame, text="Update", command=update)
update_button.grid(row=len(data), column=0, columnspan=6)

# Configure the scrollbar to work with the canvas
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=canvas.yview)

# Update the canvas scrollregion whenever the size of the entries_frame changes
entries_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Pack the canvas and scrollbar
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Pack the frame and canvas
frame.pack(fill=tk.BOTH, expand=True)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a button to update the data
update_button = tk.Button(root, text="Update", command=update)
update_button.pack(pady=10)

root.mainloop()
