# MultithreadedImageProcessing

A project demonstrating performance improvement in image processing using multithreading with Python.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Introduction

Image processing can be a time-consuming task, especially when dealing with a large number of images. This project demonstrates how multithreading can be used to speed up the process of converting images to grayscale using Python.

## Features

- Sequential and multithreaded image processing
- Efficient handling of multiple images
- Improved performance using multithreading

## Requirements

- Python 3.x
- OpenCV
- Git

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-github-username/MultithreadedImageProcessing.git
    cd MultithreadedImageProcessing
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install opencv-python-headless
    ```

4. **Prepare input images:**

    - Create an `InputImages` directory in the project root and place the images you want to process there.

    ```bash
    mkdir InputImages
    # Copy your images to this directory
    ```

5. **Prepare output directory:**

    - Create an `OutputImages` directory in the project root where processed images will be saved.

    ```bash
    mkdir OutputImages
    ```

## Usage

### Sequential Image Processing

To run the sequential image processing script, use the following command:

```bash
python3 gray_scale.py
