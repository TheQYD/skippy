#!/usr/bin/python

import sys
import telnetlib
import yaml
import argparse
from lib import ds1054z

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
  parser = argparse.ArgumentParser( version='lxi-cmd.py 1.0')
  subparsers = parser.add_subparsers(help='commands')
  
  # Looping through arguments.
  for arg in config:
    arg_data = config[arg]
    arg_help = arg_data['help']
    positional_argument = subparsers.add_parser(arg, help=arg_help)
    
    # Processing args.
    flags = arg_data['flags']
    if flags is not None:
      for flag in flags:
        flag_help = flags[flag]['help'] 
        flag = '--' + flag
        positional_argument.add_argument(flag, action='store', nargs='*', help=flag_help)
        positional_argument.set_defaults(__subparser__=arg)
  return parser.parse_args()

if __name__ == '__main__':
  config = yaml.load(open('config/rigol-ds1054z.yaml'))
  args = ProcessArgs(config)
  module = args.__subparser__.capitalize()
  args_dict = vars(args)
  for flag in args_dict:
    if args_dict[flag] is not None:
      print module, flag, args_dict[flag] 
