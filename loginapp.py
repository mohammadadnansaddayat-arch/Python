import tkinter as tk
from tkinter import messagebox

users = {}

app = tk.Tk()
app.title("Login app")
app.geometry("600x500")
app.config(bg="#1B2848")

def clear_frame():
    for widget in app.winfo_children():
        widget.destroy()

def create_entry(parent, placeholder, show=None):
    entry = tk.Entry(parent, font=("Segoe UI", 12),bd=0 , bg="#e2e8f0", fg="#64748b", width=30)
    entry.insert(0, placeholder)

    def on_focus(e):
        if entry.get() == placeholder:
            entry.delete(0,tk.END)