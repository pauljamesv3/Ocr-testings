import lanyocr
import os

ocr = lanyocr.OCR()

test_files = os.listdir('test')

for file_name in test_files:
    
    path = os.path.join('test', file_name)

    result = ocr.ocr(path)

    text_results = [line[1] for line in result]
    print(f"{file_name}: ", text_results)
