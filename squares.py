def setup():
  size(1000, 1000)
  background(233, 204, 164)

  noFill()
  stroke(0, 0, 0)

  noLoop()

  rectMode(CENTER)


def drawSquare(x, y, size):
  # the rect function to draw squares

  strokeWeight((random(0.1, 2)))

  if size < 10:
    return


  rect(x, y, size, size)

  delta = random(5, size / 4)


  drawSquare(x, y, size - delta)


def draw():

  padding = 25
  size = 50

  x = 25 + (size / 2)
  while x < (width - 25):
    y = 25 + (size / 2)
    while y < (height - 25):
      drawSquare(x, y, size)

      y += size
    x += size


  
