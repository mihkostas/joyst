import pygame
from pynput.mouse import Button, Controller

pygame.init()
move = 15
mouse = Controller()
k = Controller()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True
j = pygame.joystick.Joystick(0) 
print('''
       _                 _   
      | |               | |  
      | | ___  _   _ ___| |_ 
  _   | |/ _ \| | | / __| __|
 | |__| | (_) | |_| \__ \ |_ 
  \____/ \___/ \__, |___/\__|
                __/ |        
               |___/         
''')

for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
    print ("Detected joystick "),joysticks[-1].get_name(),"'"
while keepPlaying:
          
     clock.tick(60)
     for event in pygame.event.get():
      try:
        if event.button == 2:
            if event.type == pygame.JOYBUTTONDOWN:
               print ("X Has Been Pressed")
               mouse.press(Button.left)
            elif event.type == pygame.JOYBUTTONUP:
               mouse.release(Button.left)
               print("X Has Been released.")
        if event.button == 1:
            if event.type == pygame.JOYBUTTONDOWN:
               print ("O Has Been Pressed")
               mouse.press(Button.right)
            elif event.type == pygame.JOYBUTTONUP:
               mouse.release(Button.right)
               print("O Has Been released.") 
      except:
         pass
     if j.get_axis(0) >= 0.5:
                 print("right")
                 mouse.move(move,0)
     if j.get_axis(0) <= -1:
                 print("left")
                 mouse.move(-move,0)
     if j.get_axis(1) >= 0.5:
                 mouse.move(0,move)
                 print("down")
     if j.get_axis(1) <= -1:
                 print("up")
                 mouse.move(0,-move)
