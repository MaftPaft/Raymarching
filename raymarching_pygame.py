"""
RAYMARCHING ALGORITHM
"""
import pygame as pg
from math import *
pg.init()
w,h=800,600
win=pg.display.set_mode((w,h))
# player positions
px,py=w/2,h/2
# objects
balls=[[w/2,h/4,50]]
# ray distance cap
cap=1000
# player direction
angle=0
# loop
run=True
while run:
    # mouse data
    mx,my=pg.mouse.get_pos()
    mp=pg.mouse.get_pressed()
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run=False
        if i.type == pg.KEYDOWN:
            if i.key == pg.K_SPACE:
                ## Places objects when space key is pressed
                balls.append([mx,my,50])
    win.fill((0,0,0))
    # mouse clicks (changes direction/sets player position)
    if mp[0]:
        angle=atan2(mx-px,my-py)
    elif mp[2]:
        px,py=mx,my
    
    # find nearest object
    balls.sort(key=(lambda x: hypot(x[0]-px,x[1]-py)))
    c=balls[0]
    rad=hypot(c[0]-px,c[1]-py)-c[2]
    # radius is the distance between the point and nearest object
    rays=[[px,py,rad]]
    # loop until object is hit or reaches the distance limit
    while hypot(rays[-1][0]-px,rays[-1][1]-py)<=cap and rad>1:
        rx,ry=sin(angle)*rad+rays[-1][0],cos(angle)*rad+rays[-1][1]
        balls.sort(key=(lambda x: hypot(x[0]-rx,x[1]-ry)))
        c=balls[0]
        rad=hypot(c[0]-rx,c[1]-ry)-c[2]
        rays.append([rx,ry,rad])

    # drawing objects and rays
    for b in balls:
        pg.draw.circle(win,(255,255,255),(b[0],b[1]),b[2],1)
    for i, r in enumerate(rays):
        pg.draw.circle(win,(0,255,0),(r[0],r[1]),r[2],1)
        if i >= 1:
            pg.draw.line(win,(255,0,0),(rays[i-1][0],rays[i-1][1]),(rays[i][0],rays[i][1]))
    
    
    pg.display.update()
