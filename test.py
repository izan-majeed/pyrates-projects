"""
  **** PYRATES CODING CLUB PROJECT ******
********* QR CODE SCANNER ULTIMATE **********
  ************* TAHOOR BILAL *************
"""

import cv2
from pyzbar.pyzbar import decode
img = cv2.imread("uploadthephoto.png")
code=decode(img)
print(code)

