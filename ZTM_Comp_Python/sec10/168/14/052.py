# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_14.md

class CustomException(Exception):
    """Exception raised for custom purpose
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message) -> None:
        self._message = message


n = int(input())

try:
    if n < 10:
        raise CustomException("Input < 10")
    elif n > 10:
        raise CustomException("Input > 10")
except CustomException as ce:
    print(f"Error: {ce._message}")
