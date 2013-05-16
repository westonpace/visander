'''
Created on May 15, 2013

@author: Pace
'''
from visander.color import ensure_grayscale, GrayscaleIntensityComponent
from visander.contrast import ContrastOperator
from visander.io import DirectoryBasedImageSource
from visander.util import ImageSampler
import cv2
import numpy.core.multiarray

image_source = DirectoryBasedImageSource('/Users/Pace/git/westonpace/visander/resource/images')
contrast_op = ContrastOperator()
contrasts = [contrast_op.calculate(entity) for entity in ImageSampler(image_source, 20, 20).entities]
print sorted(contrasts)
f = open('data.csv', mode='w+')
for contrast in contrasts:
  f.write("{0}\n".format(contrast))
f.close()
#for entity in ImageSampler(image_source, 20, 20).entities:
#  print contrast_op.calculate(entity)
#  ensure_grayscale(entity)
#  #print image
#  cv2.namedWindow('foobar')
#  cv2.imshow('foobar',entity.get_component(GrayscaleIntensityComponent).mat)
#  cv2.waitKey()