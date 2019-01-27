from vpython import *
#GlowScript 2.7 VPython
from vpython import *
#Totally accurate ball game
#RodrigoQueirós e MiguelMelo
#January 2019


scene.range = 40
scene.forward = vec(0,-1,-1)

scoreBoard = box(canvas = scene, size = 15*vec(2.4, 1.45, 0.1), texture = "https://i.imgur.com/3n1UAgM.png", color = color.white)
scoreBoard.pos = vec(0,10,-40)
bluePoints = 0
redPoints = 0
redScore = label(text = redPoints, pos = vec(-10, 6.5,-40), canvas = scene, opacity = 0, height = 40, color = color.red, box = False)
blueScore = label(text = bluePoints, pos = vec(10, 6.5, -40), canvas = scene, opacity = 0, height = 40, color = color.blue, box = False)

# p1 Movement booleans
playerOneMoveRight = False
playerOneMoveLeft = False
playerOneMoveForward = False
playerOneMoveBack = False

#p2 Movement booleans
playerTwoMoveForward = False
playerTwoMoveRight = False
playerTwoMoveLeft = False
playerTwoMoveBack = False

#Some vars
timecount = 0
battleroyale = False  

InicialXRed = -20
InicialZRed = 0
InicialXBlue = 20
InicialZBlue = 0

Inicial2XRed = -15
Inicial2ZRed = -80
Inicial2XBlue = 15
Inicial2ZBlue = -80



#red side of the field
redField = box()
redField.size = vec(40,1,60)
redField.pos= vec(-20,0,0)
redField.color = color.red


circleField = cylinder()
circleField.radius = 40
circleField.axis = vec(0,3,0)
circleField.pos= vec(0,-3,-80)
circleField.color = color.white
#blue side of the field
blueField = box()
blueField.size = vec(40,1,60)
blueField.pos= vec(20,0,0)
blueField.color = color.blue

##BALLS##

blueBall = sphere()
blueBall.radius = 1.5
blueBall.pos = vec(InicialXBlue,2,InicialZBlue)
blueBall.color = color.blue
blueBall.force = arrow(axis = vec(0,0,0), shaftwidth = 0.2, color = color.blue)
blueBall.vel = vec(0,0,0) #Movimento incial X Z
blueBall.mass = 1.5 # 2.0

redBall = sphere()
redBall.radius = 1.5
redBall.pos = vec(InicialXRed,2,InicialZRed)
redBall.color = color.red
redBall.force = arrow(axis = vec(0,0,0), shaftwidth = 0.2, color = color.red)
redBall.vel = vec(0,0,0) 
redBall.mass = 1.5

class pointerBluePos:
    x = blueBall.pos.x
    z = blueBall.pos.z

class pointerRedPos:
    x = redBall.pos.x
    z = redBall.pos.z
    
#Parede vermelha
rail1 = box()
rail1.texture = {'file': "https://i.imgur.com/ss5OcnL.jpg"}
rail1.size = vec(3,3,55)
rail1.color = color.red
rail1.pos = vec(-39,1,0)

rail3 = box()
rail3.color = color.yellow
rail3.size = vec(40,3,3)
rail3.pos = vec(-20,1,29)

rail4 = box()
rail4.color = color.yellow
rail4.size = vec(40,3,3)
rail4.pos = vec(-20,1,-29)

rail8 = box()
rail8.color = color.yellow
rail8.size = vec(3,3,10)
rail8.pos = vec(-5,1,-10)

rail9 = box()
rail9.color = color.yellow
rail9.size = vec(8,3,8)
rail9.pos = vec(-15,1,15)


rail13 = box()
rail13.color = color.yellow
rail13.size = vec(3,3,10)
rail13.pos = vec(-20,1,-24)

rail16 = box()
rail16.color = color.yellow
rail16.size = vec(3,3,10)
rail16.pos = vec(-15,1,0)

rail17 = box()
rail17.color = color.yellow
rail17.size = vec(5,3,3)
rail17.pos = vec(-8,1,-13.5)

#Parede Azul
rail2 = box()
rail2.texture = {'file': "https://i.imgur.com/ss5OcnL.jpg"}
rail2.size = vec(3,3,55)
rail2.color = color.blue
rail2.pos = vec(39,1,0)

rail5 = box()
rail5.color = color.green
rail5.size = vec(40,3,3)
rail5.pos = vec(20,1,29)

rail6 = box()
rail6.color = color.green
rail6.size = vec(40,3,3)
rail6.pos = vec(20,1,-29)

rail7 = box()
rail7.color = color.green
rail7.size = vec(3,3,10)
rail7.pos = vec(5,1,10)

rail10 = box()
rail10.color = color.green
rail10.size = vec(8,3,8)
rail10.pos = vec(15,1,-15)

