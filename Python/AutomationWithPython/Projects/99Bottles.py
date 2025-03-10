# Alex Miller
# print 99 to 0 bottles of milk

import sys, time

pause = 2
bottles = 99

while bottles > 1: # for when bottles are > 1
    print(bottles, ' bottles of milk on the wall')
    time.sleep(pause) # pause the program for 2 seconds?
    print(bottles, ' bottles of milk!')
    time.sleep(pause)
    print('take one down, pass it around')
    time.sleep(pause)
    bottles -= 1
    if bottles == 1: # fixing english
        print(bottles, ' bottle of milk on the wall')
    else:
        print(bottles, ' bottles of milk on the wall')
    print()
    time.sleep(pause)

if bottles == 1: # when there is only one bottle left (english will work better)
    print(bottles, ' bottle of milk on the wall')
    time.sleep(pause)
    print(bottles, ' bottle of milk!')
    time.sleep(pause)
    print('take it down, pass it around')
    time.sleep(pause)
    print('No more bottles of milk on the wall!')