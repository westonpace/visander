
class Entity(object):

  def __init__(self, *args):
    self.__components = list(args)
    
  def get_component(self, component_type):
    components = self.get_components(component_type)
    if len(components) > 1:
      raise Exception("Multiple components of type {0} found on entity {1}".format(component_type, self))
    if components:
      return components[0]
    else:
      return None
      
  def get_components(self, component_type=None):
    if component_type is None:
      return self.__components
    return [component for component in self.__components if isinstance(component, component_type)]

  def has_component(self, component_type):
    return self.get_component(component_type) is not None

  def add_component(self, component):
    self.__components.append(component)
