import turtle

turtle.left(90) 

def draw(rzm, glb):    
  if glb > 0: 
    turtle.forward(rzm) 
    turtle.right(rzm)
    draw(0.75 * rzm, glb-1) 
    turtle.left(rzm * 2)
    draw(0.75 * rzm, glb-1) 
    turtle.right(rzm) 
    turtle.right(180)
    turtle.forward(rzm) 
    turtle.left(180)   

draw(90, 6)
