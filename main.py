import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def organize_downloads_folder():

    
    path = 'C:\\Users\\brand\\Downloads\\'  # Use double backslashes for Windows paths

    for file_path in os.listdir(path):
        file_name, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()  # Convert the extension to lowercase for comparison

        # pdf folder
        if file_extension == ".pdf":
            destination_folder = os.path.join(path, 'PDFS')
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
        # docs folder
        elif file_extension in {".docx", ".doc", ".docm", ".txt", ".xlsx"}:
            destination_folder = os.path.join(path, 'DOCS')
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
        # videos folder
        elif file_extension in {".wmv", ".mov", ".mp4", ".mkv", ".gif"}:
            destination_folder = os.path.join(path, 'VIDEOS')
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
        # pictures folder
        elif file_extension in {".jpeg", ".jpg", ".png", ".heif"}:
            destination_folder = os.path.join(path, 'PICTURES')
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
        elif file_extension in {".mp3"}:
            destination_folder = os.path.join(path, 'AUDIO')
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
        elif file_extension in {".exe", ".msi"}:
            destination_folder = os.path.join(path, 'APPLICATIONS')
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
        else:
            # If the file doesn't match any known extension, continue to the next file
            continue

        # Provide the complete destination path, including the file name
        destination_path = os.path.join(destination_folder, file_path)

        os.rename(os.path.join(path, file_path), destination_path)
        print(f"Moved {file_path} to {destination_path}")

class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file added: {event.src_path}")
            time.sleep(1)  # Wait for 1 second to avoid any file locks
            organize_downloads_folder()

if __name__ == "__main__":
    path = 'C:\\Users\\brand\\Downloads\\'
    event_handler = DownloadsHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        print("Watching for new files in Downloads folder...")
        while True:
            time.sleep(10)  # Check for new files every 10 seconds
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
