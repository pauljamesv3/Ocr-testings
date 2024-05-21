import easyocr
import os
import time

reader = easyocr.Reader(['en'])

test_files = os.listdir('test')

for file_name in test_files:
    
    path = os.path.join('test', file_name)

    result = reader.readtext(path)

    text_results = [text for _, text, _ in result]
    print(f"{file_name}: ", text_results)

print(reader)