import easyocr
import os
import time

reader = easyocr.Reader(['en'])

test_files = os.listdir('test')

for file_name in test_files:
    
    path = os.path.join('test', file_name)

    start_time = time.time()
    result = reader.readtext(path)
    end_time = time.time()
    print(f'The time taken was{end_time - start_time}')
    text_results = [text for _, text, _ in result]
    print(f"{file_name}: ", text_results)

print(reader)