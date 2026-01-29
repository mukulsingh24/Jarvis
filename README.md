# Sensi - Workflow Automation

A simple automation tool that opens your prerequisite apps for different work modes with a single command. Save time and clicks every day!

## 🎯 What It Does

Sensi automatically launches the apps you need for specific tasks, so you can jump straight into work.

## 📁 Project Structure

```
Sensi/
├── code.py           # Study Mode - opens coding environment
├── photoediting.py   # Design Mode - opens design tools
└── README.md
```

## 🚀 Available Modes

### 🖥️ Study Mode (`code.py`)
Opens your coding environment:
- Google Chrome (Default profile)
- Brave Browser (Profile 1)
- VS Code with your project folder

### 🎨 Design Mode (`photoediting.py`)
Opens your design tools:
- Brave Browser (Profile 5)
- Adobe Photoshop 2022

## 🎤 How to Use

Run the mode you need:

```bash
# For coding/study work
python code.py

# For design work
python photoediting.py
```

| Command | Action |
|---------|--------|
| `python code.py` | Launches Study Mode |
| `python photoediting.py` | Launches Design Mode |

## ⚙️ Customization

### Add New Apps
Edit the `apps` list in `code.py` or `photoediting.py`:
```python
apps = [
    [r"C:\Path\To\App.exe", "--optional-args"],
]
```

### Create New Modes
Create a new `.py` file following the same pattern:
```python
import subprocess
import time

apps = [
    [r"C:\Path\To\App1.exe"],
    [r"C:\Path\To\App2.exe", "--args"],
]

for app in apps:
    try:
        subprocess.Popen(app)
        time.sleep(1)
    except Exception as e:
        print(f"Error Opening {app}: {e}")
```

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| App not opening | Check the file path in the respective `.py` file |
| "File not found" error | Verify the app is installed at the specified path |

## 🔮 Future Scope

- **Voice Control** - Wake word detection ("Sensi") to launch modes hands-free using speech recognition
- **GUI Interface** - A simple UI to select and run modes
- **Scheduled Automation** - Auto-launch modes at specific times
- **More Modes** - Music mode, Gaming mode, etc.
