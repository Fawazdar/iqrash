import tkinter as tk
from tkinter import messagebox
from booking_handler import validate_and_save
from confirmation import generate_confirmation
import social_links

def launch_booking_ui():
    def submit_form():
        name = name_entry.get()
        contact = contact_entry.get()
        date = date_entry.get()
        event_type = event_entry.get()
        notes = notes_entry.get("1.0", tk.END)

        valid, message = validate_and_save(name, contact, date, event_type, notes)
        if valid:
            confirmation = generate_confirmation(name, date)
            messagebox.showinfo("Success", confirmation)
        else:
            messagebox.showerror("Error", message)

    root = tk.Tk()
    root.title("DJ Vlad Booking Tool")
    root.geometry("400x400")

    tk.Label(root, text="Full Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Contact Info").pack()
    contact_entry = tk.Entry(root)
    contact_entry.pack()

    tk.Label(root, text="Event Date (YYYY-MM-DD)").pack()
    date_entry = tk.Entry(root)
    date_entry.pack()

    tk.Label(root, text="Event Type").pack()
    event_entry = tk.Entry(root)
    event_entry.pack()

    tk.Label(root, text="Notes").pack()
    notes_entry = tk.Text(root, height=5, width=30)
    notes_entry.pack()

    tk.Button(root, text="Submit Booking", command=submit_form).pack(pady=10)

    # Social links
    tk.Button(root, text="Instagram", command=social_links.open_instagram).pack(side=tk.LEFT, padx=5)
    tk.Button(root, text="SoundCloud", command=social_links.open_soundcloud).pack(side=tk.LEFT, padx=5)

    root.mainloop()
