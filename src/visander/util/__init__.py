import numpy
from visander.core import Entity
from visander.color import get_intensity

class Filterer(object):
  '''
  Just a simple filterer that takes in some kind of callable and weeds out
  the images which evaluate to False by the callable.
  '''
  
  def __init__(self, source, filter_):
    self.source = source
    self.filter_ = filter_
    
  @property
  def images(self):
    for image in self.source.images:
      if self.filter_(image):
        yield image

class ImageSampler(object):
  '''
  A class which splits a large image into multiple smaller
  images.  It takes as input an image source and acts as an
  image source itself.  If the input image is not evenly divisible by
  the sample width/height then some border pixels (lower and right border)
  will be discarded.
  '''
  
  def __init__(self, source, sample_width, sample_height):
    self.source = source
    self.sample_width = sample_width
    self.sample_height = sample_height
    self.index = 0
    
  def __sub_entities(self, entity):
    intensity_component = get_intensity(entity)
    if intensity_component is None:
      raise Exception("ImageSampler only works on entities with an intensity component")
    image = intensity_component.mat
    index = 0
    while True:
      vert_samples = image.shape[0] / self.sample_height
      horiz_samples = image.shape[1] / self.sample_width
      x_index = self.index % horiz_samples
      y_index = self.index / horiz_samples
      if y_index >= vert_samples:
        break
      x_pos = x_index * self.sample_width
      y_pos = y_index * self.sample_height
      self.index += 1
      image_sample = numpy.copy(image[y_pos:y_pos+self.sample_height,x_pos:x_pos+self.sample_width])
      yield Entity(type(intensity_component)(image_sample))    
    
  @property
  def entities(self):
    '''
    Goes through each image in the source and breaks it into sample_width x sample_height
    subimages and returns each subimage.
    '''
    for entity in self.source.entities:
      for sub_entity in self.__sub_entities(entity):
        yield sub_entity
