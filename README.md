#File Organizer for Downloads Folder
This Python script is designed to automatically organize the files in your Downloads folder on Windows. It watches for new files in the Downloads folder and moves them to specific subfolders based on their file extensions. This helps you keep your Downloads folder clean and organized.

##Requirements
Python 3.x
watchdog library (install using pip install watchdog)
##How to Use
Make sure you have Python 3.x installed on your system.
Install the required watchdog library by running pip install watchdog in your terminal or command prompt.
Download the organize_downloads.py script from this repository and place it in a convenient location.
Open the script using a text editor or IDE of your choice.
##How it Works
The script uses the watchdog library to monitor the Downloads folder for new files. When a new file is detected, it checks its file extension and moves it to the appropriate subfolder accordingly.

The following file extensions are recognized and their corresponding destination folders are created if they don't exist:

PDF files: Stored in the 'PDFS' folder.
Microsoft Office documents (DOCX, DOC, DOCM, TXT, XLSX): Stored in the 'DOCS' folder.
Videos (WMV, MOV, MP4, MKV, GIF): Stored in the 'VIDEOS' folder.
Pictures (JPEG, JPG, PNG, HEIF): Stored in the 'PICTURES' folder.
Audio files (MP3): Stored in the 'AUDIO' folder.
Executable files (EXE, MSI): Stored in the 'APPLICATIONS' folder.
Any files with extensions that don't match the above categories will be skipped and left in the Downloads folder.

##Usage
Open a terminal or command prompt.
Navigate to the directory where the script organize_downloads.py is located.
Run the script using the command: python organize_downloads.py
The script will start watching for new files in the Downloads folder.
Whenever a new file is added to the Downloads folder, it will be automatically organized into the corresponding subfolder based on its file extension.
##Important Notes
If you have special characters or spaces in your Downloads folder path, you might encounter issues. It's recommended to use the default Downloads folder or modify the script's path variable to match your Downloads folder path correctly.
The script will run continuously and organize new files as they appear. To stop the script, press Ctrl + C in the terminal or command prompt.
##Disclaimer
Please use this script at your own risk. Although the script is designed to organize files safely, it's always a good idea to back up your important files before running any automation tool.

##License
This script is open-source and licensed under the MIT License. You are free to modify, distribute, and use it for personal or commercial purposes.

##Acknowledgments
The script uses the watchdog library to handle file system events. Special thanks to the developers and contributors of the watchdog project.

If you encounter any issues, have suggestions for improvements, or want to contribute to this project, feel free to create an issue or submit a pull request on GitHub. Happy organizing!
