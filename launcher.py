import subprocess
import time
import tkinter as tk
from tkinter import ttk
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# App configurations
STUDY_APPS = [
    [r"C:\Program Files\Google\Chrome\Application\chrome.exe", "--profile-directory=Default"],
    [r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe", "--profile-directory=Profile 1"],
    [r"C:\Users\msrk1\AppData\Local\Programs\Microsoft VS Code\Code.exe", r"D:\coding\AMD HACKATHON\AGRODRISHTI"]
]

DESIGN_APPS = [
    [r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe", "--profile-directory=Profile 5"],
    [r"C:\Program Files\Adobe\Adobe Photoshop 2022\Photoshop.exe"]
]

def launch_apps(apps):
    for app in apps:
        try:
            subprocess.Popen(app)
            time.sleep(1)
        except Exception as e:
            print(f"Error Opening {app}: {e}")

def start_study():
    root.destroy()
    launch_apps(STUDY_APPS)

def start_design():
    root.destroy()
    launch_apps(DESIGN_APPS)

# Create the window
root = tk.Tk()
root.title("Sensi Launcher")
root.geometry("300x200")
root.resizable(False, False)

# Center the window on screen
root.eval('tk::PlaceWindow . center')

# Style
root.configure(bg="#1e1e1e")

# Title label
title = tk.Label(root, text="🚀 Sensi", font=("Segoe UI", 24, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=20)

subtitle = tk.Label(root, text="Choose your mode:", font=("Segoe UI", 11), bg="#1e1e1e", fg="#888")
subtitle.pack()

# Button frame
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=20)

# Study button
study_btn = tk.Button(btn_frame, text="📚 Study", font=("Segoe UI", 12), 
                      width=10, height=2, command=start_study,
                      bg="#4CAF50", fg="white", activebackground="#45a049", 
                      relief="flat", cursor="hand2")
study_btn.pack(side=tk.LEFT, padx=10)

# Design button
design_btn = tk.Button(btn_frame, text="🎨 Design", font=("Segoe UI", 12),
                       width=10, height=2, command=start_design,
                       bg="#2196F3", fg="white", activebackground="#1976D2",
                       relief="flat", cursor="hand2")
design_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
