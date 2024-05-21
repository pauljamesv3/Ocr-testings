import pytesseract
from PIL import Image
import os
import time

test_files = os.listdir('test')

for file_name in test_files:
    path = os.path.join('test', file_name)
    
    img = Image.open(path)
    
    start_time = time.time()
    text = pytesseract.image_to_string(img)
    end_time = time.time()
    print(f"The time taken was: {end_time - start_time}")
    print(f"{file_name}: ", text.split('\n'))

print(pytesseract)
