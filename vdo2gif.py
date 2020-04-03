#!bin/python3
import argparse
from moviepy.editor import *

argparser = argparse.ArgumentParser()

argparser.add_argument('inputdir',type=str, help='Input directory for video file')
argparser.add_argument('outputdir',type=str,help='Output directory for gif file')
argparser.add_argument('-c', '--cut', nargs=2, action='store', dest='time', metavar=('hr:min:sec','hr:min:sec'), help='the video will be trimmed within the given timeline and convert to gif when specify.(Format: 0:0:0)')

args = argparser.parse_args()

startTime = list()
endTime = list()
banner = """
created by -
     _   __                       ___  ___            _ _____ _           
    | | / /                       |  \/  |           | |_   _| |          
    | |/ /  __ _ _   _ _ __   __ _| .  . |_   _  __ _| |_| | | |__  _   _ 
    |    \ / _` | | | | '_ \ / _` | |\/| | | | |/ _` | __| | | '_ \| | | |
    | |\  \ (_| | |_| | | | | (_| | |  | | |_| | (_| | |_| | | | | | |_| |
    \_| \_/\__,_|\__,_|_| |_|\__, \_|  |_/\__, |\__,_|\__\_/ |_| |_|\__,_|
                              __/ |        __/ |                          
                             |___/        |___/                           

github: https://github.com/kmt29
"""
clip = None

if args.time != None:
    startTime = args.time[0].split(':',3)
    endTime = args.time[1].split(':',3)
    if len(startTime) > 3 or len(endTime) > 3:
        argparser.print_help()
        sys.exit()
    clip = (VideoFileClip(args.inputdir).subclip((float(startTime[0]),float(startTime[1]),float(startTime[2])),(float(endTime[0]),float(endTime[1]),float(endTime[2]))))
    
if args.time == None:
    clip = VideoFileClip(args.inputdir)

print(banner)
clip.write_gif(args.outputdir+'.gif')
  
