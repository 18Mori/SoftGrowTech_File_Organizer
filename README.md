# File Optimizer (Automated File Organizer)

`File Optimizer` is a Python-based utility script designed to declutter your directories. It automatically categorizes and moves files into organized subfolders (Images, Documents, Videos, etc.) based on their file extensions.

## Features
* **Automatic Categorization**: Sorts files into predefined folders: `Images`, `Documents`, `Videos`, `Music`, `Archives`, and `Others`.
* **Conflict Prevention**: Automatically appends a timestamp to filenames if a file with the same name already exists in the destination folder.
* **Path Validation**: Ensures the target directory exists before attempting to move files.
* **Real-time Feedback**: Provides console logs for every file moved and a final summary of the operation.



## How It Works
The script follows a simple logical flow to ensure your data is handled safely:
1.  **Input**: The user provides a folder path.
2.  **Scan**: The script iterates through every file in that specific directory.
3.  **Map**: It matches the file extension against a dictionary of known types.
4.  **Move**: It creates the necessary subdirectories (if they don't exist) and moves the files.

## Prerequisites
* Python 3.x
* No external libraries are required.

## Installation & Usage
1.  **Clone or Download** the repository to your local machine.
2.  **Open your Terminal** or Command Prompt.
3.  **Navigate** to the folder containing `file_optimizer.py`.
4.  **Run the script**:
    ```bash
    python file_optimizer.py
    ```
5.  **Enter the path** of the directory you wish to organize when prompted (e.g., `C:\Users\YourName\Downloads`).

## Folder Mapping
| Category | Extensions |
| :--- | :--- |
| **Images** | .jpg, .jpeg, .png, .gif, .bmp |
| **Documents** | .pdf, .docx, .txt, .xlsx, .pptx |
| **Videos** | .mp4, .mkv, .mov, .avi |
| **Music** | .mp3, .wav, .aac |
| **Archives** | .zip, .rar, .7z, .tar |
| **Others** | Any extension not listed above |

## ⚠️ Notes
* The script only moves files in the **top-level** of the provided directory; it does not currently recurse into existing subfolders.
* Ensure you have read/write permissions for the directory you are organizing.
