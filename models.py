from keras import backend as K
from keras.models import Model
from keras.models import Input
from keras.layers.core import Dense, Activation
from keras.layers import TimeDistributed, BatchNormalization
from keras.layers.recurrent import (LSTM)


def simple_lstm_model(input_dim, units, activation, output_dim=29):
    """
    Input
    """
    input_data = Input(name='input', shape=(None, input_dim))

    """
    LSTM
        units: Pos Int: dimentional of output
        return_sequences: Bool - return the last output: output sequence or full sequence
        implementation: mode 1 - Large number, mode 2 - batch
    """
    lstm = LSTM(units, activation=activation, return_sequences=True, implementation=2, name='lstm-rnn')(input_data)

    """
    TODO: Add Batch normalization
    """
    bn_rnn = BatchNormalization(name='bn_rnn_1d')(lstm)

    """
    TODO: Add Time dense
        Time dense:
    """
    time_dense = TimeDistributed(Dense(output_dim))(bn_rnn)

    """
    TODO: Add activation
        'softmax' func:  
    """
    y_pred = Activation('softmax',name='activation')(time_dense)

    model = Model(inputs=input_data, outputs=y_pred)
    model.output_length = lambda x: x

    print(model.summary())
    return model
