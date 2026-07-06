import os  
os.environ['ConEmuANSI'] = '1' # Stops blessed terminal probe. Might cause problems later!

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
if hasattr(sys.__stdout__, 'reconfigure'):
    sys.__stdout__.reconfigure(encoding='utf-8')
if hasattr(sys.__stderr__, 'reconfigure'):
    sys.__stderr__.reconfigure(encoding='utf-8')

from chemstractor.AI import AI
AI() # Instantiate the singleton

from chemstractor.commands.commands import cli

if __name__ == '__main__':
    cli()
