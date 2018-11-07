import numpy as np
from scipy.fftpack import fft, ifft
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
fft = fft(x)
ifft = ifft(fft)

print "input x =", x, "\n"
print "fft of x =", fft, "\n"
print "ifft of fft =", ifft, "\n"
