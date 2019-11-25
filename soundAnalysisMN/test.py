from keras.models import Sequential
from kapre.kapre.time_frequency import Melspectrogram
from kapre.kapre.utils import Normalization2D
from kapre.kapre.augmentation import AdditiveNoise

# 6 channels (!), maybe 1-sec audio signal, for an example.
input_shape = (6, 44100)
sr = 44100
model = Sequential()
# A mel-spectrogram layer
model.add(Melspectrogram(n_dft=512, n_hop=256, input_shape=input_shape,
                         padding='same', sr=sr, n_mels=128,
                         fmin=0.0, fmax=sr/2, power_melgram=1.0,
                         return_decibel_melgram=False, trainable_fb=False,
                         trainable_kernel=False,
                         name='trainable_stft'))
# Maybe some additive white noise.
model.add(AdditiveNoise(power=0.2))
# If you wanna normalise it per-frequency
model.add(Normalization2D(str_axis='freq')) # or 'channel', 'time', 'batch', 'data_sample'
# After this, it's just a usual keras workflow. For example..
# Add some layers, e.g., model.add(some convolution layers..)
# Compile the model
model.compile('adam', 'categorical_crossentropy') # if single-label classification
# train it with raw audio sample inputs
x = load_x() # e.g., x.shape = (10000, 6, 44100)
y = load_y() # e.g., y.shape = (10000, 10) if it's 10-class classification
# and train it
model.fit(x, y)
# Done!