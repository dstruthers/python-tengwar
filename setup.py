from setuptools import setup

setup(name='tengwar',
      version='1.0.0',
      author='Darren M. Struthers',
      author_email='dstruthers@gmail.com',
      py_modules=['tengwar'],
      description='Tengwar transliteration library',
      license='MIT',
      install_requires=[
          'bidict',
          'parsing'
      ],
      tests_require=['pytest'],
      dependency_links=['https://github.com/dstruthers/python-parsing/tarball/master#egg=parsing']
      )
