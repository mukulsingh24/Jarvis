import subprocess
import time

brave_path  = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
ps_path = r"C:\Program Files\Adobe\Adobe Photoshop 2022\Photoshop.exe"

apps = [
    [brave_path,"--profile-directory=Profile 5"],
    [ps_path]
]

for app in apps:
    try:
        subprocess.Popen(app)
        time.sleep(1)
    except Exception as e:
        print("Error Opening {app} as {e}")