import keras_ocr
import os
import time

pipeline = keras_ocr.pipeline.Pipeline()

test_files = os.listdir('test')

for file_name in test_files:
    path = os.path.join('test', file_name)
    
    start_time = time.time()
    
    image = keras_ocr.tools.read(path)
    
    prediction_groups = pipeline.recognize([image])
    
    end_time = time.time()
    
    time_taken = end_time - start_time
    
    # Extract the text results
    # text_results = [text for text, box in prediction_groups[0]]
    print(f"{file_name}: ", prediction_groups)
    print(f"Time taken for {file_name}: {time_taken} seconds")
