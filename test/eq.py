import pyaudio
from colorama import Fore, Back, init
import numpy as np
import time, os, struct
from tkinter import TclError
import matplotlib.pyplot as plt
from scipy.fftpack import fft

init()

# %matplotlib tk

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


fig, (ax, ax2) = plt.subplots(2, figsize=(15, 8))

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK,
)

x = np.arange(0, 2 * CHUNK, 2)

x_fft = np.linspace(0, RATE, CHUNK)

(line,) = ax.plot(x, np.random.rand(CHUNK), "-", lw=2)
# line_fft, = ax2.plot(x_fft, np.random.rand(CHUNK), '-', lw=2)
(line_fft,) = ax2.semilogx(x_fft, np.random.rand(CHUNK), "-", lw=2)


ax.set_title("AUDIO WAVEFORM")
ax.set_xlabel("samples")
ax.set_ylabel("volume")
ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])


ax2.set_xlim(20, RATE / 2)


plt.show(block=False)


print("stream started")


frame_count = 0
start_time = time.time()


while True:
    data = stream.read(CHUNK)

    data_int = struct.unpack(str(2 * CHUNK) + "B", data)

    data_np = np.array(data_int, dtype="b")[::2] + 128

    line.set_ydata(data_np)

    y_fft = fft(data_int)
    line_fft.set_ydata(np.abs(y_fft[0:CHUNK] * 2 / (256 * CHUNK)))

    try:
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1

    except TclError:
        frame_rate = frame_count / (time.time() - start_time)

        print("stream stopped")
        print(f"average frame rate = {frame_rate}")
        break
