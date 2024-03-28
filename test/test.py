import pyaudio


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024 * 2
dev_index = 30

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if dev["name"] == "Stereo Mix (Realtek(R) Audio)" and dev["hostApi"] == 0:
        dev_index = dev["index"]
        print("dev_index", dev_index)


stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    input_device_index=dev_index,
    frames_per_buffer=CHUNK,
)
data = stream.read(CHUNK)

print(f"length of data: {len(data)}")

new_data = []
for elem in data:
    new_data.append(elem)

print(new_data[:1024])
