import numpy

class ImageSampler(object):
  '''
  A class which splits a large image into multiple smaller
  images.  It takes as input an image source and acts as an
  image source itself.  If the input image is not evenly divisible by
  the sample width/height then some border pixels (lower and right border)
  will be discarded.
  '''
  
  def __init__(self, image_source, sample_width, sample_height):
    self.image_source = image_source
    self.sample_width = sample_width
    self.sample_height = sample_height
    self.index = 0
    
  def __get_next_sample(self, image):
    vert_samples = image.shape[0] / self.sample_height
    horiz_samples = image.shape[1] / self.sample_width
    x_index = self.index % horiz_samples
    y_index = self.index / horiz_samples
    if y_index >= vert_samples:
      return None
    x_pos = x_index * self.sample_width
    y_pos = y_index * self.sample_height
    self.index += 1
    return numpy.copy(image[y_pos:y_pos+self.sample_height,x_pos:x_pos+self.sample_width])    
    
  @property
  def images(self):
    '''
    Goes through each image in the source and breaks it into sample_width x sample_height
    subimages and returns each subimage.
    '''
    for image in self.image_source.images:
      self.index = 0
      sample = self.__get_next_sample(image)
      while sample is not None:
        yield sample
        sample = self.__get_next_sample(image)
