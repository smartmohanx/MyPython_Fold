'''
16. Create a class to implement shapes and draw the following
shapes
a) Rectangle
b) Circle
And Find their Areas Using Method Area.
'''

import pygame,sys
pygame.init()

#input
print("DRAW SHAPE AND FIND AREA!")
x = int((input("Enter RECTANGLE = 1 OR CIRCLE = 2:")))
if x == 1:
    l = int(input("Enter length:"))
    w = int(input("Enter width:"))
elif x == 2:
    r = int(input("Enter radius:"))
#text
font = pygame.font.SysFont("verdana",20)
text = font.render("Demo figure:Circle",True,'white')
text_rect = text.get_rect()
text_rect.center = (200,50)

font1 = pygame.font.SysFont('verdana',20)
text1 = font1.render("Demo figure:Rectangle",True,'white')
text1_rect = text1.get_rect()
text1_rect.center = (200,50)

def shape_circle():
    pygame.draw.circle(screen,"white",(200,200),100,5)
def rectangle():
    pygame.draw.line(screen,'white',(50,100),(350,100),5)
    pygame.draw.line(screen,'white',(50,250),(350,250),5)
    pygame.draw.line(screen,'white',(50,100),(50,250),5)
    pygame.draw.line(screen,'white',(350,100),(350,250),5)
class Shape:
        def area_rect(self,l,w):
            self.l = l
            self.w = w
            self.area = self.l * self.w
            #text-area result
            global text2,text2_rect
            font2 = pygame.font.SysFont("verdana",20)
            text2 = font2.render(("Area:{0};length,width:{1},{2}".format(self.area,self.l,self.w)),True,'black')
            text2_rect = text2.get_rect()
            text2_rect.center = (200,350)

        def area_cir(self,r):
            self.r = r
            self.area = 3.14 * self.r**2
            #text-area result
            global text2,text2_rect
            font2 = pygame.font.SysFont("verdana",20)
            text2 = font2.render(("Area:{0};Radius:{1}".format(self.area,self.r)),True,'black')
            text2_rect = text2.get_rect()
            text2_rect.center = (200,350)


obj = Shape() 
while True:
    if x == 1:
        #screen
        obj.area_rect(l,w)
        screen = pygame.display.set_mode((400,400))
        pygame.display.set_caption("rectangle")
        screen.fill("red")
        screen.blit(text1,text1_rect)
        screen.blit(text2,text2_rect)

    elif x == 2:
        #screen
        obj.area_cir(r)
        screen = pygame.display.set_mode((400,400))
        pygame.display.set_caption("circle")
        screen.fill("red")
        screen.blit(text,text_rect)
        screen.blit(text2,text2_rect)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if x == 1:
        screen.blit(text1,text1_rect)
        #drawing rectangle
        rectangle()
    elif x == 2:
        screen.blit(text,text_rect)
        #drawing circle
        shape_circle()

    pygame.display.update()



