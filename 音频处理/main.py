import cv2
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf

y,sr = librosa.load('音频处理/当那一天来临.mp3', mono=True, offset=0.0, duration=None)
melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
logmelspec = librosa.power_to_db(melspec)
plt.figure()
plt.subplot(2, 1, 1)
librosa.display.waveshow(y, sr, x_axis='time')
plt.title('Beat wavform')
plt.subplot(2, 1, 2)
librosa.display.specshow(logmelspec, sr=sr, x_axis='time', y_axis='mel')
plt.title('Mel spectrogram')
plt.tight_layout()
plt.show()









# audio, fs = sf.read("音频处理\宋祖英 - 好日子.mp3")
# x = [i[0] for i in audio]
# y = [i[1] for i in audio]
# plt.plot(x,y)
# plt.show()
# print(len(audio))

# with wave.open('音频处理\宋祖英 - 好日子.mp3','rb') as m:
#     pass