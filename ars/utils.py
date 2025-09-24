from datetime import datetime
from zoneinfo import ZoneInfo
import os, platform, subprocess

def getNow():
	now = datetime.now(ZoneInfo("Asia/Dhaka"))
	return now.strftime("%d-%B-%y %I:%M:%S %p")

def getToday():
	now = datetime.now(ZoneInfo("Asia/Dhaka"))
	return now.strftime("%d-%B-%y")

def getTimeStamp():
	now = datetime.now(ZoneInfo("Asia/Dhaka"))
	return now.strftime("_%d_%B_%y_%I_%M_%S_%p_")

def openFile(fp):
		#Open files using this method
		if platform.system() == "Windows" or platform.system() == "nt":
				os.startfile(fp)
		elif platform.system() == "Darwin":
			subprocess.run(["open", fp])
		else:
			subprocess.run(["xdg-open", fp])

def clear_reports():
	try:
		REPORT_DIR = os.path.join(os.path.dirname(__file__), "reports")
		if not os.path.exists(REPORT_DIR):
			print(f"Directory {REPORT_DIR} does not exist.")
			return

		print(f"Clearing reports in: {REPORT_DIR}")
		for filename in os.listdir(REPORT_DIR):
			file_path = os.path.join(REPORT_DIR, filename)
			if filename.endswith('.pdf'):
				os.remove(file_path)
				print(f"Deleted: {filename}")
			else:
				print(f"{filename} is not a PDF, skipped.")

		print(f"{REPORT_DIR} has been cleared successfully.")
	except Exception as e:
		print(f"Error: {e}")

def isZero( value: str):
#this method checkhs if the given value is 0?
#if its a 0 then return empty else returns timeStamp from the utils module, I Used this method in ScaleReport Application.
	return "" if value == "0" else getNow()

def isDigit(value):
	#this method checks if the value is a number, if number then returns the value else retuns a 0.  I Used this method in ScaleReport Application.
	return value if value.isdigit() else 0


def isValue(value,valueToUse):
# first check if value is not empty
# if the value is empty then valueToUse otherwise return value. 
	return value if value is not ""  else valueToUse