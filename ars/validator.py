def isZero(value: str) -> str:
#this method checkhs if the given value is 0?
#if its a 0 then return empty else returns timeStamp from the utils module, I Used this method in ScaleReport Application.
	
	# This method is used to check if the user had inserted a value in the QLineEdit object which is responsible to save time stamp of the moment when A Report is created.
	return "" if value == "0" else getNow()

def isDigit(value) -> int:
	#this method checks if the value is a number, if number then returns the value else retuns a 0.  I Used this method in ScaleReport Application.
	return value if value.isdigit() else 0


def ifEmpty(value,valueToUse):
# first check if value is not empty
# if the value is empty then valueToUse otherwise return value. 
	return valueToUse if value == "" else value
