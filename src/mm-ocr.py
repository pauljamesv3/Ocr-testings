from mmocr.apis import MMOCR
import os

ocr = MMOCR(det='DB_r18', recog='SAR')

test_files = os.listdir('test')

for file_name in test_files:
    path = os.path.join('test', file_name)
    
    result = ocr.readtext(path, output=None)
    
    for res in result:
        for line in res['result']:
            print(line['text'])
