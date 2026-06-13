# utils.py module. 
# Time related functions/methods from utils.py module
from .timeUtils import getNow
from .timeUtils import getToday
from .timeUtils import getTimeStamp

# Helper functions/methods for PyQtScaleReport project.
from .fileUtils import openFile
from .validator import isZero
from .validator import isDigit
from .validator import ifEmpty

# color_utils.py module
from .color_utils import getColorPallete

# mail module
from .mail import Email

__version__ = "1.2.0"
