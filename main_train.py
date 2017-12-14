# import NN architectures for speech recognition
from models import *
# import function for training acoustic model
from train_utils import train_model

from main_build import *

train_model(
    input_to_softmax=model_0,
    pickle_path='model_0.pickle',
    save_model_path='model_0.h5',
    spectrogram=False)  
