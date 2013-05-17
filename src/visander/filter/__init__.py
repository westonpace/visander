import cv2
from visander.color import get_intensity
from visander.core import Entity

class GaussianFilter(object):
  
  def __init__(self, size, sigma=0):
    if size % 2 == 0:
      raise Exception("Cannot create a gaussian filter with even size")
    self.size = size
    self.sigma = sigma
    
  def filter(self, entity):
    intensity_component = get_intensity(entity)
    blurred_image = cv2.GuassianBlur(intensity_component.mat, self.size, self.sigma)
    return Entity(type(intensity_component)(blurred_image))
    