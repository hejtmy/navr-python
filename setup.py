from setuptools import setup

setup(name='navr',
      version='0.1',
      description='Navigation related analytical and graphing functions',
      url='http://github.com/hejtmy/navr-python',
      author='Lukáš "hejtmy" Hejtmánek',
      author_email='hejtmy@gmail.com',
      license='MIT',
      packages=['navr'],
      install_requires=[
            'pandas',
            'numpy>=1.16.0',
            'matplotlib',
      ],
      zip_safe=False)