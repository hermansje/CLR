from setuptools import setup

setup(name='keras_clr',
      version='0.1',
      description='Cyclic learning rate callback for Keras.',
      url='http://github.com/bckenstler/CLR',
      author='Brad Kenstler',
      license='MIT',
      py_modules=['clr_callback'],
      install_requires=[
            'keras>=2.0.0',
            'numpy'
      ],
      zip_safe=False)
