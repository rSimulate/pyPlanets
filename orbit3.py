## This can be run from a python shell by typing
##    import orbit
## or from unix command line with
##    python orbit.py
from visual import *

## By default, "visual" creates a 3-D object called scene
scene.autoscale=0
scene.range=2

## create three objects, set their initial
##   position, radius, color, and other
##   properties: mass, momentum("p")
giant = sphere()
giant.pos = vector(-0.201,0.020,0)
giant.radius = 0.075 ; giant.color = color.red
giant.mass = 1
giant.p = vector(0, 0.051, -0.01) * giant.mass

dwarf = sphere()
dwarf.pos = vector(1.5,0,0)
dwarf.radius = 0.056 ; dwarf.color = color.yellow
dwarf.mass = 0.125
dwarf.p = -giant.p

moon = sphere()
moon.pos = vector(0,0.5,0.5)
moon.radius = 0.04 ; moon.color = color.cyan
moon.mass = 0.00125
moon.p = 0.035 * dwarf.p

## tweak initial condition so that total momentum is zero
giant.p -= moon.p

## create 'curve' objects showing where we've been
for a in [giant, dwarf, moon]:
  a.orbit = curve(color=a.color, radius = 0.01)


def pstep( giant, dwarf ):
  dist = dwarf.pos - giant.pos
  force = G * giant.mass * dwarf.mass * dist / mag(dist)**3
  giant.p = giant.p + force*dt
  dwarf.p = dwarf.p - force*dt
  dist = dwarf.pos - giant.pos

dt = 0.01
G = 1
while 1:
  ## set the picture update rate (100 times per second)
  rate(100)

  pstep( giant, dwarf )
  pstep( giant, moon )
  pstep( moon, dwarf )

  for a in [giant, dwarf, moon]:
    a.pos = a.pos + a.p/a.mass * dt
    a.orbit.append(pos=a.pos)

## For an intro to visual python see
## http://wiki.aims.ac.za/mediawiki/index.php/Vpython:Getting_Started
