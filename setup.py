from setuptools import setup, find_packages

setup(name='pymel',
      version='1.0.7',
      package_dir = {'': 'lib'},
      packages=find_packages('lib', exclude='docs'),
      py_modules=['shiboken']
     )

