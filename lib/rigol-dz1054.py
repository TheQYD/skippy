class Math(object):
  
  @classmethod
  def Operator(cls, arg, flag, value=None):
    scpi_command = arg + ':' + flag + value[0]
    return scpi.upper()
