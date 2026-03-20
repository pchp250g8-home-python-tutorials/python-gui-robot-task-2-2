# --coding:utf-8--

from robot import *

while(is_cell_painted()):
    move_down()
    paint()
    move_up()
    move_right()
