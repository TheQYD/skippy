#!/usr/bin/python

def FormatSkippyCommand(command, identifier, flag, value):

  # If it's an IEEE command, build it and return.
  if flag == "Default":
    scpi_command = ":" + command
    return scpi_command.upper()

  # Attach command identifiers.
  if identifier is not None:
    command = command + identifier

  # Build the actual command.
  scpi_command = ":" + command + ":" + flag
  if value is not None:
    scpi_command = scpi_command + " " + value[0]
  else:
    scpi_command = scpi_command + "?"
  return scpi_command.upper()
