import wget
import os
import zipfile


# wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')
# with zipfile.ZipFile('./dados.zip', 'r') as fp:
#   fp.extractall('./dados')

os.rename('ex05\dados\dow_jones_index.data', 'ex05\dados\dow_jones_index.csv')
  