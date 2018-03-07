"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Colleen Fulton.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################


import rosegraphics as rg
window = rg.TurtleWindow()

henry = rg.SimpleTurtle('turtle')
henry.pen = rg.Pen('light pink', 5)
henry.speed = 10

size = 300
for k in range(13):

    henry.draw_square(size)

    henry.pen_up()
    henry.right(45)
    henry.forward(10)
    henry.left(45)

    henry.pen_down()
    size = size - 12

luke = rg.SimpleTurtle('turtle')
luke.pen = rg.Pen('black', 5)
luke.speed = 10

size = 300
for k in range(13):

    luke.draw_square(size)

    luke.pen_down()
    luke.left(45)
    luke.backward(10)
    luke.right(45)

    luke.pen_down()
    size = size - 12

window.close_on_mouse_click()


