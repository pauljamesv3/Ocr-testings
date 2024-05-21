from paddleocr import PaddleOCR
import os
import time 

ocr = PaddleOCR(use_angle_cls=True, lang='en')

test_files = os.listdir('test')

for file_name in test_files:
    path = os.path.join('test', file_name)
    
    start_time = time.time()
    result = ocr.ocr(path, cls=True)
    end_time = time.time()
    print(f"The time taken was: {end_time - start_time}")
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line[1][0])
