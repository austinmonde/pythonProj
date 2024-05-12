import os
import shutil
import datetime
import schedule
import time


source_dir = input("Please enter your source path: ")
destination_dir = input("Enter the path of where to backup: ")


def copy_folder_to_directory(source, dest):
    today = datetime.date.today() 
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

def l():
    copy_folder_to_directory(source_dir, destination_dir)
    
schedule.every().day.at("00:00").do(l)

while True:
    schedule.run_pending()
    time.sleep(60)
