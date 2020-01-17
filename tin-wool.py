import time

def setup():
  size(1000, 1000)
  background(0)

  stroke(210)
  strokeWeight(2)
  curveTightness(3)
  noFill()
  noLoop()

def pointGen(x, y, d):
  # generates a point on a circle

  angle = random(0, 6.28)
  px = cos(angle) * (d / 2)
  py = sin(angle) * (d / 2)

  coord = [x + int(px), y + int(py)]
  return coord

def distCalc(one, two):
  # calculates dist between two points

  xDist = abs(one[0] - two[0])
  yDist = abs(one[1] - two[1])

  dist = xDist + yDist

  return dist

def drawWool(x, y, d, t):
  # drawing wool

  for i in range(t):

    one = pointGen(x, y, d)
    two = pointGen(x, y, d)
    dist = distCalc(one, two)

    if (dist < (d / 3)):
      one = pointGen(x, y, d)
      two = pointGen(x, y, d)
      dist = distCalc(one, two)

    line(two[0], two[1], one[0], one[1])


def draw():

  diameter = 150

  y = 150
  while (y < height):
    x = 150
    while (x < width):
      drawWool(x, y, diameter, int(random(7, 17)))
      x += 225
    y += 225

  name = "tin_wool" + str(int(time.time()))
  save(name)