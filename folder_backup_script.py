from pathlib import Path
from datetime import datetime
import shutil

def backup_folder(source_path):
  # Converts the input path string to Path object
  source = Path(source_path)

  # Gets current time and format it
  current_dt = datetime.now()
  dt = current_dt.strftime('%Y-%m-%d_%H%M%S')

  # Defines and creates the backup folder
  backup_folder = Path(r'C:\Users\user\Desktop') / 'Backup folder' / f"backup_file_{dt}"
  backup_folder.mkdir(parents=True, exist_ok=True)

  # Iterates over files and copy it
  for file in source.iterdir():

    # Defines the new path (destination folder and original file name)
    new_path = backup_folder / file.name
    try:
      shutil.copy2(file, new_path)
    except Exception as e:
      print(f'Failed to copy {file}: {e}')

  print('Backup files created successfully✅')


backup_folder(r'C:\Users\user\Desktop\Sample folder')