# import and global vars
from pathlib import Path
import shutil


base_dir = Path(r"D:\KickIroni\project\reels")
target_dir = base_dir / 'sorted'

# declare categories and extensions
FILE_CATEGORIES = {
    "image":['.png', '.jpeg'],
    "videos":['.mp4', 'wmv']
}


# create dirs based on categories
def create_category_directories():
    for category, _ in FILE_CATEGORIES.items():
        (target_dir / category).mkdir(parents=True, exist_ok=True)


# searching and categorizing files
def search_and_categorize_files():
    for file in base_dir.rglob("*"): #r glob recursive search for in to folders check
        for category, extensions in FILE_CATEGORIES.items():
            if file.suffix in extensions:  # format or extensions
                try:
                    shutil.copy(file,target_dir / category)
                except shutil.SameFileError:
                    pass
            
                 
# run the app
def main():
    create_category_directories()
    search_and_categorize_files()
    
if __name__ == "__main__":
    main()
