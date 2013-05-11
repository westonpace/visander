class FocusGroundTruth(object):
  '''
  A component that represents focus ground truth information.  This ground
  truth information is stored as a double named scale which represents the
  degree to which something is focused.  Although it does not specifically
  mean this it can be helpful to think of this as similar to the scale of a
  Gaussian.
  '''
  
  def __init__(self, scale):
    self.scale = scale
    
class FocusCorrelator(object):
  
  def __init__(self):
    pass