#!C:\Users\Leonardo\PycharmProjects\StarWars-API\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'jsondiff==1.2.0','console_scripts','jdiff'
__requires__ = 'jsondiff==1.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('jsondiff==1.2.0', 'console_scripts', 'jdiff')()
    )
