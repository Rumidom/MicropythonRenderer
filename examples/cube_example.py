import random
from machine import Pin, SPI
import gc9a01
import framebuf
import fontlib
from micropython_rederer import loadObj
import time

spi = SPI(0, baudrate=60000000, sck=Pin(18), mosi=Pin(19))
tft = gc9a01.GC9A01(
    spi,
    dc=Pin(21, Pin.OUT),
    cs=Pin(17, Pin.OUT),
    reset=Pin(20, Pin.OUT),
    #backlight=Pin(14, Pin.OUT),
    rotation=0)

screen_width = 240
screen_height = 240
bytebuffer = bytearray(screen_width * screen_height * 2) #two bytes for each pixel
fbuf = framebuf.FrameBuffer(bytebuffer, screen_width, screen_height, framebuf.RGB565)
IBM_font = fontlib.font("IBM BIOS (8,8).bmp")
cube = loadObj('cube.obj')
white_c = gc9a01.color565((255,255,255))

i = 0
cube.pos = (0,0,3)
for j in range(360):
    i += 1
    cube.ang = (i,j)
    fbuf.fill(0)
    start_time = time.ticks_ms()
    cube.render(fbuf,(screen_width,screen_height))
    render_time = time.ticks_ms()-start_time
    fontlib.prt("FPS: "+str(round(1/(render_time/1000),4)),30,40,0,fbuf,IBM_font,invert = False,color=white_c)
    tft.blit_buffer(bytebuffer,0,0,screen_width,screen_height)
    
