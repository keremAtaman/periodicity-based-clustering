import numpy as np

input = np.zeros(512)
for i in range(len(input)):
    if i%7 == 0:
        input[i] = 1

ratio_to_power = 0.25

w = np.fft.fft(input)
# get the "powers"
abs = np.absolute(w)
power = abs[0]
power_threshold = power * ratio_to_power
# get the periods
periods = 1. / np.fft.fftfreq(len(input))
results = []
for i in range(1,len(periods)):
    if abs[i] >= power_threshold:
        results.append(np.round(periods[i]))
print("done")