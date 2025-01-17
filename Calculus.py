import math
import pygame
import sys
class TextSprite(pygame.sprite.Sprite):
  def __init__(self, text, font, color, position):
      super().__init__()
      self.font = font
      self.color = color
      self.text = text
      self.update_text(self.text)
      self.rect = self.image.get_rect()
      self.rect.center = position
  def update_text(self, text):
      self.image = self.font.render(text, True, self.color)
      self.rect = self.image.get_rect()
class OldTextSprite(pygame.sprite.Sprite):
  def __init__(self, text, font, color, position):
      super().__init__()
      self.font = font
      self.color = color
      self.text = text
      self.update_text(self.text)
      self.rect = self.image.get_rect()
      self.rect.center = position
  def update_text(self, text):
      self.image = self.font.render(text, True, self.color)
class Line(pygame.sprite.Sprite):
  def __init__(self, start_pos, end_pos, color, thickness=2):
      super().__init__()
      self.color = color
      self.thickness = thickness
      self.start_pos = start_pos
      self.end_pos = end_pos
      self.image = pygame.Surface((abs(end_pos[0] - start_pos[0]) + thickness, abs(end_pos[1] - start_pos[1]) + thickness), pygame.SRCALPHA)
      self.rect = self.image.get_rect()
      self.rect.topleft = min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1])
      self.draw_line()
  def draw_line(self):
      self.image = pygame.Surface((abs(self.end_pos[0] - self.start_pos[0]) + self.thickness, abs(self.end_pos[1] - self.start_pos[1]) + self.thickness), pygame.SRCALPHA)
      self.rect = self.image.get_rect()
      self.rect.topleft = min(self.start_pos[0], self.end_pos[0]), min(self.start_pos[1], self.end_pos[1])
      pygame.draw.line(self.image, self.color, (self.start_pos[0] - self.rect.x, self.start_pos[1] - self.rect.y), (self.end_pos[0] - self.rect.x, self.end_pos[1] - self.rect.y), self.thickness)
class BlockSprite(pygame.sprite.Sprite):
  def __init__(self, surface_size, color, position):
     super().__init__()
     self.image = pygame.Surface(surface_size)
     self.color = color
     self.rect = self.image.get_rect()
     self.image.fill(color)
     self.rect.x, self.rect.y = position[0], position[1]
  def update(self, color):
      self.color = color
      self.image.fill(self.color)
class Circle(pygame.sprite.Sprite):
  def __init__(self, radius, color, position, thickness=2):
      super().__init__()
      self.radius = radius
      self.color = color
      self.position = position
      self.thickness = thickness
      self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
      self.rect = self.image.get_rect(center=position)
      self.draw_circle()
  def draw_circle(self):
      pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius, self.thickness)
class NumberBlock(BlockSprite):
  def __init__(self, number, position):
      super().__init__((75, 75), (155,150,150), position)
      font = pygame.font.SysFont(None, 60)
      self.number = number
      self.text_sprite = TextSprite(str(number), font, (0, 0, 0), (self.rect.center))
      num_text_sprites.append(self.text_sprite)
class fraction(pygame.sprite.Sprite):
  def __init__(self):
      super().__init__()
      self.frac_line = Line((frac_button.rect.centerx - 25, frac_button.rect.centery), (frac_button.rect.centerx + 25, frac_button.rect.centery), BLACK)
      self.numer = BlockSprite((35,35), BLACK, (frac_button.rect.centerx, frac_button.rect.centery))
      self.numer.rect.center = (frac_button.rect.centerx, frac_button.rect.centery-25)
      self.numerC = BlockSprite((31,31), BGRAY, (frac_button.rect.centerx, frac_button.rect.centery))
      self.numerC.rect.center = (frac_button.rect.centerx, frac_button.rect.centery-25)
      self.denom = BlockSprite((35,35), BLACK, (frac_button.rect.centerx, frac_button.rect.centery+5))
      self.denom.rect.center = (frac_button.rect.centerx, frac_button.rect.centery+25)
      self.denomC = BlockSprite((31,31), BGRAY, (frac_button.rect.centerx, frac_button.rect.centery+5))
      self.denomC.rect.center = (frac_button.rect.centerx, frac_button.rect.centery+25)
      self.frac_sprites = [self.frac_line, self.numer, self.numerC, self.denom, self.denomC]
def inflate(text, font_to_grow, alpha, growth):
  if alpha >= 0:
      alpha -= 25
      growth += 1
      changing = True
      font_to_grow = pygame.font.SysFont("arial", growth, bold=True)
      text.font = font_to_grow
      text.update_text(text.text)
      text.image.set_alpha(alpha)
      text.rect.x -= .51
      text.rect.y -= .51
  else:
      changing = False
  return changing, text, font_to_grow, alpha, growth
