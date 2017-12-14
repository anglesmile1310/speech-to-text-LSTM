from data_generator import vis_train_features, plot_raw_audio, plot_mfcc_feature

#Config backend
from keras.backend.tensorflow_backend import set_session
import tensorflow as tf
config = tf.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.5
set_session(tf.Session(config=config))

# import NN architectures for speech recognition
from models import *
# import function for training acoustic model
from train_utils import train_model



""" Build model_0: 
    Simple LSTM    
"""
model_0 = simple_lstm_model(
    input_dim=13, #Use MFCC
    units=200,
    activation='relu'
)

