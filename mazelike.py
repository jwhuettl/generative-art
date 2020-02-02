def setup():
  size(1000, 1000)
  background(189, 87, 87)

  stroke(235, 227, 190)
  strokeWeight(1.5)
  noLoop()


def squarePattern(x, y, step, size):
  # draws a square with pattern at x y w/ size

  for i in range(x, x + size, step):
    for j in range(y, y + size, step):
      r = random(0, 1)

      if r > 0.5:
        line(i, j, i + step, j + step)
      else:
        line(i + step, j, i, j + step)


def draw():

  step = 5
  padding = 15
  size = 970

  x = padding
  while x < (width - padding):
    y = padding
    while y < (height - padding):
      squarePattern(x, y, step, size)
