import numpy as np
import scipy.signal as sp


def find_template_1D(t, s):
    # TODO: Locate template t in signal s and return index. Use scipy.signal.correlate2d
    pass

s = np.array([[-1, 0, 0, 5, 1, 1, 0, 0, -1, -7, 2, 1, 0, 0, -1]])
t = np.array([[-1, -7, 2]])

print "Signal: \n {} \n {}".format(np.array(range(s.shape[1])), s[0])
print "Tiemplate: \n {} \n {}".format(np.array(range(t.shape[1])), t[0])

index = find_template_1D(t, s)
print "Index: {}".format(index)
