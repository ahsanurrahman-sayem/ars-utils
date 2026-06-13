from datetime import datetime
from zoneinfo import ZoneInfo

def getNow(zoneInfo:str) -> str:
    # returns 12 hour time format.
	now = datetime.now(ZoneInfo(zoneInfo))
	return now.strftime("%d-%B-%y %I:%M:%S %p")

def getToday(str:zoneInfo) -> str:
	now = datetime.now(ZoneInfo(zoneInfo))
	return now.strftime("%d-%B-%y")

def getTimeStamp() -> str:
	now = datetime.now(ZoneInfo("Asia/Dhaka"))
	return now.strftime("_%d_%B_%y_%I_%M_%S_%p_")
