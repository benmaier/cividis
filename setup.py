from setuptools import setup

setup(name='cividis',
      version='0.0.1',
      description="Register the color map `cividis` by Nunez et al. in matplotlib.",
      url='https://www.github.com/benmaier/bfmplot',
      author='Benjamin F. Maier',
      author_email='bfmaier@physik.hu-berlin.de',
      license='MIT',
      packages=['cividis'],
      install_requires=[
          'numpy>=1.14',
          'matplotlib>=2.2',
      ],
      zip_safe=False)
