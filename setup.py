from setuptools import setup

setup(name='cividis',
      version='0.0.1',
      description="Register `cividis` with matplotlib, a color map optimized for color vision deficiency, as published in Nuñez, et al. (2018), PLoS ONE 13(7): e0199239 .",
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
