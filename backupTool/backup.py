import os
import shutil
import datetime
import time
import schedule

source_dir = "C:\\Users\\Nehan\\OneDrive\\Pictures\\Screenshots"
destination_dir = "D:\\austinWork\\backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()