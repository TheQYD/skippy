class Math(object):
  
  def Operator(self, arg, flag, value=None):
    scpi_command = arg + ':' + flag + value[0]
    return scpi.upper()
    
    

