import os
import cv2
from visander.util import ImageSampler

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
  def images(self):
    '''
    A generator function which returns all of the images in this image source.
    '''
    for root,_,filenames in os.walk(self.root_dir):
      for filename in filenames:
        _,extension = os.path.splitext(filename)
        if extension.lower() in self.image_extensions:
          image = cv2.imread(os.path.join(root,filename))
          yield image 

image_source = DirectoryBasedImageSource('/Users/Pace/git/westonpace/visander/resource/images')
for image in ImageSampler(image_source, 20, 20).images:
  #print image
  cv2.namedWindow('foobar')
  cv2.imshow('foobar',image)
  cv2.waitKey()