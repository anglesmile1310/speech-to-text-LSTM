from keras import backend as K
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.recurrent import (LSTM)


def simple_lstm_model(input_dim, activation, unit, output_dim):
    # Output of LSTM: 2D tensor with shape of (batch_size, output_dim)
    in_out_neurons = 2

    hidden_neurons = 300

    # Sequential model is a linear stack of layers.
    model = Sequential()

    
    model.add(
        LSTM(
            hidden_neurons,
            return_sequences=False,
            input_shape=(None, in_out_neurons)))
    model.add(Dense(in_out_neurons, input_dim=hidden_neurons))
    model.add(Activation("linear"))

    # RMSProp optimizer: leave the parameters of this optimizer at their default values
    # - (except the learning rate, which can be freely tuned)
    model.compile(loss="mean_squared_error", optimizer="rmsprop")

    print(model.summary())
    return model