rail14 = box()
rail14.color = color.green
rail14.size = vec(3,3,10)
rail14.pos = vec(20,1,24)

rail15 = box()
rail15.color = color.green
rail15.size = vec(3,3,10)
rail15.pos = vec(15,1,0)

rail18 = box()
rail18.color = color.green
rail18.size = vec(5,3,3)
rail18.pos = vec(8,1,13.5)


rail = []
rail.append(rail1, rail2, rail3, rail4,rail5,rail6,rail7,rail8,rail9,rail10,rail13,rail14,rail15,rail16,rail17,rail18)

ball = []
ball.append(blueBall, redBall)


ball[0].force = arrow(axis = vec(0,0,0), color = color.white)


game1  = button(bind = click, text = 'Brawl Ball')
def click():
    nonlocal battleroyale
    blueBall.pos.x = InicialXBlue
    blueBall.pos.z = InicialZBlue
    redBall.pos.x = InicialXRed
    redBall.pos.z = InicialZRed
    pointerBluePos.x = InicialXBlue
    pointerBluePos.z = InicialZBlue
    pointerRedPos.x = InicialXRed
    pointerRedPos.z = InicialZRed
    blueBall.vel.x = 0
    blueBall.vel.z = 0
    redBall.vel.x = 0
    redBall.vel.z = 0
    scene.range = 35
    scene.forward = vec(0,-1,-1)
    scene.center = vec(0, 0, 5)
    battleroyale = False  
    scoreBoard.pos.z = -40
    scoreBoard.pos.y = 10
    blueScore.pos.z = -40
    blueScore.pos.y = 6.5
    redScore.pos.z = -40
    redScore.pos.y = 6.5

game2  = button(bind = click1, text = 'Ball Royale')
def click1():
    nonlocal battleroyale
    blueBall.pos.x = Inicial2XBlue
    blueBall.pos.z = Inicial2ZBlue
    redBall.pos.x = Inicial2XRed
    redBall.pos.z = Inicial2ZRed
    pointerBluePos.x = Inicial2XBlue
    pointerBluePos.z = Inicial2ZBlue
    pointerRedPos.x = Inicial2XRed
    pointerRedPos.z = Inicial2ZRed
    blueBall.vel.x = 0
    blueBall.vel.z = 0
    redBall.vel.x = 0
    redBall.vel.z = 0
    scene.range = 40
    scene.center = vec(0, -1, -65)
    battleroyale = True
    circleField.radius = 40
    scoreBoard.pos.z = -140
    scoreBoard.pos.y = 4
    blueScore.pos.z = -140
    blueScore.pos.y = 1
    redScore.pos.z = -140
    redScore.pos.y = 1
    
reset  = button(bind = click2, text = 'Reset')
def click2():
    nonlocal battleroyale, bluePoints, redPoints
    blueBall.pos.x = InicialXBlue
    blueBall.pos.z = InicialZBlue
    redBall.pos.x = InicialXRed
    redBall.pos.z = InicialZRed
    pointerBluePos.x = InicialXBlue
    pointerBluePos.z = InicialZBlue
    pointerRedPos.x = InicialXRed
    pointerRedPos.z = InicialZRed
    blueBall.vel.x = 0
    blueBall.vel.z = 0
    redBall.vel.x = 0
    redBall.vel.z = 0
    scene.center = vec(0, 0, 0)
    scene.range = 40
    scene.forward = vec(0,-1,-1)
    bluePoints = 0
    redPoints = 0
    blueScore.text = bluePoints
    redScore.text = redPoints
    battleroyale = False  
    scoreBoard.pos.z = -40
    scoreBoard.pos.y = 10
    blueScore.pos.z = -40
    blueScore.pos.y = 6.5
    redScore.pos.z = -40
    redScore.pos.y = 6.5

## KEYS
def playerMovement(event):
    ## FUCK NON LOCAL SHIT MOFO PLS
    nonlocal playerOneMoveRight, playerOneMoveLeft, playerOneMoveForward, playerOneMoveBack, playerTwoMoveForward, playerTwoMoveBack, playerTwoMoveRight, playerTwoMoveLeft
    if event.which == 83:
        playerTwoMoveRight = True
    if event.which == 87:
        playerTwoMoveLeft = True
    if event.which == 68:
        playerTwoMoveForward = True
    if event.which == 65:
        playerTwoMoveBack = True

    if event.which == 37:
        playerOneMoveForward = True
    if event.which == 39:
        playerOneMoveBack = True
    if event.which == 40:
        playerOneMoveRight = True
    if event.which == 38:
        playerOneMoveLeft = True

