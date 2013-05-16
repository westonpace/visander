import os
import cv2
from visander.util import ImageSampler
from visander.core import Entity
from visander.color import BgrIntensityComponent, GrayscaleIntensityComponent,\
  get_intensity, ensure_grayscale

class DirectoryBasedImageSource(object):
  '''
  An image source which is given a directory and will walk 
  all files in the directory and all subdirectory and read in and
  return those files which look like images (based on the file extension)
  '''
  
  def __init__(self, root_dir):
    self.root_dir = root_dir
    self.image_extensions = ['.jpg','.png','.bmp','.tif','.tiff']
    
  @property
  def entities(self):
    '''
    A generator function which returns all of the images in this image source.
    '''
    for root,_,filenames in os.walk(self.root_dir):
      for filename in filenames:
        _,extension = os.path.splitext(filename)
        if extension.lower() in self.image_extensions:
          image = cv2.imread(os.path.join(root,filename))
          if image.shape[2] == 3:
            yield Entity(BgrIntensityComponent(image))
          else:
            yield Entity(GrayscaleIntensityComponent(image)) 
