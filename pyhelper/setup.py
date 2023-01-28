from setuptools import setup, find_packages

setup(
  name="Py Helper",
  version="1.0",
  py_modules="info",
  packages=find_packages(),
  install_requires=[
    'click',
    'rich',
    'pytube'
  ],
  entry_points='''
  [console_scripts]
  pyhelper=commands:cli
  '''
)