def playerStopMovement(event):
    ## FUCK NON LOCAL SHIT MOFO PLS
    nonlocal playerOneMoveRight, playerOneMoveLeft, playerOneMoveForward, playerOneMoveBack, playerTwoMoveForward, playerTwoMoveBack, playerTwoMoveRight, playerTwoMoveLeft
    if event.which == 83:
        playerTwoMoveRight = False
    if event.which == 87:
        playerTwoMoveLeft = False
    if event.which == 68:
        playerTwoMoveForward = False
    if event.which == 65:
        playerTwoMoveBack = False

    if event.which == 37:
        playerOneMoveForward = False
    if event.which == 39:
        playerOneMoveBack = False
    if event.which == 40:
        playerOneMoveRight = False
    if event.which == 38:
        playerOneMoveLeft = False

scene.bind('click keydown', playerMovement)
scene.bind("click keyup", playerStopMovement)


##




elasticConst = 500
dt = 0.01
time = 0

while (True):
  rate(1/dt)
  
  
  
  if(battleroyale == True):
    timecount +=1
    if (timecount > 100):
        circleField.radius -= 1
        timecount =0
        
    
  
  for i in range(len(ball)):
    ball[i].vel = ball[i].vel + ( ball[i].force.axis * dt / ball[i].mass )
    ball[i].force.pos = ball[i].pos

  for i in range(len(ball)):
    for j in range(len(ball)):
      if (i == j): continue
      separation = ball[i].pos - ball[j].pos
      contactSeparation = separation.norm() * (ball[i].radius + ball[j].radius)
      if (separation.mag < contactSeparation.mag):
        elasticForce = - elasticConst * (separation - contactSeparation)
        ball[i].vel = ball[i].vel + (elasticForce / ball[i].mass) * dt
        