def sine_graph(a, b):
    sine_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    points = []
    for x in range(840):
        y = SCREEN_HEIGHT // 2 - int(a * math.sin(b * (x - 360 // 2)))
        points.append((x+360, y))
    pygame.draw.lines(sine_surf, RED, False, points, 2)
    return sine_surf
def cosine_graph(a, b):
    cosine_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    points = []
    for x in range(840):
        y = SCREEN_HEIGHT // 2 - int(a * math.cos(b * (x - 360 // 2)))
        points.append((x+360, y))
    pygame.draw.lines(cosine_surf, RED, False, points, 2)
    return cosine_surf
def find_angle_degrees(a):
    angle = math.radians(a)
    x = unitcirc.rect.centerx + (250 * math.cos(angle))
    y = unitcirc.rect.centery - (250 * math.sin(angle))
    angle_line.end_pos = (x, y)
    angle_line.draw_line()
    return angle_line
def find_angle_radians(a):
    angle = a
    x = unitcirc.rect.centerx + (250 * math.cos(angle))
    y = unitcirc.rect.centery - (250 * math.sin(angle))
    angle_line.end_pos = (x, y)
    angle_line.draw_line()
    return angle_line

BLACK = (0,0,0)
WHITE = (255,255,255)
TBLACK = (0,0,0,50)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
HIGHLIGHT = (184, 108, 108)
GRAY = (100,100,100)
BGRAY = (155,150,150)
DGRAY = (80,80,80)

pygame.init()
(SCREEN_WIDTH, SCREEN_HEIGHT) = 1200, 800
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("THE CALCULUS CALCINATOR 3000")
bg = BlockSprite((800,800), WHITE, (0,0))
surface = pygame.Surface((800, 800), pygame.SRCALPHA)
sine_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
cosine_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
origin = (400,400)
screen.fill(WHITE)


graph = []
num_lines = 40
for j in range(2):
  for i in range(num_lines):
      sep = 800//num_lines
      cord = (sep*i)
      if j==1:
          pygame.draw.line(screen, BLACK, (origin[0] - 10, cord), (origin[0] + 10, cord), 2)
          pygame.draw.line(surface, TBLACK, (0, cord), (800, cord), 2)
      else:
          pygame.draw.line(screen, BLACK, (cord, origin[0] - 10), (cord, origin[0] + 10), 2)
          pygame.draw.line(surface, TBLACK, (cord, 0), (cord, 800), 2)

x_line = Line((0, origin[1]), (800, origin[1]), BLACK)
y_line = Line((origin[1], 0), (origin[1], 800), BLACK)
circle = Circle(200, BLACK, origin)

##### TEXT SPRITES #####
title_font = pygame.font.SysFont("arial", 100, bold=True)
title = OldTextSprite("Unit Circle", title_font, RED, (origin[0], 200))
text_font = pygame.font.SysFont("arial", 60, bold=True)
calc = OldTextSprite("Calculator", text_font, BLACK, (origin[0], 270))
hyp = Line(origin, origin, RED)

##### MATH CALCULATES #####
theta = 0
x_end = origin[0] + 200 * math.cos(math.radians(theta))
y_end = origin[1] - 200 * math.sin(math.radians(theta))
sine = Line((x_end, origin[1]), (x_end, y_end), RED)
cosine = Line (origin, (x_end, origin[1]), RED)


##### COMMON #####
x_end = origin[0] + 200 * math.cos(math.radians(45))
y_end = origin[1] - 200 * math.sin(math.radians(45))


