import cv2
import numpy as np
from scipy.stats import entropy
from visander.color import ensure_grayscale, GrayscaleIntensityComponent,\
  BgrIntensityComponent
import math

class ContrastOperator(object):
  
  def __calculate_entropy(self, histogram):
    result = 0
    histogram = np.ndarray.flatten(histogram)
    T = sum(histogram)
    for p in histogram:
      value = p * math.log(p,2) if p != 0 else 0 
      result += value
    entropy = math.log(T,2) - ((1.0/T) * result)
    return entropy / math.log(T,2)
  
  def calculate(self, entity):
    ensure_grayscale(entity)
    grayscale_image = entity.get_component(GrayscaleIntensityComponent).mat
    histogram = cv2.calcHist([grayscale_image], [0], None, [256], [0,256])
    entro = self.__calculate_entropy(histogram)
    return entro