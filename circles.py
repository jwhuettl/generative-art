import time


def setup():
  size(800, 800)

  ellipseMode(CENTER)
  colorMode(RGB)
  background(225, 225, 225)
  noLoop()

palette = [[247, 197, 159],
           [42, 50, 75],
           [118, 123, 145],
           [199, 204, 219],
           [255, 299, 238]]

def drawEllipse(x, y, w, h):
  # draws ellipses

  ec = palette[int(random(0, 4))]

  fill(ec[0], ec[1], ec[2])
  noStroke()
  ellipse(x, y, w, h)

  # creates smaller circles within original
  if (w >= 20):
    minus = random(0, 30)
    drawEllipse(x, y, w - minus, h - minus)
  else:
    return

def draw():

    y = 100

    while (y < height):
        x = 100
        while (x < width):
            drawEllipse(x, y, 200, 200)
            x += 200
        y += 200

    name = "circles"+str(int(time.time()))
    save("images/"+name)
