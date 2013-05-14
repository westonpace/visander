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
    
    
  def __new_image(self):
    self.index = 0
    
  @property
  def images(self):
    for image in self.image_source.images:
      sample = self.__get_next_sample(image)
      while sample is not None:
        yield sample
        sample = self.__get_next_sample(image)
      self.__new_image()
