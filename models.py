""" AlexNet.
Applying 'Alexnet' to Oxford's 17 Category Flower Dataset classification task.
References:
    - Alex Krizhevsky, Ilya Sutskever and Geoffrey E. Hinton. ImageNet
    Classification with Deep Convolutional Neural Networks. NIPS, 2012.

Links:
    - [AlexNet Paper](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
"""

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization


def alexnet(width, height, lr, batch=64):
    # Start Layers

    network = input_data(shape=[None, width, height, 1], name='input')

    network = conv_2d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')

    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)

    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')

    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 3, activation='softmax')
    # End Layers

    network = regression(network, optimizer='momentum', batch_size=batch,
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, tensorboard_verbose=2,
                        tensorboard_dir='trained_models/log')

    return model


def alexnetAdam(width, height, lr, batch):
    # Start Layers

    network = input_data(shape=[None, width, height, 1], name='input')

    network = conv_2d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')

    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)

    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')

    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)

    network = fully_connected(network, 3, activation='softmax')
    # End Layers

    network = regression(network, optimizer='adam', batch_size=batch,
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, tensorboard_verbose=2,
                        tensorboard_dir='trained_models/log')

    return model
