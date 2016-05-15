#!/usr/bin/python

import sys
import telnetlib
import yaml
import argparse
from lib import ds1054z
import inspect

def ConnectToDevice(device):
  connected_device = telnetlib.Telnet(device, 5555)
  return connected_device

def WriteCommand(connected_device, command):
  command = ":" + str(command) + "\n"
  connected_device.write(command)

def ReadResponse(connected_device):
  device_response = connected_device.read_all()
  return device_response

def DisconnectFromDevice(connected_device):
  connected_device.close()

def ProcessArgs(config):
  parser = argparse.ArgumentParser( version='skippy.py 1.0')
  subparsers = parser.add_subparsers(help='commands')

  # Looping through arguments.
  for arg in config:
    arg_data = config[arg]
    arg_help = arg_data['help']
    command = subparsers.add_parser(arg, help=arg_help)
    command.add_argument('identifier', nargs='?')
    command.set_defaults(__subparser__=arg)

    # Processing args.
    flags = arg_data['flags']
    if flags is not None:
      for flag in flags:
        flag_help = flags[flag]['help']
        flag = '--' + flag
        command.add_argument(flag, action='store', nargs='*', help=flag_help)
  return parser.parse_args()

def BuildCommand(config):
  config = yaml.load(open(config))
  args = ProcessArgs(config)


  # Setting up defaults.
  command = args.__subparser__.capitalize()
  identifier = args.identifier
  flag = "Default"
  value = None
  scpi_command = None

  # Converting args to dict and deleting temporary items.
  args_dict = vars(args)
  args_dict.pop('__subparser__')
  args_dict.pop('identifier')

  for element in args_dict:
    if args_dict[element] is not None:
       value = args_dict[element]
       flag = element.capitalize()

  command_call = getattr(ds1054z, command)
  flag_call = getattr(command_call, flag)
  scpi_command = flag_call(command, identifier, flag, value)

  print scpi_command

if __name__ == '__main__':

  argument_data = {}
  command_objects = inspect.getmembers(ds1054z, predicate=inspect.isclass)
  for command_data in command_objects:
    flag_objects = inspect.getmembers(command_data[1], predicate=inspect.ismethod)
    flags = [flag_data[0] for flag_data in flag_objects]
    argument_data[command_data[0]] = flags

  print argument_data


  #BuildCommand('config/rigol-ds1054z.yaml')
