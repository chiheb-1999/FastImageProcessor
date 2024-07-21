import os
import cv2 as cv
import shutil
import time
import threading
import sys
from queue import Queue

folder_path = os.getcwd()

inputFolder = os.path.join(folder_path, '/home/parallels/Desktop/ImageProcessingProject/InputImages')
outputFolder = os.path.join(folder_path, '/home/parallels/Desktop/ImageProcessingProject/OutputImages')


mthreads = 6

if len(sys.argv) == 2:
    mthreads = int(sys.argv[1])


if os.path.exists(outputFolder):
    shutil.rmtree(outputFolder)
os.mkdir(outputFolder)


semaphore = threading.Semaphore(mthreads)


mutex = threading.Lock()


image_queue = Queue()

def producer(images):
    for img_name in images:
        image_queue.put(img_name)

def consumer():
    while True:
        img_name = image_queue.get()
        if img_name is None:
            break
        with semaphore:  
            rgb_to_grayscale(img_name)
        image_queue.task_done()

def rgb_to_grayscale(img_name):
    inputImage = os.path.join(inputFolder, img_name)
    img = cv.imread(inputImage)

    if img is None:
        with mutex:
            print(f"Failed to load image: {inputImage}")
        return

    gray_scale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    outputFile = os.path.join(outputFolder, f'/home/parallels/Desktop/ImageProcessingProject/OutputImages/processed_{img_name}')
    cv.imwrite(outputFile, gray_scale)

allImages = os.listdir(inputFolder)

if len(allImages) < 500:
    print('Not enough files in InputImages folder')
    exit(0)

for j in range(100, 501, 100):
    start_bundle = time.time()

    
    producer_thread = threading.Thread(target=producer, args=(allImages[:j],))
    producer_thread.start()

    
    consumer_threads = []
    for _ in range(mthreads):
        thread = threading.Thread(target=consumer)
        consumer_threads.append(thread)
        thread.start()

   
    producer_thread.join()

    
    for _ in range(mthreads):
        image_queue.put(None)

    
    for thread in consumer_threads:
        thread.join()

    end_bundle = time.time()
    with mutex:
        print(f"{j} images processed in {end_bundle - start_bundle} seconds")

end = time.time()
