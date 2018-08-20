import matplotlib.pyplot as pl
import cividis
import numpy as np

x = np.arange(0, 2*np.pi, 0.07)
y = np.arange(0, 2*np.pi, 0.07)
X, Y = np.meshgrid(x,y)
Z = np.cos(X) * np.sin(Y) * 20
Z += np.random.randn(*Z.shape)

pl.figure(figsize=(4,3.375))
pl.imshow(Z,cmap='cividis')
pl.colorbar()
pl.gcf().savefig('xmpl.png',dpi=150)

pl.show()
