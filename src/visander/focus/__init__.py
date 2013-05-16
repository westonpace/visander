import scipy.stats.pearsonr

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
    
class WholeImageFocusOperatorEvaluator(object):
  '''
  This is an evaluator for focus operators.  It evaluates operators which produce
  a single scale value for a given image as focus information.  It takes in a 
  stream of images that have FocusGroundTruth information attached to them.  
  These images are sent to the focus operator to determine the focus level.
  
  The ground truth values and the measured values are compared with Pearson correlation
  to determine the final score.  Scores range from -1 (this would indicate that
  the measure is backwards but highly accurate) to 0 (worst possible score, no
  additional information) to 1 (perfect).
  '''
  
  def __init__(self, focus_operator, test_image_source):
    ground_truths,observations = [],[]
    for test_image in test_image_source:
      ground_truths.append(test_image.get_component(FocusGroundTruth).scale)
      observations.append(focus_operator.get_focus(test_image_source))
    return scipy.stats.pearsonr(ground_truths,observations)