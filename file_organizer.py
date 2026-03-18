import shutil
import logging
from pathlib import Path

# tracing setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def organize_files(file_path):
  # validate path
  base_path = Path(file_path).resolve()
  
  if not base_path.is_dir():
    logging.error(f'The Path {base_path} is not a valid directory.')
    return
  
  categories = {
        'Images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'},
        'Documents': {'.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'},
        'Videos': {'.mp4', '.mkv', '.mov', '.avi'},
        'Music': {'.mp3', '.wav', '.aac'},
        'Archives': {'.zip', '.rar', '.7z', '.tar'},
    }
  
  count = 0
  # Itarate over the path & organize files
  for i in base_path.iterdir():
    if not i.is_file():
      continue
    ext = i.suffix.lower()
    target_folder = 'Others'
    
    for category, extentions in categories.items():
      if ext in extentions:
        target_folder = category
        break
      
    # Secure Dir creation  
    target_dir = base_path / target_folder
    target_dir.mkdir(exist_ok=True)
    
    # move file to target dir
    target_file = target_dir / i.name
    
    # Avoid overwriting of existing files
    if target_file.exists():
      # rename file by appending a number suffix
      timestamp = int(i.shutil.time.time())
      target_file = target_dir / f'{i.stem}_{timestamp}{i.suffix}'
      try:
        shutil.move(str(i), str(target_file))
        logging.info(f'Moved: {i.name} >>> {target_folder}/')
        count=+1
      except Exception as e:
        logging.error(f'Failed to move {i.name}: {e}')
        
  print (f'>> Finished! Organised {count} files in {base_path.name} <<')
  
  
if __name__ == "__main__":
    print(">>> File Organizer <<<")
    folder = input("Enter path: ").strip()
    if folder:
        organize_files(folder)