#Collision with walls
  for i in range(len(ball)):
     for j in range(len(rail)):
        #Collision redB with bluewall
        if(redBall.pos.x + redBall.radius >= 37 and redBall.pos.z - redBall.radius > -40):
            blueBall.pos.x = InicialXBlue
            blueBall.pos.z = InicialZBlue
            redBall.pos.x = InicialXRed
            redBall.pos.z = InicialZRed
            pointerBluePos.x = InicialXBlue
            pointerBluePos.z = InicialZBlue
            pointerRedPos.x = InicialXRed
            pointerRedPos.z = InicialZRed
            blueBall.vel.x = 0
            blueBall.vel.z = 0
            redBall.vel.x = 0
            redBall.vel.z = 0
            redPoints += 1
            redScore.text = redPoints
        #Collision blueB with redwall   
        if(blueBall.pos.x - blueBall.radius <= -37 and blueBall.pos.z - blueBall.radius > -40):
            blueBall.pos.x = InicialXBlue
            blueBall.pos.z = InicialZBlue
            redBall.pos.x = InicialXRed
            redBall.pos.z = InicialZRed
            pointerBluePos.x = InicialXBlue
            pointerBluePos.z = InicialZBlue
            pointerRedPos.x = InicialXRed
            pointerRedPos.z = InicialZRed
            blueBall.vel.x = 0
            blueBall.vel.z = 0
            redBall.vel.x = 0
            redBall.vel.z = 0
            bluePoints += 1
            blueScore.text = bluePoints
            
        #Collision balls with all walls
        if(ball[i].pos.x <= rail[j].pos.x + rail[j].size.x/2 and ball[i].pos.x >= rail[j].pos.x - rail[j].size.x/2 and ball[i].pos.z + ball[i].radius >= rail[j].pos.z - rail[j].size.z/2 and ball[i].pos.z - ball[i].radius <= rail[j].pos.z + rail[j].size.z/2):
            ball[i].vel.z = - ball[i].vel.z
            break
        if(ball[i].pos.z >= rail[j].pos.z - rail[j].size.z/2 and ball[i].pos.z <= rail[j].pos.z + rail[j].size.z/2 and ball[i].pos.x + ball[i].radius >= rail[j].pos.x - rail[j].size.x/2 and ball[i].pos.x - ball[i].radius <= rail[j].pos.x + rail[j].size.x/2):
            ball[i].vel.x = - ball[i].vel.x
            break
        
  ##Balls collision for point
  if (blueBall.pos.x-redBall.pos.x)**2 + (blueBall.pos.z-redBall.pos.z)**2 <= (blueBall.radius + redBall.radius)**2:
      if(redBall.pos.x > 0 and redBall.pos.z > -40):
        blueBall.pos.x = InicialXBlue
        blueBall.pos.z = InicialZBlue
        redBall.pos.x = InicialXRed
        redBall.pos.z = InicialZRed
        pointerBluePos.x = InicialXBlue
        pointerBluePos.z = InicialZBlue
        pointerRedPos.x = InicialXRed
        pointerRedPos.z = InicialZRed
        blueBall.vel.x = 0
        blueBall.vel.z = 0
        redBall.vel.x = 0
        redBall.vel.z = 0
        bluePoints += 1
        blueScore.text = bluePoints
        
      if(blueBall.pos.x < 0 and blueBall.pos.z > -40):
        blueBall.pos.x = InicialXBlue
        blueBall.pos.z = InicialZBlue
        redBall.pos.x = InicialXRed
        redBall.pos.z = InicialZRed
        pointerBluePos.x = InicialXBlue
        pointerBluePos.z = InicialZBlue
        pointerRedPos.x = InicialXRed
        pointerRedPos.z = InicialZRed
        blueBall.vel.x = 0
        blueBall.vel.z = 0
        redBall.vel.x = 0
        redBall.vel.z = 0
        redPoints += 1 
        redScore.text = redPoints
        
        
  for i in range(len(ball)):
    ball[i].pos = ball[i].pos + ball[i].vel * dt
  
  ## SUMO CHECK
  if (circleField.pos.x-redBall.pos.x)**2 + (circleField.pos.z-redBall.pos.z)**2 > (circleField.radius + redBall.radius)**2 and (circleField.pos.x-redBall.pos.x)**2 + (circleField.pos.z-redBall.pos.z)**2 < (circleField.radius + redBall.radius + 4)**2:
      blueBall.pos.x = Inicial2XBlue
      blueBall.pos.z = Inicial2ZBlue
      redBall.pos.x = Inicial2XRed
      redBall.pos.z = Inicial2ZRed  
      pointerBluePos.x = Inicial2XBlue
      pointerBluePos.z = Inicial2ZBlue
      pointerRedPos.x = Inicial2XRed
      pointerRedPos.z = Inicial2ZRed
      blueBall.vel.x = 0
      blueBall.vel.z = 0
      redBall.vel.x = 0
      redBall.vel.z = 0
      bluePoints += 1
      blueScore.text = bluePoints
      circleField.radius = 40
      
  if (circleField.pos.x-blueBall.pos.x)**2 + (circleField.pos.z-blueBall.pos.z)**2 > (circleField.radius + blueBall.radius)**2 and (circleField.pos.x-blueBall.pos.x)**2 + (circleField.pos.z-blueBall.pos.z)**2 < (circleField.radius + blueBall.radius + 4)**2:
      blueBall.pos.x = Inicial2XBlue
      blueBall.pos.z = Inicial2ZBlue
      redBall.pos.x = Inicial2XRed
      redBall.pos.z = Inicial2ZRed  
      pointerBluePos.x = Inicial2XBlue
      pointerBluePos.z = Inicial2ZBlue
      pointerRedPos.x = Inicial2XRed
      pointerRedPos.z = Inicial2ZRed
      blueBall.vel.x = 0
      blueBall.vel.z = 0
      redBall.vel.x = 0
      redBall.vel.z = 0
      redPoints += 1    
      redScore.text = redPoints
      circleField.radius = 40
      
  if playerOneMoveForward:
      pointerBluePos.x -= 1
  if playerOneMoveLeft:
      pointerBluePos.z -= 1
  if playerOneMoveRight:
      pointerBluePos.z += 1
  if playerOneMoveBack:
      pointerBluePos.x += 1

  if playerTwoMoveForward:
      pointerRedPos.x += 1
  if playerTwoMoveLeft:
      pointerRedPos.z -= 1
  if playerTwoMoveRight:
      pointerRedPos.z += 1
  if playerTwoMoveBack:
      pointerRedPos.x -= 1
      
  blueBall.force.axis.x = pointerBluePos.x - blueBall.pos.x
  blueBall.force.axis.z = pointerBluePos.z - blueBall.pos.z
  blueBall.force.pos = blueBall.pos
  blueBall.force.shaftwidth = 0.5
  blueBall.force.axis.y = 0 

  redBall.force.axis.x = pointerRedPos.x - redBall.pos.x
  redBall.force.axis.z = pointerRedPos.z - redBall.pos.z
  redBall.force.pos = redBall.pos
  redBall.force.shaftwidth = 0.5
  redBall.force.axis.y = 0
  
  if bluePoints == 5:
      blueWins = box(canvas = scene, size = 100*vec(2.4, 1.45, 0.1), texture = "https://i.imgur.com/LT3PGP9.jpg", color = color.white)
      blueWins.pos = vec(0,200,-40)
      scene.center = vec(0, 200, -120)
      scene.forward = vec(0, 0, 0)
      bluePoints = 0

  if redPoints == 5:
      redWins = box(canvas = scene, size = 100*vec(2.4, 1.45, 0.1), texture = "https://i.imgur.com/QOAmRMf.jpg", color = color.white)
      redWins.pos = vec(0,200,-40)
      scene.center = vec(0, 200, -120)
      scene.forward = vec(0, 0, 0)
      redPoints = 0