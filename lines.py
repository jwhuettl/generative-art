import random

def setup():
  size(1000, 1000)

  colorMode(RGB)
  noLoop()
  strokeWeight(4)

def drawLine(coord):
  line(coord[0], coord[1], coord[2], coord[3])



def draw():
  x = 100
  y = 100

  while (y < (height - 100)):

    flip = random.randint(0, 1)

    if (flip == 1):
      coord = [x, y, width - 100, y]
      drawLine(coord)

    y += 20

  y = 100

  while ( x < (width - 100)):

    flip = random.randint(0, 1)

    if (flip == 1):
      coord = [x, y, x, height - 100]
      drawLine(coord)

    x += 20
