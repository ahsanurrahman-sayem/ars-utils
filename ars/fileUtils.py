def openFile(fp:str):
    """\"fp\" arg takes absolute file path and Opens the files with respective file handler."""
    import platform, subprocess

    if platform.system() == "Windows" or platform.system() == "nt":
        sf(fp)
    elif platform.system() == "Darwin":
        subprocess.run(["open", fp])
    else:
        subprocess.run(["xdg-open", fp])

def clearDir(dirToClear:str, fileSuffix:str):
    """ \"dirToClose:str\" arg takes directory name and \"fileSuffix:str\" takes file type e.g. '.txt/.py,etc'. """
    try:
        import os
        REPORT_DIR = os.path.join(os.path.dirname(__file__),dirToClear)
        if not os.path.exists(REPORT_DIR):
            print(f"Directory {REPORT_DIR} does not exist.")
            return

        print(f"Clearing \"{REPORT_DIR}\" directory...")
        for filename in os.listdir(REPORT_DIR):
            file_path = os.path.join(REPORT_DIR, filename)
            if filename.endswith(fileSuffix):
                os.remove(file_path)
                print(f"Deleted: {filename}")
            else:
                print(f"{filename} is not a type of \"{fileSuffix}\", skipped.")

        print(f"{REPORT_DIR} has been cleared successfully.")
    except Exception as e:
        print(f"Error: {e}")
