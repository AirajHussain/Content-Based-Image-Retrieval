# Content-Based Image Retrieval (CBIR)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

This project implements a **Content-Based Image Retrieval (CBIR)** system, utilizing **barcode-based feature extraction** to identify the closest matching images from a given database.  

## Overview  
The CBIR system processes an image database and uses feature projections to generate barcodes for images. It then compares the barcode of a query image against the database using **Hamming distance** to retrieve the closest match. The project includes:  
- **Barcode Generation Algorithm**: Extracts unique binary codes based on projections.  
- **Search Algorithm**: Finds matches using Hamming distance.  

### Key Features  
- Processes images from the MNIST dataset for image matching.  
- Efficient barcode generation with a complexity of **O(n³)**.  
- Linear search algorithm with a complexity of **O(n)**.  
- Accuracy rate: **83%**, with suggestions for improvement.  

## Algorithms  
### 1. Barcode Generation  
Generates a binary barcode for each image using four projection angles (0°, 45°, 90°, 135°). The barcodes are saved in `Barcode.txt`, and their respective paths are stored in `Address.txt`.  

### 2. Search Algorithm  
Compares the query image barcode to the database barcodes using Hamming distance to find the closest match.  

## Project Files  
- **main.py**: The primary entry point for running the CBIR system.  
- **Barcode.txt**: Stores barcodes for database images.  
- **Address.txt**: Maps barcodes to their image paths.  
- **data/**: Folder containing the MNIST images.  

## Prerequisites  
- Python 3.7+  
- Required libraries:  
  ```bash
  pip install numpy pillow

## How to run 

- Clone the repository: 
  ```bash
  clone https://github.com/AirajHussain/Content-Based-Image-Retrieval.git

  
- Running the program:
  ```bash
  cd Content-Based-Image-Retrieval
  python main.py
