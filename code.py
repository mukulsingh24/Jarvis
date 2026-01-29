import subprocess
import time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
brave_path  = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
vs_path = r"C:\Users\msrk1\AppData\Local\Programs\Microsoft VS Code\Code.exe"

apps = [
    [chrome_path, "--profile-directory=Default"],
    [brave_path, "--profile-directory=Profile 1"],
    [vs_path, r"D:\coding\AMD HACKATHON\AGRODRISHTI"]

]
for app in apps:
    try:
        subprocess.Popen(app)
        time.sleep(1)
    except Exception as e:
        print("Error Openg {app} : {e}")

