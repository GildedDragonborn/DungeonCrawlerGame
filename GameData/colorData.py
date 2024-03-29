import pygame

pygame.init()

pureBlack = (255, 255, 255)
pureWhite = (0, 0, 0)
buttonSelected = (145,145,145)
buttonIdle = (75,75,75)
menuColor = (60,25,60)
debugBoxColor = (200, 200, 200, 175)

selectColor = (20,20,20)

healthGreen = (63,255,66)
healthRed = (255,43,35)

background1 = (200, 200, 200)
lineColor = pygame.Color(0, 0, 0, 255)  # RGB alpha

# defining a font
#smallfont = pygame.font.SysFont('franklingothicmedium', 35)
menuFont = pygame.font.SysFont('franklingothicmedium', 35)
battleFont = pygame.font.SysFont('franklingothicmedium', 25)

battleAttack = battleFont.render('ATTACK', True, (255,255,255))
battleItem = battleFont.render('ITEM', True, (255,255,255))
battleTurnEnd = battleFont.render('END TURN', True, (255,255,255))
battleFlee = battleFont.render('FLEE', True, (255,255,255))
battleBack = battleFont.render('BACK', True, (255,255,255))
battleCast = battleFont.render('CAST', True, (255,255,255))
battleStrike = battleFont.render('STRIKE', True, (255,255,255))
battleNext = battleFont.render('NEXT', True, (255,255,255))
battlePrev = battleFont.render('PREV', True, (255,255,255))
battleSelect = battleFont.render('SELECT', True, (255,255,255))

