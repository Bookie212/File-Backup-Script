# 💾 Folder Backup Script

A simple yet powerful **Python automation script** that creates backups of any folder on your computer.  
Each backup is timestamped automatically, helping you keep organized snapshots of your files.

---

## ✨ Features

✅ Creates a new backup folder with the current date and time  
✅ Preserves original filenames and metadata (`shutil.copy2`)  
✅ Works on **Windows**, **macOS**, and **Linux**  
✅ Automatically creates missing folders (`mkdir(parents=True)`)  
✅ Lightweight — no external dependencies  

---

## 🧠 Example

### 📂 Source Folder
C:\Users\user\Desktop\Sample folder
│
├── notes.txt
├── report.pdf
└── image1.jpg

### 📦 After Running Script
C:\Users\user\Desktop\Backup folder
└── backup_file_2025-10-22_145233
├── notes.txt
├── report.pdf
└── image1.jpg

⚙️ Requirements
1. Python 3.6+
No third-party modules required
(only built-in modules: pathlib, datetime, shutil)

🪄 How to Run
1. Clone or download this script
2. Edit your folder path inside the script:
  backup_folder(r"C:\Users\user\Desktop\Sample folder")
3. Run the script:
  python backup_folder.py
4. Your backup will be created inside:
  C:\Users\user\Desktop\Backup folder\

💡 What I Learned
1. How to manage paths using pathlib
2. Using datetime for timestamps
3. Copying files with metadata using shutil.copy2
4. Automating file backups safely

👩🏽‍💻 Author
Bukola Hambolu
📧 hambolubukola650@gmail.com
🔗 (https://www.linkedin.com/in/bukola-hambolu-71a581209/)

💼 Aspiring DevOps Engineer | IT Support & Cloud Enthusiast
⭐️ If you found this project helpful, consider starring the repo!