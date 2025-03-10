# Alex Miller
# maze creation for Speed Maze

import sys, os, shutil
from pathlib import Path 
from pyamaze import maze,agent
import random
import time
from PIL import ImageGrab

def main(i):

    p = Path.cwd()
    m = maze(12,8)
    randy = random.randint(1,2)
    randx = random.randint(1,8)
    if randx == 1:
        goalx = 1
    else:
        goalx = 12
    loop = random.randint(1,50)

    if goalx == 1:
        ax = 12
    else:
        ax = 1

    ay = random.randint(1,8)


    m.CreateMaze(goalx, randx, loopPercent=loop)
    a = agent(m)
    a.position = (ax,ay)
    m.run()
    
    region = (10,30,700,1035)
    ssimage = ImageGrab.grab(region)
    ssimage.save(str(i+1) + "-Maze.jpg")

    for file in p.glob("*.jpg"):
        shutil.move(file, "Mazes")

    i += 1
    print('Maze: ' + str(i))
    time.sleep(1)

if __name__ == '__main__':
    for i in range(200):
        main(i)

# https://towardsdatascience.com/a-python-module-for-maze-search-algorithms-64e7d1297c96