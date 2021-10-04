import pygame
pygame.init()

walkRight = [pygame.image.load('Animation\WalkR1.png'), pygame.image.load('Animation\WalkR2.png'), # массив спрайтов
             pygame.image.load('Animation\WalkR3.png'), pygame.image.load('Animation\WalkR4.png'),
             pygame.image.load('Animation\WalkR5.png'), pygame.image.load('Animation\WalkR6.png')]
walkLeft = [pygame.image.load('Animation\WalkL1.png'), pygame.image.load('Animation\WalkL2.png'), # массив спрайтов
             pygame.image.load('Animation\WalkL3.png'), pygame.image.load('Animation\WalkL4.png'),
             pygame.image.load('Animation\WalkL5.png'), pygame.image.load('Animation\WalkL6.png')]
Stand = pygame.image.load('Animation\Stand.png') # спрайт персонажа в бездействии
StandL = pygame.image.load('Animation\StandL.png')
Sit = pygame.image.load('Animation\Sit.png')
SitL = pygame.image.load('Animation\SitL.png')

main_menu_anim = [pygame.image.load('main_menu\Rain1.png'), pygame.image.load('main_menu\Rain2.png'), # массив спрайтов
             pygame.image.load('main_menu\Rain3.png'), pygame.image.load('main_menu\Rain4.png'),
             pygame.image.load('main_menu\Rain5.png'), pygame.image.load('main_menu\Rain6.png')]
house_rain_anim = [pygame.image.load('Grounds\ground_house_rain1.png'), pygame.image.load('Grounds\ground_house_rain2.png'),
                   pygame.image.load('Grounds\ground_house_rain3.png'), pygame.image.load('Grounds\ground_house_rain4.png'),
                   pygame.image.load('Grounds\ground_house_rain5.png'), pygame.image.load('Grounds\ground_house_rain6.png')] # задний фон в доме
sleep_forest = [pygame.image.load('Grounds\Forest1.png'), pygame.image.load('Grounds\Forest2.png'),
                pygame.image.load('Grounds\Forest3.png'), pygame.image.load('Grounds\Forest4.png'),
                pygame.image.load('Grounds\Forest5.png'), pygame.image.load('Grounds\Forest6.png')]
tombstone_burn = [pygame.image.load('Grounds\Forest_tombstone_fire1.png'), pygame.image.load('Grounds\Forest_tombstone_fire2.png'),
                  pygame.image.load('Grounds\Forest_tombstone_fire3.png'), pygame.image.load('Grounds\Forest_tombstone_fire4.png'),
                  pygame.image.load('Grounds\Forest_tombstone_fire5.png'), pygame.image.load('Grounds\Forest_tombstone_fire6.png'),]
forest_rain = [pygame.image.load('Grounds\Forest_rain1.png'), pygame.image.load('Grounds\Forest_rain2.png'),
               pygame.image.load('Grounds\Forest_rain3.png'), pygame.image.load('Grounds\Forest_rain4.png'),
               pygame.image.load('Grounds\Forest_rain5.png'), pygame.image.load('Grounds\Forest_rain6.png'),]
forest_blood_rain = [pygame.image.load('Grounds\Forest_blood_rain1.png'), pygame.image.load('Grounds\Forest_blood_rain2.png'),
                     pygame.image.load('Grounds\Forest_blood_rain3.png'), pygame.image.load('Grounds\Forest_blood_rain4.png'),
                     pygame.image.load('Grounds\Forest_blood_rain5.png'), pygame.image.load('Grounds\Forest_blood_rain6.png')]
spirit_on = [pygame.image.load('Grounds\ground_house_floor_0_room_1_spirit1.png'), pygame.image.load('Grounds\ground_house_floor_0_room_1_spirit2.png'),
            pygame.image.load('Grounds\ground_house_floor_0_room_1_spirit3.png'), pygame.image.load('Grounds\ground_house_floor_0_room_1_spirit4.png'),
            pygame.image.load('Grounds\ground_house_floor_0_room_1_spirit5.png'), pygame.image.load('Grounds\ground_house_floor_0_room_1_spirit6.png')]

walkRightObsession = [pygame.image.load('Enemy\WalkR1.png'), pygame.image.load('Enemy\WalkR2.png'), # массив спрайтов
             pygame.image.load('Enemy\WalkR3.png'), pygame.image.load('Enemy\WalkR4.png'),
             pygame.image.load('Enemy\WalkR5.png'), pygame.image.load('Enemy\WalkR6.png')]
walkLeftObsession = [pygame.image.load('Enemy\WalkL1.png'), pygame.image.load('Enemy\WalkL2.png'), # массив спрайтов
             pygame.image.load('Enemy\WalkL3.png'), pygame.image.load('Enemy\WalkL4.png'),
             pygame.image.load('Enemy\WalkL5.png'), pygame.image.load('Enemy\WalkL6.png')]
StandObsession = pygame.image.load('Enemy\Stand.png')

