# Alex Miller
# Used to quick fix database issues

import openpyxl as xl
import sys, random, re

def main(): # main method
    wb = xl.load_workbook('moviedb.xlsx')
    sheet = wb['Movies']

    for i in range(2, sheet.max_row+1):
        ycell = 'B' + str(i)
        lcell = 'D' + str(i)
        yvalue = sheet[ycell].value
        lcell = sheet[lcell].value
        if yvalue.endswith('m'):
            length = MtoH(yvalue)
            sheet[ycell] = 'N/A'
            sheet[lcell] = length


def MtoH(v):
    v = v[:len(v)-1]
    v = int(v)
    h = 0
    while v >= 60:
        h += 1
        v -= 60
    
    if h == 0:
        return '{} m'.format(v)
    elif v == 0:
        return '{} H'.format(h)
    else:
        return '{} H {} m'.format(h, v)



