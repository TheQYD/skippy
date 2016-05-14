class Math(object):

  @classmethod
  def Operator(cls, module, pos=None, flag=None, value=None):
    scpi_command = module + ':' + flag + value[0]
    return scpi_command.upper()


class Channel(object):

  @classmethod
  def Scale(cls, module, pos=None, flag=None, value=None):
    if pos is not None:
      module = module + pos
    scpi_command = module + ':' + flag + ':' + value[0]
    return scpi_command.upper()


class Channel1(Channel):
  pass

class Channel2(Channel):
  pass

class Channel3(Channel):
  pass

class Channel4(Channel):
  pass