small_text_font = pygame.font.SysFont("arial", 20, bold=True)
Chyp = Line(origin, (x_end, y_end), BLUE)
Csin = Line((x_end, origin[1]), (x_end, y_end), BLUE)
Csin_text = OldTextSprite("Sineθ", small_text_font, BLUE, (x_end+25, 220+y_end//2))
Ccos = Line (origin, (x_end, origin[1]), BLUE)
Ccos_text = OldTextSprite("Cosineθ", small_text_font, BLUE, (200+x_end//2, origin[1]+ 10))
theta_text = OldTextSprite("θ", small_text_font, BLUE, (origin[0]+30, origin[1]- 12))
alpha = 255
common = [Chyp, Csin, Ccos]
common_text = [Csin_text, Ccos_text, theta_text]


##### Sprite Group #####
sprites = pygame.sprite.Group(bg, x_line, y_line, circle, hyp, sine, cosine, common, common_text, title, calc)


##### CALCULATOR SURFACES #####
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
font = pygame.font.SysFont(None, 60, bold=True)
efont = pygame.font.SysFont(None, 60)
sfont = pygame.font.SysFont(None, 30)
calcbg = BlockSprite((360,500), GRAY, (0, 2*SCREEN_HEIGHT//5-10))
unitcirc = Circle(250, BLACK, (2000//3, SCREEN_HEIGHT//2))
angle_line = Line((unitcirc.rect.center), (unitcirc.rect.center), RED, thickness=4)

entrybg = BlockSprite((340, 100), BGRAY, (10, (2*SCREEN_HEIGHT//5)))
entrytxt = TextSprite("", efont, BLACK, (entrybg.rect.right-20, entrybg.rect.centery))
entrytxt.math = ""
entrytxt2 = TextSprite("", efont, BLACK, (entrybg.rect.right-20, entrybg.rect.centery))
entrytxt2.math = ""
cover = BlockSprite((10,90), GRAY, (0, 2*SCREEN_HEIGHT//5+10))


# Square root symbol block
sqrt_block = BlockSprite((75,75), BGRAY, (255, (2 * SCREEN_HEIGHT // 5) + 110))
sqrt_text_sprite = TextSprite("√", font, BLACK, sqrt_block.rect.center)
sqrt_button = [sqrt_block, sqrt_text_sprite]

# Pi block
pi_block =BlockSprite((75,75), BGRAY, (255, (2 * SCREEN_HEIGHT // 5) + 295))
pi_text_sprite = TextSprite("π", efont, BLACK, pi_block.rect.center)
pi_button = [pi_block, pi_text_sprite]

# Enter block
enter_block =BlockSprite((75,50), BGRAY, (255, (2 * SCREEN_HEIGHT // 5) + 375))
enter_text_sprite = TextSprite("Enter", sfont, BLACK, enter_block.rect.center)
enter_button = [enter_block, enter_text_sprite]

all_sprites = pygame.sprite.Group()
number_blocks = []
num_text_sprites = [sqrt_text_sprite]


for i in range(9, 6, -1):  # Loop for numbers 7, 8, and 9
  number_block = NumberBlock(i, (15 + ((i - 7) % 3) * 80, (2 * SCREEN_HEIGHT // 5) + 110 + ((i - 7) // 3) * 80))
  number_blocks.append(number_block)
for i in range(6, 3, -1):  # Loop for numbers 4, 5, and 6
  number_block = NumberBlock(i, (15 + ((i - 4) % 3) * 80, (2 * SCREEN_HEIGHT // 5) + 190 + ((i - 4) // 3) * 100))
  number_blocks.append(number_block)
for i in range(3):  # Loop for numbers 1, 2, and 3
  number_block = NumberBlock(i + 1, (15 + (i % 3) * 80, (2 * SCREEN_HEIGHT // 5) + 270 + (i // 3) * 80))
  number_blocks.append(number_block)
number_block = NumberBlock(0, (entrybg.rect.centerx-85, 670))
number_blocks.append(number_block)

clear = BlockSprite((75,75), BGRAY, (entrybg.rect.centerx-5, 670))
clear_text_sprite = TextSprite("C", font, BLACK, clear.rect.center)
clear_button =[clear, clear_text_sprite]

negative = BlockSprite((75,75), BGRAY, (entrybg.rect.centerx-165, 670))
negative_text_sprite = TextSprite("(-)", efont, BLACK, negative.rect.center)
negative_button = [negative, negative_text_sprite]

##### Options #####
opt_block = BlockSprite((150,40), BGRAY, (22, 750))
opt_text_sprite = OldTextSprite("Radians", sfont, BLACK, opt_block.rect.center)
opt_block2 = BlockSprite((150,40), DGRAY, (opt_block.rect.x+150, 750))
opt_text_sprite2 = OldTextSprite("Degrees", sfont, BLACK, opt_block2.rect.center)
option1 = [opt_block,opt_text_sprite]
option2 = [opt_block2,opt_text_sprite2]
options = [option1, option2]

##### FRACTION BUTTON #####
frac_button = BlockSprite((75,100), BGRAY, (255, (2 * SCREEN_HEIGHT // 5) + 190))
fraction_sym = fraction()
fraction_sym.frac_sprites.insert(0, frac_button)
placement_numer = None
placement_denom = None

##### Instructions #####
instruct = OldTextSprite("", efont, BLACK, (15,30))
equation = OldTextSprite("", title_font, BLACK, (unitcirc.rect.x, (8*SCREEN_HEIGHT)//9))
instructions = [instruct,equation]
a, b = "a","b"
a_text = 'a'
##### MAIN LOOP #####
b_in_use = False  
radians = False
changing = False
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = False
       elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
           ##### MENU #####
                if not changing:
                  for text in common_text:
                      if text.rect.collidepoint(event.pos):
                          alpha = 255
                          growth = 20
                          change_text = text
                          changing =True
           ##### CALCULATOR #####
                if calcbg in sprites:     
                    ##### OPTIONS #####
                    for option in options:
                        for item in option:
                            if item.rect.collidepoint(event.pos):
                                if item in options[0]:
                                    option1[0].image.fill(DGRAY)
                                    option2[0].image.fill(BGRAY)
                                    if change_text.text == "θ":
                                        radians = True
                                    else:
                                        b_in_use = True  
                                elif item in options[1]:
                                    option1[0].image.fill(BGRAY)
                                    option2[0].image.fill(DGRAY)
                                    if change_text.text == "θ":
                                        radians = False
                                    else:
                                        b_in_use = False  
                    ##### ENTER #####
                    if entrytxt.text != "":
                        for item in enter_button:
                            if item.rect.collidepoint(event.pos):
                                enter_block.image.fill(DGRAY)
                                #### REMOVE
                                if "f" in entrytxt.math:
                                    for item in insert_frac.frac_sprites:
                                        sprites.remove(item)
                                #### MATH
                                if "√" in entrytxt.math:
                                    parts = entrytxt.text.split('√')
                                    before_sqrt = int(parts[0])
                                    after_sqrt = int(parts[1])
                                    entrytxt.text = before_sqrt * math.sqrt(after_sqrt)
                                    
                                if "√" in entrytxt2.math:
                                    parts = entrytxt2.text.split('√')
                                    before_sqrt = int(parts[0])
                                    after_sqrt = int(parts[1])
                                    entrytxt2.text = before_sqrt * math.sqrt(after_sqrt)    

                                if "π" in entrytxt.math:
                                    parts = entrytxt.text.split("π")
                                    try:
                                        before_pi = int(parts[0])
                                    except:
                                        before_pi = 1    
                                    try:
                                        after_pi = int(parts[1])
                                    except:
                                        after_pi = 1
                                    entrytxt.text = before_pi * math.pi * after_pi
                                    
                                if "π" in entrytxt2.math:
                                    parts = entrytxt2.text.split("π")
                                    try:
                                        before_pi = int(parts[0])
                                    except:
                                        before_pi = 1    
                                    try:
                                        after_pi = int(parts[1])
                                    except:
                                        after_pi = 1
                                    entrytxt.text = before_pi * math.pi * after_pi

                                if change_text.text == "Sineθ":
                                    if not b_in_use:
                                        instruct.text = "Enter value for b"
                                        instruct.update_text(instruct.text)    
                                        if "f" in entrytxt.math:
                                            entrytxt.math =  float(entrytxt.text)/float(entrytxt2.text)
                                        else:
                                            entrytxt.math =  float(entrytxt.text)

                                        parts = str(entrytxt.math).split('.')
                                        if len(parts) > 1 and parts[1] == '0':
                                            a_text = parts[0]    
                                        else:
                                            a_text = entrytxt.math
                                        a = entrytxt.math
                                        try:
                                            equation.text = f"y={a_text}+{b_text}sinθ"
                                        except:
                                            equation.text = f"y={a_text}+{b}sinθ"
                                        equation.update_text(equation.text)

                                    elif b_in_use:
                                        instruct.text = "Enter value for a"
                                        if "f" in entrytxt.math:
                                            entrytxt.math =  float(entrytxt.text)/float(entrytxt2.text)
                                        else:
                                            entrytxt.math =  float(entrytxt.text)
                                        parts = str(entrytxt.math).split('.')
                                        if len(parts) > 1 and parts[1] == '0':
                                            b_text = parts[0]    
                                        else:
                                            b_text = entrytxt.math
                                        b = entrytxt.math  * 0.1
                                        equation.text = f"y={a_text}+{b_text}sinθ"
                                        equation.update_text(equation.text)
                                    if a != "a" and b != "b":
                                        sine_surf = sine_graph(a, b)

                                elif change_text.text == "Cosineθ":
                                    if not b_in_use:
                                        instruct.text = "Enter value for b"
                                        instruct.update_text(instruct.text)    
                                        if "f" in entrytxt.math:
                                            entrytxt.math =  float(entrytxt.text)/float(entrytxt2.text)
                                        else:
                                            entrytxt.math =  float(entrytxt.text)

                                        parts = str(entrytxt.math).split('.')
                                        if len(parts) > 1 and parts[1] == '0':
                                            a_text = parts[0]    
                                        else:
                                            a_text = entrytxt.math
                                        a = entrytxt.math
                                        try:
                                            equation.text = f"y={a_text}+{b_text}cosθ"
                                        except:
                                            equation.text = f"y={a_text}+{b}cosθ"
                                        equation.update_text(equation.text)

                                    elif b_in_use:
                                        instruct.text = "Enter value for a"
                                        if "f" in entrytxt.math:
                                            entrytxt.math =  float(entrytxt.text)/float(entrytxt2.text)
                                        else:
                                            entrytxt.math =  float(entrytxt.text)
                                        parts = str(entrytxt.math).split('.')
                                        if len(parts) > 1 and parts[1] == '0':
                                            b_text = parts[0]    
                                        else:
                                            b_text = entrytxt.math
                                        b = entrytxt.math  * 0.1
                                        equation.text = f"y={a_text}+{b_text}cosθ"
                                        equation.update_text(equation.text)

                                    if a != "a" and b != "b":
                                        cosine_surf = cosine_graph(a, b)

                                elif change_text.text == "θ":
                                    
                                    if "f" in entrytxt.math:
                                        entrytxt.math =  float(entrytxt.text)/float(entrytxt2.text)
                                    else:
                                        entrytxt.math =  float(entrytxt.text)
                                    a = entrytxt.math
                                    if not radians:
                                        angle_line = find_angle_degrees(a)
                                    elif radians:
                                        angle_line = find_angle_radians(a)
                                
                                placement_numer = None
                                placement_denom = None
                                entrytxt.text =""
                                entrytxt.math =""
                                entrytxt2.text =""
                                entrytxt2.math =""
                                entrytxt.update_text(entrytxt.text)
                                entrytxt2.update_text(entrytxt2.text)
                                break
                    ##### PI BUTTON #####
                    for item in pi_button:
                        if item.rect.collidepoint(event.pos):
                            try:
                                if entrytxt.text[-1] != "π":
                                    if placement_numer is None and placement_denom is None:
                                        entrytxt.text +="π"
                                        entrytxt.math += "π"
                                        entrytxt.update_text(entrytxt.text)
                                        entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                                    else:
                                        ##### DENOMERATOR
                                        if insert_frac.denomC.color == HIGHLIGHT:
                                            entrytxt2.math += "π"
                                            entrytxt2.text += "π"
                                            entrytxt2.update_text(entrytxt2.text)
                                            entrytxt2.rect.topright = placement_denom
                                            sprites.remove(insert_frac.denom, insert_frac.denomC)

                                        ##### NUMERATOR
                                        if insert_frac.numerC.color == HIGHLIGHT:
                                            entrytxt.math += "π"
                                            entrytxt.text += "π"
                                            entrytxt.update_text(entrytxt.text)
                                            entrytxt.rect.topright = placement_numer
                                            sprites.remove(insert_frac.numer, insert_frac.numerC)
                                    break
                            except:
                                if placement_numer is None and placement_denom is None:
                                    entrytxt.text +="π"
                                    entrytxt.math += "π"
                                    entrytxt.update_text(entrytxt.text)
                                    entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                                else:
                                    ##### DENOMERATOR
                                    if insert_frac.denomC.color == HIGHLIGHT:
                                        entrytxt2.math += "π"
                                        entrytxt2.text += "π"
                                        entrytxt2.update_text(entrytxt2.text)
                                        entrytxt2.rect.topright = placement_denom
                                        sprites.remove(insert_frac.denom, insert_frac.denomC)

                                    ##### NUMERATOR
                                    if insert_frac.numerC.color == HIGHLIGHT:
                                        entrytxt.math += "π"
                                        entrytxt.text += "π"
                                        entrytxt.update_text(entrytxt.text)
                                        entrytxt.rect.topright = placement_numer
                                        sprites.remove(insert_frac.numer, insert_frac.numerC)
                                break
                    ##### NUMBER PAD #####
                    for item in number_blocks:
                        if item.rect.collidepoint(event.pos) or item.text_sprite.rect.collidepoint(event.pos):
                            item.image.fill(DGRAY)
                            if placement_numer is None and placement_denom is None:
                                entrytxt.text += item.text_sprite.text
                                entrytxt.math += item.text_sprite.text
                                entrytxt.update_text(entrytxt.text)
                                entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                            else:
                                ##### DENOMERATOR
                                if insert_frac.denomC.color == HIGHLIGHT:
                                    entrytxt2.math += item.text_sprite.text
                                    entrytxt2.text += item.text_sprite.text
                                    entrytxt2.update_text(entrytxt2.text)
                                    entrytxt2.rect.topright = placement_denom
                                    sprites.remove(insert_frac.denom, insert_frac.denomC)

                                ##### NUMERATOR
                                if insert_frac.numerC.color == HIGHLIGHT:
                                    entrytxt.math += item.text_sprite.text
                                    entrytxt.text += item.text_sprite.text
                                    entrytxt.update_text(entrytxt.text)
                                    entrytxt.rect.topright = placement_numer
                                    sprites.remove(insert_frac.numer, insert_frac.numerC)
                            break
                   ##### PRESS NEGATIVE #####
                    for item in negative_button:
                        if item.rect.collidepoint(event.pos):
                            try:
                                if entrytxt.text[0] != "-":
                                    if placement_numer is None and placement_denom is None:
                                            entrytxt.text = "-" + entrytxt.text
                                            entrytxt.math = "-" + entrytxt.math
                                            entrytxt.update_text(entrytxt.text)
                                            entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                                    else:
                                        ##### DENOMERATOR
                                        if insert_frac.denomC.color == HIGHLIGHT:
                                                entrytxt2.text = "-" + entrytxt2.text
                                                entrytxt2.math = "-" + entrytxt2.math
                                                entrytxt2.update_text(entrytxt2.text)
                                                entrytxt2.rect.topright = placement_denom
                                                sprites.remove(insert_frac.denom, insert_frac.denomC)

                                        ##### NUMERATOR
                                        if insert_frac.numerC.color == HIGHLIGHT:
                                                entrytxt.text = "-" + entrytxt.text
                                                entrytxt.math = "-" + entrytxt.math
                                                entrytxt.update_text(entrytxt.text)
                                                entrytxt.rect.topright = placement_numer
                                                sprites.remove(insert_frac.numer, insert_frac.numerC)
                                    break
                            except:
                                if placement_numer is None and placement_denom is None:
                                    entrytxt.text +="-"
                                    entrytxt.math += "-"
                                    entrytxt.update_text(entrytxt.text)
                                    entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                                else:
                                    ##### DENOMERATOR
                                    if insert_frac.denomC.color == HIGHLIGHT:
                                        entrytxt2.math += "-"
                                        entrytxt2.text += "-"
                                        entrytxt2.update_text(entrytxt2.text)
                                        entrytxt2.rect.topright = placement_denom
                                        sprites.remove(insert_frac.denom, insert_frac.denomC)
                                    ##### NUMERATOR
                                    if insert_frac.numerC.color == HIGHLIGHT:
                                        entrytxt.math += "-"
                                        entrytxt.text += "-"
                                        entrytxt.update_text(entrytxt.text)
                                        entrytxt.rect.topright = placement_numer
                                        sprites.remove(insert_frac.numer, insert_frac.numerC)
                                break
                    ##### PRESS SQUARE ROOT #####
                    for item in sqrt_button:
                        if item.rect.collidepoint(event.pos):
                            try:
                                if entrytxt.text[-1] != "√":
                                    if placement_numer is None and placement_denom is None:
                                        entrytxt.text +="√"
                                        entrytxt.math += "√"
                                        entrytxt.update_text(entrytxt.text)
                                        entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                                    else:
                                        ##### DENOMERATOR
                                        if insert_frac.denomC.color == HIGHLIGHT:
                                            entrytxt2.math += "√"
                                            entrytxt2.text += "√"
                                            entrytxt2.update_text(entrytxt2.text)
                                            entrytxt2.rect.topright = placement_denom
                                            sprites.remove(insert_frac.denom, insert_frac.denomC)

                                        ##### NUMERATOR
                                        if insert_frac.numerC.color == HIGHLIGHT:
                                            entrytxt.math += "√"
                                            entrytxt.text += "√"
                                            entrytxt.update_text(entrytxt.text)
                                            entrytxt.rect.topright = placement_numer
                                            sprites.remove(insert_frac.numer, insert_frac.numerC)
                                    break
                            except:
                                if placement_numer is None and placement_denom is None:
                                    entrytxt.text +="√"
                                    entrytxt.math += "√"
                                    entrytxt.update_text(entrytxt.text)
                                    entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                                else:
                                    ##### DENOMERATOR
                                    if insert_frac.denomC.color == HIGHLIGHT:
                                        entrytxt2.math += "√"
                                        entrytxt2.text += "√"
                                        entrytxt2.update_text(entrytxt2.text)
                                        entrytxt2.rect.topright = placement_denom
                                        sprites.remove(insert_frac.denom, insert_frac.denomC)

                                    ##### NUMERATOR
                                    if insert_frac.numerC.color == HIGHLIGHT:
                                        entrytxt.math += "√"
                                        entrytxt.text += "√"
                                        entrytxt.update_text(entrytxt.text)
                                        entrytxt.rect.topright = placement_numer
                                        sprites.remove(insert_frac.numer, insert_frac.numerC)
                                break
                    ##### PRESS FRACTION #####
                    for item in fraction_sym.frac_sprites:
                        if item.rect.collidepoint(event.pos):
                           
                            insert_frac = fraction()
                            frac_button.image.fill(DGRAY)
                            fraction_sym.numerC.image.fill(DGRAY)
                            insert_frac.numerC.image.fill(HIGHLIGHT)
                            insert_frac.numerC.color = HIGHLIGHT


                            fraction_sym.denomC.image.fill(DGRAY)
                            for item in insert_frac.frac_sprites:
                                item.rect.y -= 190
                                sprites.add(item)
                            placement_numer = insert_frac.numerC.rect.topright
                            placement_denom = insert_frac.denomC.rect.topright
                            if entrytxt.text != "":
                                entrytxt.rect.topright = insert_frac.numer.rect.topright
                                sprites.remove(insert_frac.numer, insert_frac.numerC)                            
                            entrytxt.math += "f"
                            break                
                    ##### CLEAR AND HIGHLIGHTS #####            
                    if "f" in entrytxt.math:
                        if insert_frac.numerC.rect.collidepoint(event.pos):
                            insert_frac.denomC.image.fill(BGRAY)
                            insert_frac.numerC.image.fill(HIGHLIGHT)
                            insert_frac.numerC.color = HIGHLIGHT
                            insert_frac.denomC.color = BGRAY
                        elif insert_frac.denomC.rect.collidepoint(event.pos):
                            insert_frac.numerC.image.fill(BGRAY)
                            insert_frac.denomC.image.fill(HIGHLIGHT)
                            insert_frac.denomC.color = HIGHLIGHT
                            insert_frac.numerC.color = BGRAY
                    ##### CLEAR BUTTON #####
                    if entrytxt.text != "":
                        for item in clear_button:
                            if item.rect.collidepoint(event.pos):
                                clear.image.fill(DGRAY)
                                if "f" in entrytxt.math:
                                    for item in insert_frac.frac_sprites:
                                        sprites.remove(item)
                                placement_numer = None
                                placement_denom = None
                                entrytxt.text =""
                                entrytxt.math =""
                                entrytxt2.text =""
                                entrytxt2.math =""
                                entrytxt.update_text(entrytxt.text)
                                entrytxt2.update_text(entrytxt2.text)
                                break
       #### CHANGE BUTTON COLOR #####
       elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if calcbg in sprites:
                    for button in number_blocks:
                        button.update(BGRAY)
                    clear.image.fill(BGRAY)
                    enter_block.image.fill(BGRAY)
                    frac_button.image.fill(BGRAY)
                    fraction_sym.numerC.image.fill(BGRAY)
                    fraction_sym.denomC.image.fill(BGRAY)
       ##### KEY PRESS #####
       elif event.type == pygame.KEYDOWN:
           if calcbg in sprites:
               for num in num_text_sprites:
                   try:
                       if num.text == chr(event.key):
                           for button in number_blocks:
                               if button.rect.colliderect(num.rect):
                                   button.image.fill(DGRAY)
                                   if placement_numer is None and placement_denom is None:
                                       entrytxt.text += num.text
                                       entrytxt.math += num.text
                                       entrytxt.update_text(entrytxt.text)
                                       entrytxt.rect.topright =(entrybg.rect.right-20, entrybg.rect.y+30)
                                   else:
                                       ##### DENOMERATOR
                                       if insert_frac.denomC.color == HIGHLIGHT:
                                           entrytxt2.math += num.text
                                           entrytxt2.text += num.text
                                           entrytxt2.update_text(entrytxt2.text)
                                           entrytxt2.rect.topright = placement_denom
                                           sprites.remove(insert_frac.denom, insert_frac.denomC)
                                       ##### NUMERATOR
                                       if insert_frac.numerC.color == HIGHLIGHT:
                                           entrytxt.math += num.text
                                           entrytxt.text += num.text
                                           entrytxt.update_text(entrytxt.text)
                                           entrytxt.rect.topright = placement_numer
                                           sprites.remove(insert_frac.numer, insert_frac.numerC)
                                   break
                   except ValueError:
                       continue
       elif event.type == pygame.KEYUP:  
          if calcbg in sprites:
              for num in num_text_sprites:
                   try:
                       if num.text == chr(event.key):  
                           for button in number_blocks:
                               if button.rect.colliderect(num.rect):
                                   button.update(BGRAY)
                   except ValueError:
                       continue
   if changing:
        changing, change_text, font_to_grow, alpha, growth = inflate(change_text, small_text_font, alpha, growth)
        if change_text.text == "Sineθ" and alpha <= 0:
            sprites.empty()
            surface.set_alpha(0)
            sprites.add(x_line, y_line, calcbg, entrybg, number_blocks, sqrt_block, num_text_sprites, entrytxt, entrytxt2, cover, \
                fraction_sym.frac_sprites, clear_button, negative_button, enter_button, instructions, options, pi_button)
            opt_text_sprite.text, opt_text_sprite2.text = "B", "A"
            opt_text_sprite.rect.centerx += 16
            opt_text_sprite2.rect.centerx += 17
            instruct.text = "Enter value for a"
            equation.text = "y=a+bsinθ"
            sine_surf = sine_graph(100,.1)
            SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            opt_text_sprite.update_text(opt_text_sprite.text) 
            opt_text_sprite2.update_text(opt_text_sprite2.text) 
            equation.update_text(equation.text)    
            instruct.update_text(instruct.text)    
            x_line.start_pos, x_line.end_pos = (0, SCREEN_HEIGHT//2) , (SCREEN_WIDTH, SCREEN_HEIGHT//2)
            y_line.start_pos, y_line.end_pos = (unitcirc.rect.centerx, 0), (unitcirc.rect.centerx, SCREEN_HEIGHT)
            x_line.draw_line()
            y_line.draw_line()

        elif change_text.text == "Cosineθ" and alpha <= 0:
            sprites.empty()
            surface.set_alpha(0)
            sprites.add(x_line, y_line, calcbg, entrybg, number_blocks, sqrt_block, num_text_sprites, entrytxt, entrytxt2, cover, \
                fraction_sym.frac_sprites, clear_button, negative_button, enter_button, instructions, options, pi_button)
            opt_text_sprite.text, opt_text_sprite2.text = "B", "A"
            opt_text_sprite.rect.centerx += 16
            opt_text_sprite2.rect.centerx += 17
            instruct.text = "Enter value for a"
            equation.text = "y=a+bcosθ"
            cosine_surf = cosine_graph(100,.1)

            SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            opt_text_sprite.update_text(opt_text_sprite.text) 
            opt_text_sprite2.update_text(opt_text_sprite2.text) 
            equation.update_text(equation.text)    
            instruct.update_text(instruct.text)    
            x_line.start_pos, x_line.end_pos = (0, SCREEN_HEIGHT//2) , (SCREEN_WIDTH, SCREEN_HEIGHT//2)
            y_line.start_pos, y_line.end_pos = (unitcirc.rect.centerx, 0), (unitcirc.rect.centerx, SCREEN_HEIGHT)
            x_line.draw_line()
            y_line.draw_line()

        elif change_text.text == "θ" and alpha <= 0:
            sprites.empty()
            surface.set_alpha(0)
            sprites.add(x_line, y_line, calcbg, unitcirc, entrybg, number_blocks, sqrt_block, num_text_sprites, entrytxt, entrytxt2, cover, \
                fraction_sym.frac_sprites, clear_button, negative_button, enter_button, instructions, angle_line, options, pi_button)
            instruct.text = "Enter " + change_text.text + " value to see the Angle"

            SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            equation.update_text(equation.text)    
            instruct.update_text(instruct.text)    
            x_line.start_pos, x_line.end_pos = (0, SCREEN_HEIGHT//2) , (SCREEN_WIDTH, SCREEN_HEIGHT//2)
            y_line.start_pos, y_line.end_pos = (unitcirc.rect.centerx, 0), (unitcirc.rect.centerx, SCREEN_HEIGHT)
            x_line.draw_line()
            y_line.draw_line()

   theta += 1
   x_end = origin[0] + 199 * math.cos(math.radians(theta))
   y_end = origin[1] - 199 * math.sin(math.radians(theta))

   hyp.end_pos = (x_end, y_end)
   sine.start_pos, sine.end_pos = (x_end, origin[1]), (x_end, y_end)
   cosine.end_pos = (x_end, origin[1])

   hyp.draw_line()
   sine.draw_line()
   cosine.draw_line()
   
   screen.fill(WHITE)
   sprites.draw(screen)
   screen.blit(surface, (0, 0))
   screen.blit(sine_surf, (0, 0))
   screen.blit(cosine_surf, (0, 0))
   
   pygame.display.flip()
   pygame.time.Clock().tick(30)
# Quit Pygame
pygame.quit()
sys.exit()