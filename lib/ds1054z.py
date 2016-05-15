from utilities import formatter


class Autoscale(object):
  """Help: Auto-adjust waveform scale."""

  @classmethod
  def Default(cls, command, identifier, flag, value):
    """Help: Default flag for this command"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Clear(object):
  """Help: Clear all waveforms on screen."""

  @classmethod
  def Default(cls, command, identifier, flag, value):
    """Help: Default flag for this command"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Run(object):
  """Help: Start oscilloscope."""
  @classmethod
  def Default(cls, command, identifier, flag, value):
    """Help: Default flag for this command"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Stop(object):
  """Help: Stop the oscilliscope"""

  @classmethod
  def Default(cls, command, identifier, flag, value):
    """Help: Default flag for this command"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Single(object):
  """Help: Set single trigger mode."""
  @classmethod
  def Default(cls, command, identifier, flag, value):
    """Help: Default flag for this command"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Tforce(object):
  """Help: Generate a trigger signal forcefully."""

  @classmethod
  def Default(cls, command, identifier, flag, value):
    """Help: Default flag for this command"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Acquire(object):
  """Help: Set and get values that affect signal acquisition."""

  @classmethod
  def Average(cls, command, identifier, flag, value):
    """Help: Lowers noise and increases vertical resolution."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Mdepth(cls, command, identifier, flag, value):
    """Help: Set or query the memory depth of the oscilloscope."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Type(cls, command, identifier, flag, value):
    """Help: Set or query the acquisition mode of the oscilloscope."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Srate(cls, command, identifier, flag, value):
    """Help: Query the current sample rate."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Calibrate(object):
  """Help: Start and stop self calibration."""

  @classmethod
  def Quit(cls, command, identifier, flag, value):
    """Help: Exit self-calibration."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Start(cls, command, identifier, flag, value):
    """Help: Starts self-calibration."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Channel(object):
  """Help: Set or query vertical parameters of analog channels."""

  @classmethod
  def Bwlimit(cls, command, identifier, flag, value):
    """Help: Set or query the bandwidth limit for a channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Coupling(cls, command, identifier, flag, value):
    """Help: Set or query the coupling mode of the specified channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Display(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Invert(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the inverted channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Offset(cls, command, identifier, flag, value):
    """Help: Set or query the vertical offset of a channel"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Range(cls, command, identifier, flag, value):
    """Help: Set or query the vertical range of a specified channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Tcal(cls, command, identifier, flag, value):
    """Help: Set or query the delay calibration time of a channel"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Scale(cls, command, identifier, flag, value):
    """Help: Set or query the vertical scale of a channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Probe(cls, command, identifier, flag, value):
    """Help: Set or query the probe ratio of a channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Units(cls, command, identifier, flag, value):
    """Help: Set or query the amplitude unit of a channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Vernier(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the adjustment of the y of a channel"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Cursor(object):
  """Help: Measure X-axis and Y-axis value of a waveform."""

  @classmethod
  def Mode(cls, command, identifier, flag, value):
    """Help: Set or query the cursor measurement mode."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Manual(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Track(cls, command, identifier, flag, value):
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Auto(cls, command, identifier, flag, value):
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Xy(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Decoder(object):
  """Help: Execute decoding settings and operations."""

  @classmethod
  def Mode(cls, command, identifier, flag, value):
    """Help: Set or query the decoder type. """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Display(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the decoder."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Format(cls, command, identifier, flag, value):
    """Help: Set or query the bus display format."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Position(cls, command, identifier, flag, value):
    """Help: Set or query the vertical position of the bus."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Threshold(cls, command, identifier, flag, value):
    """Help: Set or query the threshold level."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Config(cls, command, identifier, flag, value):
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Uart(cls, command, identifier, flag, value):
    """Help: UART commands used to set the RS232 decoding parameters"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Iic(cls, command, identifier, flag, value):
    """Help: IIC commands used to set decoding parameters. """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Spi(cls, command, identifier, flag, value):
    """Help: SPI commands used to set decoding parameters."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Parallel(cls, command, identifier, flag, value):
    """Help: Parallel commands used to set decoding parameters."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Display(object):
  """Help: Set waveform display properties."""

  @classmethod
  def Clear(cls, command, identifier, flag, value):
    """Help: Clear all the waveforms."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Data(cls, command, identifier, flag, value):
    """Help: Reads the bitmap data stream."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Type(cls, command, identifier, flag, value):
    """Help: Set or query the display mode of the waveform"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Grading(cls, command, identifier, flag, value):
    """Help: Set or query the persistence time."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Wbrightness(cls, command, identifier, flag, value):
    """Help: Set or query the waveform brightness."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Grid(cls, command, identifier, flag, value):
    """Help: Set or query the grid type."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Gbrightness(cls, command, identifier, flag, value):
    """Help: Set or query the brightness."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Etable(object):
  """Help: Set parameters to decode event table."""
  @classmethod
  def Disp(cls, command, identifier, flag, value):
    """Help: Enbable, disable, or query the decoding event table"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Format(cls, command, identifier, flag, value):
    """Help: Set or query the data display format of the event table."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def View(cls, command, identifier, flag, value):
    """Help: Set or query the display mode of the event table."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Column(cls, command, identifier, flag, value):
    """Help: Set or query the current column of the event table."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Row(cls, command, identifier, flag, value):
    """Help: Set or query the current row of the event table."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Sort(cls, command, identifier, flag, value):
    """Help: Set or query the display type of the decoding results."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Data(cls, command, identifier, flag, value):
    """Help: Read the current event table data."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Function(object):
  """Help: Set waveform recording and playback parameters."""

  @classmethod
  def Wrecord(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Wreplay(cls, command, identifier, flag, value):
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Iee(object):
  """Help: Common flags for querying or executing operations. """

  @classmethod
  def Cls(cls, command, identifier, flag, value):
    """Help: Clear all the event registers and clear the error queue."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Ese(cls, command, identifier, flag, value):
    """Help: Set or query the enable register to the standard."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Esr(cls, command, identifier, flag, value):
    """Help: Query and clear the event register."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Idn(cls, command, identifier, flag, value):
    """Help: Query for the ID string."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Opc(cls, command, identifier, flag, value):
    """Help: Query whether the current operation is finished."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Rst(cls, command, identifier, flag, value):
    """Help: Sets the oscilloscope default state."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Sre(cls, command, identifier, flag, value):
    """Help: Set or query the enable register."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Stb(cls, command, identifier, flag, value):
    """Help: Query the event register for the status byte register."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Tst(cls, command, identifier, flag, value):
    """Help: Perform a self-test and then return the self-test results."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Wai(cls, command, identifier, flag, value):
    """Help: Wait for the operation to finish."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class La(object):
  """Help: Perform related operations on digital channels."""
  @classmethod
  def Active(cls, command, identifier, flag, value):
    """Help: Set or query the current active channel or channel group."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Autosort(cls, command, identifier, flag, value):
    """Help: Set the auto ordering mode of the waveforms."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Digital(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Display(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query a  digital channel"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Pod(cls, command, identifier, flag, value):
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Size(cls, command, identifier, flag, value):
    """Help: Set or query the display size of the waveforms."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def State(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query LA function."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Tcalibrate(cls, command, identifier, flag, value):
    """Help: Set or query the delay calibration time of a channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Math(object):
  """Help: Perform related operations on digital channels. """
  @classmethod
  def Display(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the math operation function."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Operator(cls, command, identifier, flag, value):
    """Help: Set or query the operator of the math operation."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Source1(cls, command, identifier, flag, value):
    """Help: Set or query a source."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Source2(cls, command, identifier, flag, value):
    """Help: Set or query a source."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Lsource1(cls, command, identifier, flag, value):
    """Help: Set or query a source logic operation."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Lsource2(cls, command, identifier, flag, value):
    """Help: Set or query a source logic operation."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Scale(cls, command, identifier, flag, value):
    """Help: Set or query the vertical scale of the operation result."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Offset(cls, command, identifier, flag, value):
    """Help: Set or query the vertical scale of the operation result."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Invert(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the inverted operation result."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Reset(cls, command, identifier, flag, value):
    """Help: Adjusts the vertical scale of the operation result."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Fft(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Option(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Mask(object):
  """Help: Set and query pass/fail test parameters."""
  @classmethod
  def Enable(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the pass/fail test."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Source(cls, command, identifier, flag, value):
    """Help: Set or query the source of the pass/fail test."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Operate(cls, command, identifier, flag, value):
    """Help: Run, stop, or query the pass/fail test."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Mdisplay(cls, command, identifier, flag, value):
    """Help: Enable or disable the statistic information."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Sooutput(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query “Stop on Fail” function."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Output(cls, command, identifier, flag, value):
    """Help: Enable or disable the sound prompt."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def X(cls, command, identifier, flag, value):
    """Help: Set or query the horizontal adjustment parameter."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Y(cls, command, identifier, flag, value):
    """Help: Set or query the vertical adjustment parameter."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Create(cls, command, identifier, flag, value):
    """Help: Create the pass/fail test mask."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Passed(cls, command, identifier, flag, value):
    """Help: Query the number of passed frames in the pass/fail test."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Failed(cls, command, identifier, flag, value):
    """Help: Query the number of failed frames in the pass/fail test."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Total(cls, command, identifier, flag, value):
    """Help: Query the total number of frames in the pass/fail test."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Reset(cls, command, identifier, flag, value):
    """Help: Reset the total number of frames."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Measure(object):
  """Help: Set and query measurement parameters."""

  @classmethod
  def Source(cls, command, identifier, flag, value):
    """Help: Set or query the source of the current measurement parameter."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Counter(cls, command, identifier, flag, value):
    """Help: Set or query the source of the frequency counter."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Clear(cls, command, identifier, flag, value):
    """Help: Clear one or all of the last five measurement items enabled. """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Recover(cls, command, identifier, flag, value):
    """Help: Recover the measurement item which has been cleared."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Adisplay(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query, the all measurement function."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Amsource(cls, command, identifier, flag, value):
    """Help: Set or query the source(s) of the all measurement function."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Setup(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Statistic(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Item(cls, command, identifier, flag, value):
    """Help: Measure any waveform parameter of the specified source."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Reference(object):
  """Help: Set reference waveform parameters."""

  @classmethod
  def Display(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the REF function."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Enable(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the specified reference channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Source(cls, command, identifier, flag, value):
    """Help: Set or query the source of the current reference channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Vscale(cls, command, identifier, flag, value):
    """Help: Set or query the vertical scale of a reference channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Voffset(cls, command, identifier, flag, value):
    """Help: Set or query the vertical offset of a reference channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Reset(cls, command, identifier, flag, value):
    """Help: Reset the vertical scale and vertical offset of a ref channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Current(cls, command, identifier, flag, value):
    """Help: Select the current reference channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Save(cls, command, identifier, flag, value):
    """Help: Store the waveform of a reference channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Color(cls, command, identifier, flag, value):
    """Help: Set or query the display color of the current reference channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Source(object):
  """Help: Toggle or query output of a source channel."""


  @classmethod
  def Output(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the output of a source channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Frequency(cls, command, identifier, flag, value):
    """Help: Set or query the output frequency of the specified source channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Phase(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Function(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Voltage(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Pulse(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Mod(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Apply(cls, command, identifier, flag, value):
    """Help: Query the output configurations of a source channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class System(object):
  """Help: Set system parameters (sound, language, etc). """

  @classmethod
  def Autoscale(cls, command, identifier, flag, value):
    """Help: Enable or disable the AUTO key at the front panel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Beeper(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the beeper."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Error(cls, command, identifier, flag, value):
    """Help: Query and delete the last system error message."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Gpib(cls, command, identifier, flag, value):
    """Help: Set or query the GPIB address."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Language(cls, command, identifier, flag, value):
    """Help: Set or query the system language."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Locked(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query the keyboard lock function"""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Pon(cls, command, identifier, flag, value):
    """Help: Set or query the system configuration."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Option(cls, command, identifier, flag, value):
    """Help: Install a option."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Trace(object):
  """Help: Set waveform parameters of built-in signal sources."""

  @classmethod
  def Data(cls, command, identifier, flag, value):
    """Help: Download the floating point voltage values."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Timebase(object):
  """Help: Set horizontal parameters."""

  @classmethod
  def Delay(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Main(cls, command, identifier, flag, value):
    """Help: Set or query the main timebase offset."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Mode(cls, command, identifier, flag, value):
    """Help: Set or query the mode of the horizontal timebase."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Trigger(object):
  """Help: Set trigger system. """

  @classmethod
  def Mode(cls, command, identifier, flag, value):
    """Help: Select or query the trigger type."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Coupling(cls, command, identifier, flag, value):
    """Help: Select or query the trigger coupling type."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Status(cls, command, identifier, flag, value):
    """Help: Query the current trigger status."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Sweep(cls, command, identifier, flag, value):
    """Help: Set or query the trigger mode."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Holdoff(cls, command, identifier, flag, value):
    """Help: Set or query the trigger holdoff time."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Nreject(cls, command, identifier, flag, value):
    """Help: Enable, disable, or query noise rejection."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Edge(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Pulse(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Slope(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Video(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Pattern(cls, command, identifier, flag, value):
    """Help: Set or query the pattern of each channel in pattern trigger."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Duration(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Timeout(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Runt(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Windows(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Delay(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Shold(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Nedge(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Rs232(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Iic(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Spi(cls, command, identifier, flag, value):
    """Help: """
    return formatter.FormatSkippyCommand(command, identifier, flag, value)


class Waveform(object):
  """Help: Read waveform data and its related settings."""

  @classmethod
  def Source(cls, command, identifier, flag, value):
    """Help: Set or query the channel of which the waveform."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Mode(cls, command, identifier, flag, value):
    """Help: Set or query the reading mode."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Format(cls, command, identifier, flag, value):
    """Help: Set or query a return format."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Data(cls, command, identifier, flag, value):
    """Help: Read waveform data."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Xincrement(cls, command, identifier, flag, value):
    """Help: Query a time difference between two neighboring points."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Xorigin(cls, command, identifier, flag, value):
    """Help: Query the start time of waveform data."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Xreference(cls, command, identifier, flag, value):
    """Help: Query the reference time of a channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Yincrement(cls, command, identifier, flag, value):
    """Help: Query the waveform increment of a channel in the Y direction."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Yorigin(cls, command, identifier, flag, value):
    """Help: Query the vertical offset relative to the vertical reference."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Yreference(cls, command, identifier, flag, value):
    """Help: Query the vertical reference position of a channel."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Start(cls, command, identifier, flag, value):
    """Help: Set or query the start position of internal memory waveform."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Stop(cls, command, identifier, flag, value):
    """Help: Set or query the stop position of internal memory waveform."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)

  @classmethod
  def Preamble(cls, command, identifier, flag, value):
    """Help: Query and return all the waveform parameters."""
    return formatter.FormatSkippyCommand(command, identifier, flag, value)
