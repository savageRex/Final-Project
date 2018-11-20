# Display Settings
screen_width = 768
screen_height = 720
FPS = 60

# Player Settings
acceleration = 1
friction = -0.12
gravity = 0.8
jump = 20

# Floor
floor = [(1,0,643), (2,3853,643), (3,4578,643), (4,5760,643), (5,6318,643), (6,6688,643)]

# Bricks locations
brick_list = [(1,1054,463),(1,1156,463),(1,1258,463),
              (1,3986,463),(1,4087,463),(3,4422,257),(3,4775,257),
              (1,4860,463),(1,5168,463),
              (1,7020,463),(1,7071,463),(1,7171,463),

              (5,6091,616),(5,6142,565),(5,6193,513),
              (5,6142,616),(5,6193,565),
              (5,6193,616),

              (5,6345,513),(5,6345,565),(5,6345,616),
              (5,6396,565),(5,6396,616),

              (5,7630,616),(5,7681,565),(5,7732,513),(5,7783,461),(5,7836,410),(5,7887,359),(5,7939,308),(5,7990,257),(5,8041,257)]

# Mystery box locations
mystery_list = [(2,1105,463),(2,1207,463),
                (2,5475,463),(2,5630,463),(2,5785,463),(2,5630,257),
                (2,7120,463)]

# Hidden box locations
annoying_list = [(1105,513), (3567,463),
                 (6401,361),
                 (6448,565),(6499,565),(6549,565),(6600,565),(6651,565)]

# Enemy locations
enemy_list = [(1050,626),(1150,626),(1600,626),
              (7000,626),(7200,626)]

#  Pipe locations
pipe_list = [(102,1492,592), (154,2007,566), (208,2418,542), (208,2983,542), (102,6738,592), (102,7560,592)]

#  Instruction
texts = [
         # ('Hey, before you read this,',100,220),
         # ('please kill the enemy in front of you first.',100,240),
         ('< BACK',20,(255,255,255),40,200),
         ('HOW TO PLAY',20,(255,255,255),280,250),
         ('MOVE',20,(255,255,255),520,310),
         # ('Use the left and right arrow keys to move.',12,(255,255,255),100,300),
         # ('You can also use "a" and "d" keys to move.',12,(255,255,255),100,320),
         ('JUMP',20,(255,255,255),520,390),
         ('HOLD TO JUMP HIGHER.',20,(255,255,255),200,450),
         # ('Press up or space key to jump.',12,(255,255,255),100,340),
         # ('Extend your jump by holding the key.',12,(255,255,255),100,360),
         # ('Disclaimer:',12,(255,255,255),100,400),
         # ('This game is not yet finished.',12,(255,255,255),100,420),
         # ('This game is not like any other platform games.',100,420),
         # ('Good luck have fun.',12,(255,255,255),100,440),
         # ('# Muhammad Erizky S - 2201797052',12,(255,255,255),100,480)
            ]