walkRightShape = [pygame.image.load('Enemy\WalkR1Shape.png'), pygame.image.load('Enemy\WalkR2Shape.png'),
                  pygame.image.load('Enemy\WalkR3Shape.png'), pygame.image.load('Enemy\WalkR4Shape.png'),
                  pygame.image.load('Enemy\WalkR5Shape.png'), pygame.image.load('Enemy\WalkR6Shape.png')]
walkLeftShape = [pygame.image.load('Enemy\WalkL1Shape.png'), pygame.image.load('Enemy\WalkL2Shape.png'),
                  pygame.image.load('Enemy\WalkL3Shape.png'), pygame.image.load('Enemy\WalkL4Shape.png'),
                  pygame.image.load('Enemy\WalkL5Shape.png'), pygame.image.load('Enemy\WalkL6Shape.png')]
StandShape = pygame.image.load('Enemy\StandShape.png')

YelR = [pygame.image.load('Enemy\YelR1.png'), pygame.image.load('Enemy\YelR2.png'),
        pygame.image.load('Enemy\YelR3.png'), pygame.image.load('Enemy\YelR4.png'),
        pygame.image.load('Enemy\YelR5.png'), pygame.image.load('Enemy\YelR6.png')]

YelL = [pygame.image.load('Enemy\YelL1.png'), pygame.image.load('Enemy\YelL2.png'),
        pygame.image.load('Enemy\YelL3.png'), pygame.image.load('Enemy\YelL4.png'),
        pygame.image.load('Enemy\YelL5.png'), pygame.image.load('Enemy\YelL6.png')]

StandYel = pygame.image.load('Enemy\YelR1.png')

eyeless = pygame.image.load('Enemy\StandGhost.png')
eyelessL = pygame.image.load('Enemy\StandGhostL.png')

StandJumpScare = pygame.image.load('Enemy\StandJumpscare.png')

med = pygame.image.load('Items\Medkit.png') # спрайт аптечки
cross_defender = pygame.image.load('Items\cross_defender.png')


flashlight = pygame.image.load('Items\Flashlight.png')
flashlight_on = pygame.image.load('Items\Flashlight_on.png')
flashlightL = pygame.image.load('Items\FlashlightL.png')
flashlight_onL = pygame.image.load('Items\Flashlight_onL.png')

infrared = pygame.image.load('Items\infrared.png')
infrared_on = pygame.image.load('Items\infrared_on.png')
infraredL = pygame.image.load('Items\infraredL.png')
infrared_onL = pygame.image.load('Items\infrared_onL.png')

camera_off = pygame.image.load('Items\camera_off.png')
camera_on = pygame.image.load('Items\camera_on.png')

rad = pygame.image.load('Items\Radio.png')
radon = pygame.image.load('Items\Radio_on.png')
radcon = pygame.image.load('Items\Radio_contact.png')

tempimg = pygame.image.load('Items\Term.png')
tempLimg = pygame.image.load('Items\TermL.png')

tombstone = pygame.image.load('Grounds\Forest_tombstone.png')
floor_0 = pygame.image.load('Grounds\ground_house_floor_0.png')
floor_0_lightoff = pygame.image.load('Grounds\ground_house_floor_0_lightoff.png')
floor_0_room_1 = pygame.image.load('Grounds\ground_house_floor_0_room_1.png')
floor_0_room_1_lightoff = pygame.image.load('Grounds\ground_house_floor_0_room_1_lightoff.png')

floor_0_room_1_camera = pygame.image.load('Grounds\ground_house_floor_0_room_camera.png')
floor_0_room_1_camera_lightoff = pygame.image.load('Grounds\ground_house_floor_0_room_camera_lightoff.png')

scream = pygame.image.load('Screamers\screamer.png')

creepy = pygame.image.load('Enemy\scare.png')
music_box = [pygame.image.load('Items\Box.png'), pygame.image.load('Items\Box_alert.png')]


mind_bar = [pygame.image.load('Interface\mind_normal.png'), pygame.image.load('Interface\mind_medium.png'),
            pygame.image.load('Interface\mind_danger.png'), pygame.image.load('Interface\mind_critical.png')]

evidance = pygame.image.load('evidence\hands.png')

cat_stand = pygame.image.load('Animal\Stand.png')
cat_standL = pygame.image.load('Animal\StandL.png')
cat_walk = [pygame.image.load('Animal\Stand.png'), pygame.image.load('Animal\R2.png'),
            pygame.image.load('Animal\Stand.png'), pygame.image.load('Animal\R4.png'),
            pygame.image.load('Animal\Stand.png'), pygame.image.load('Animal\R2.png')]
cat_walkL = [pygame.image.load('Animal\StandL.png'), pygame.image.load('Animal\L2.png'),
            pygame.image.load('Animal\StandL.png'), pygame.image.load('Animal\L4.png'),
            pygame.image.load('Animal\StandL.png'), pygame.image.load('Animal\L2.png')]
cathide = pygame.image.load('Animal\Hide.png')
cathideL = pygame.image.load('Animal\HideL.png')

