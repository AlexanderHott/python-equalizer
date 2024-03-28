# {'index': 0, 'structVersion': 2, 'name': 'Microsoft Sound Mapper - Input', 'hostApi': 0, 'maxInputChannels': 2,
# 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.09, 'defaultLowOutputLatency': 0.09, 'defaultHighInputLatency': 0.18,
# 'defaultHighOutputLatency': 0.18, 'defaultSampleRate': 44100.0}

import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)

    # Device Index
    if dev["index"] > 9:
        index = str(dev["index"])
    else:
        index = "0" + str(dev["index"])

    # Struct Version
    structVersion = dev["structVersion"]

    name = dev["name"]

    # Host API
    hostApi = dev["hostApi"]

    maxInputChannels = dev["maxInputChannels"]

    maxOutputChannels = dev["maxOutputChannels"]

    # print(f"Index: {index}, Struct Version: {structVersion}, Host API: {hostApi}, Max Input: {maxInputChannels}, Max Output: {maxOutputChannels}, Name: {name}")
    print(
        f"Index: {index}, Host API: {hostApi}, Max Input: {maxInputChannels}, Max Output: {maxOutputChannels}, Name: {name}"
    )
