def setup():
    size(1000, 1000)
    background(244, 135, 113)
    frameRate(10)


def draw_curve(x, y, count):
    xPos = x
    yPos = y
    x2Pos = xPos + random(-200, 200)
    y2Pos = yPos + random(-200, 200)
    x3Pos = x2Pos + random(-200, 200)
    y3Pos = y2Pos + random(-200, 200)
    x4Pos = x3Pos + random(-200, 200)
    y4Pos = y3Pos + random(-200, 200)

    colorMode(HSB)

    noFill()
    curveTightness(random(-10, 10))
    stroke(184, random(0, 100), random(0, 100), random(10, 255))
    strokeWeight(random(1, 5))
    curve(xPos, yPos, x2Pos, y2Pos, x3Pos, y3Pos, x4Pos, y4Pos)

    count += random(0, 10)

    if (count > 20):
        return

    draw_curve(x4Pos, y4Pos, count)

def mousePressed():
    noLoop()

def draw():

    draw_curve(random(0, 1000), random(0, 1000), 0)
