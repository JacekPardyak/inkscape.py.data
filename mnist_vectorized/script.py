from PIL import Image
import PIL.ImageOps
import tempfile
import subprocess
import shutil
import os
from IPython.display import SVG, display #, Image
import time
import pickle
with open('data.pickle', 'rb') as f:
     data = pickle.load(f)
     
(x_train, y_train), (x_test, y_test) = data
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)

#for ind in range(51000, 60000): # 60 000 
#  img = x_train[ind]
#  label = y_train[ind]
#  input = tempfile.NamedTemporaryFile(suffix='.bmp').name
#  img = Image.fromarray(img)
#  img = PIL.ImageOps.invert(img)
#  img.save(input)
#  output = tempfile.NamedTemporaryFile(suffix='.svg').name
#  subprocess.Popen(["potrace", input, "-b", "svg" , f"--output={output}"])
#  time.sleep(1)
#  file = '/mnist/' + str(label) + '/train/' + f'{str(label) + "_" + str(ind).zfill(5)}.svg'
#  os.makedirs(os.path.dirname(file), exist_ok=True)
#  shutil.copyfile(output, file)
#  print(label , ", " , file)

for ind in range(0, 10000): #10 000
  img = x_test[ind]
  label = y_test[ind]
  input = tempfile.NamedTemporaryFile(suffix='.bmp').name
  img = Image.fromarray(img)
  img = PIL.ImageOps.invert(img)
  img.save(input)
  output = tempfile.NamedTemporaryFile(suffix='.svg').name
  subprocess.Popen(["potrace", input, "-b", "svg" , f"--output={output}"])
  time.sleep(1)
  file = '/mnist/' + str(label) + '/test/' + f'{str(label) + "_" + str(ind + 60000).zfill(5)}.svg'
  os.makedirs(os.path.dirname(file), exist_ok=True)
  shutil.copyfile(output, file)
  print(label , ", " , file)
  
# zagnieżdzenie mnist/mnist + readme. redme na poziomie klass
# shutil.make_archive('svg_mnist', 'zip', '/mnist')
