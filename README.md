# cividis

Register the color map _cividis_ for matplotlib, as described in

[Nuñez JR, Anderton CR, Renslow RS (2018) Optimizing colormaps with consideration for color vision deficiency to enable accurate interpretation of scientific data. PLoS ONE 13(7): e0199239](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0199239).

## Install

    pip install cividis


## Usage

After installation, just import `cividis` once and it's registered and usable

```python
import cividis
```

Afterwards, you can use it like any other color map.

```python
import matplotlib.pyplot as pl
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
```

![](https://github.com/benmaier/cividis/raw/master/sandbox/xmpl.png "")

## More examples

### Register cividis as default

This has to be done once in your `matplotlibrc` file, or you call the corresponding function from the package.

```python
import cividis
cividis.make_default()

 ...

pl.imshow(Z)
```

Will give equal results to the above.

### Get an array of N cividis colors


```python
import cividis
color_list = cividis.get_colors(10,n_start=2,n_end=200)
```

Where the function is implemented as

```python
def get_colors(N, n_start=0, n_end=255):
    """Get a color array of `N` entries, where the `N` entries
    are taken at equidistance from the `cividis` array between
    `n_start` and `n_end`"""

    indices = np.linspace(n_start, n_end, N)
    indices = np.array(indices, dtype=int)
    return cividis[indices]
```


