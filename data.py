import numpy as np
import math

### Store data matrices for Baxter Robot ###

# inertia tensors
# IXX, IYY, IZZ, IXY, IYZ, IXZ
link1 = [0.0470910226, 0.035959884, 0.0376697645,-0.0061487003,-0.0007808689,0.0001278755]
link2 = [ 0.027885975, 0.020787492, 0.0117520941,-0.0001882199, 0.0020767576, -0.00030096397]
link3 = [0.0266173355, 0.012480083, 0.0284435520, -0.0039218988, -0.001083893, 0.0002927063]
link4 = [0.0131822787, 0.009268520, 0.0071158268, -0.0001966341, 0.000745949, 0.0003603617]
link5 = [0.0166774282, 0.003746311, 0.0167545726, -0.0001865762, 0.0006473235, 0.0001840370]
link6 = [0.0070053791, 0.005527552, 0.0038760715, 0.0001534806, -0.0002111503, -0.0004438478]
link7 = [0.0008162135, 0.0008735012, 0.0005494148, 0.000128440, 0.0001057726, 0.00018969891]

inertia = np.array([link1, link2, link3, link4, link5, link6, link7]).reshape(7, 6)
np.savetxt("inertia_tensors.txt", inertia)

# center of mass tensors
link1 = [-0.05117, 0.07908, 0.00086]
link2 = [0.00269, -0.00529, 0.06845]
link3 = [-0.07176, 0.08149, 0.00132]
link4 = [0.00159, -0.01117, 0.02618]
link5 = [-0.01168, 0.13111, 0.0046]
link6 = [0.00697, 0.006, 0.06048]
link7 = [0.005137, 0.0009572, -0.06682]

com = np.array([link1, link2, link3, link4, link5, link6, link7]).reshape(7, 3)
np.savetxt("center_of_mass.txt", com)

# Denavit-Hartenberg 
# d (m) a (m) α (rad) m (kg)
link1 = [0.2703, 0.069, -math.pi/2, 5.70044]
link2 = [0, 0, math.pi/2, 3.22698]
link3 = [0.3644, 0.069, -math.pi/2, 4.31272]
link4 = [0, 0, math.pi/2, 2.07206]
link5 = [0.3743, 0.01, -math.pi/2, 2.24665]
link6 = [0, 0, math.pi/2, 1.60979]
link7 = [0.2295, 0, 0, 0.54218]

dh = np.array([link1, link2, link3, link4, link5, link6, link7]).reshape(7, 4)
np.savetxt("denavit_hartenberg.txt", dh)

# Jacobian matrices

