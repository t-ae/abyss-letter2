#!/usr/bin/env python

import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt
import sys

with tf.device("/cpu:0"):
    from keras.models import load_model

    def create_random_features(num):
        np.random.seed(123456)
        return np.random.uniform(low=-1, high=1, 
                            size=[num, 4, 4, 4])


    files_dir = os.path.dirname(__file__)
    npy_path = os.path.join(files_dir, "./dcgan_train_data.npy")
    if len(sys.argv) > 1:
        model_path = sys.argv[1]
    else:
        model_path = os.path.join(files_dir, "./dcgan_model.h5")

    dcgan = load_model(model_path)
    dcgan.summary()

    # for l in dcgan.layers[0].layers:
    #     print(l)
    #     print(l.get_weights())

    rows = 7
    cols = 10

    features = create_random_features(rows*cols)
    images = dcgan.layers[0].predict(features)

    # print(np.max(images[0] - images[1]))

    plt.gray()
    fig = plt.figure()
    for i in range(rows):
        for j in range(cols):
            if i*cols+j >= len(images):
                break
            ax = fig.add_subplot(rows,cols,i*cols+j+1)
            ax.imshow(images[i*cols+j].reshape([32, 32]))
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
    plt.show()