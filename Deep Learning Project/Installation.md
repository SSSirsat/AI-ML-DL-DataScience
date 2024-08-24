# Installation Instruction for DNN on Windows in (10* min)

## Step 1: Must have Nvidia Graphics card.

## Step 2: Install Anaconda in your system

## Step 3: Create new conda environment

      - conda create -n tf-gpu tensorflow-gpu
      
      it will handle everything for you like Cuda Toolkit, CuDNN libraries and Other C++ lib as well
      
      - conda activate tf-gpu
      
## Step 4: Install depedence libraries as per our Project

      - Pandas, Numpy, Keras, etc
      
      - ex: conda install Numpy
      
## Step 5: Check tensorflow GPU is recorganising or not

      - import tensorflow as tf
      
      - print("Number of available GPU:", len(tf.config.list_physical_devices('GPU')))
      
      - print(tf.test.is_gpu_available())
      
## Step 6: Run your any deep learning py file or project to check.
