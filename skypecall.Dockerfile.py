#!/usr/bin/env python
try:
    from pydocker import DockerFile
except ImportError:
    from urllib.request import urlopen
    exec(urlopen('https://raw.githubusercontent.com/jen-soft/pydocker/master/pydocker.py').read())

import os
import sys
import logging

logging.getLogger('').setLevel(logging.INFO)
logging.root.addHandler(logging.StreamHandler(sys.stdout))

d = DockerFile(base_img='selenium/standalone-chrome', name='astupidbear/skypecall:latest')

d.RUN = 'sudo apt-get update && sudo apt-get install -y python3 python3-pip && pip3 install selenium'

d.RUN = 'wget -O ~/skypecall.py https://raw.githubusercontent.com/AStupidBear/skypecall/master/skypecall.py'

d.ENTRYPOINT = ['python3', '/home/seluser/skypecall.py']

d.build_img()

os.system('docker run -it --rm -v /dev/shm:/dev/shm astupidbear/skypecall:latest ' + ' '.join(sys.argv[1:]))