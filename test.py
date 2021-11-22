import sys
import os
import logging
import argparse
APPDESC=""
def _addArguments(parser,installProcedures=None):
  parser.add_argument("-c","--checkpoint",help="Run only <cp>",metavar="<cp>")
  parser.add_argument("-y","--yes",help="Automatically answer yes to all questions",action="store_true")
  parser.add_argument("-b","--dbhost",help="Connect to database at hostname or IP address",metavar="<hostname or IP>")
  parser.add_argument("-r","--restore-backup",help="Absolut path to system backup tgz file",metavar="<system backup file>")
  #parser.add_argument("-t","--test",help="Run only post testing",action="store_true")
  parser.add_argument("-v","--version",help="Print version",action="store_true")
  parser.add_argument("-d","--debug",help="Run in debug mode",action="store_true")
  parser.add_argument("-l","--log-file",help="Run in debug mode",metavar="<log file>")
  parser.add_argument("-p","--print-install-procedures",help="Print a list of availilbe install procedures",action="store_true")
  parser.add_argument("-ip","--install-procedure",help="Install procedure to run",metavar="<install procedure>")
  parser.add_argument("--print-checkpoints",help="Print a list of availilbe checkpoints",action="store_true")
  parser.add_argument("--upload-config",help="Upload current file configuration to database",action="store_true")
  parser.add_argument("--download-config",help="Download current database configuration to file system",action="store_true")
#  parser.add_argument("--config-path",help="Base path for filesystem configuration",metavar="<path to configuration base dir>")
#  parser.add_argument("--config-schema-path",help="Base path for filesystem configuration schemas",metavar="<path to schemas base dir>")
  parser.add_argument("--init-db",help="Create initial database for tni",action="store_true")
def _parseArguments(argv):
  parser = argparse.ArgumentParser(description=APPDESC,add_help=True)
  _addArguments(parser)
  return parser.parse_args()

def main(argv):
  print('this is start')
  parsedArgs = _parseArguments(argv)
  print(parsedArgs, type(parsedArgs))
  if parsedArgs.upload_config:
     print('this is upload config')
     print('this is end')
if __name__ == "__main__":
  sys.exit(main(sys.argv))