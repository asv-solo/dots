#!/bin/env python3

import os, sys
import subprocess
from PIL import Image, ImageFilter

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def take_screen():
    command='scrot /tmp/screen.png'
    subprocess.call(command.split())

def prepare(*args):
    command='convert -gamma 0.3 /tmp/screen.png /tmp/screen_dark.png'
    subprocess.call(command.split())
    im = Image.open('/tmp/screen_dark.png')
    im_out = im.filter(ImageFilter.GaussianBlur(radius=5))
    try:
        icon = Image.open('{0}/life.png'.format(get_script_path()))
        source_x, source_y = im_out.size
        icon_x, icon_y = icon.size
        im_out.paste(icon, 
                     (int(source_x*0.8 - icon_x/2), 
                      int(source_y*0.9 - icon_y/2)), 
                      icon)
        im_out.save('/tmp/screen_dark.png')
    except:
        im_out.save('/tmp/screen.png')

def lock():
    try:
        command='i3lock -u -i /tmp/screen_dark.png'
        subprocess.call(command.split())
        os.remove('/tmp/screen_img.png')
    except:
        command='i3lock -i /tmp/screen.png'
        os.remove('/tmp/screen.png')
    
if __name__ =='__main__': 
    take_screen()
    prepare()
    lock()         
