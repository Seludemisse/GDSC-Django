import os
import shutil
import time

def is_file_modified_in_last_24_hours(file_path):
    current_time = time.time()
    twenty_four_hours_ago = current_time - (24 * 60 * 60)  

    file_stats = os.stat(file_path)
    modified_time = file_stats.st_mtime
    created_time = file_stats.st_ctime

    return modified_time >= twenty_four_hours_ago or created_time >= twenty_four_hours_ago

def update_files(files):
    for file_path in files:
        with open(file_path, 'a') as file:
            timestamp = time.strftime("_%Y%m%d_%H%M%S", time.localtime())
            file.write(timestamp)

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def move_files_to_directory(files, directory):
    for file_path in files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(directory, file_name)
        shutil.move(file_path, destination_path)


current_dir = os.getcwd()
files_in_dir = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]


files_to_update = [f for f in files_in_dir if is_file_modified_in_last_24_hours(os.path.join(current_dir, f))]


update_files(files_to_update)

last_24hours_dir = os.path.join(current_dir, "last_24hours")
create_directory_if_not_exists(last_24hours_dir)

move_files_to_directory(files_to_update, last_24hours_dir)