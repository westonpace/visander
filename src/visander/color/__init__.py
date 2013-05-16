import cv2

class GrayscaleIntensityComponent(object):
  
  def __init__(self, mat):
    self.mat = mat
    
class BgrIntensityComponent(object):
  
  def __init__(self, mat):
    self.mat = mat
    
def ensure_grayscale(entity):
  if entity.has_component(GrayscaleIntensityComponent):
    return
  color_component = entity.get_component(BgrIntensityComponent)
  if color_component is None:
    raise Exception("ensure_grayscale was called on an entity but the entity did not have grayscale or color intensities")
  intensity_mat = cv2.cvtColor(color_component.mat, cv2.COLOR_BGR2GRAY)
  entity.add_component(GrayscaleIntensityComponent(intensity_mat))
  
def get_intensity(entity):
  if entity.has_component(BgrIntensityComponent):
    return entity.get_component(BgrIntensityComponent)
  elif entity.has_component(GrayscaleIntensityComponent):
    return entity.get_component(GrayscaleIntensityComponent)
  return None