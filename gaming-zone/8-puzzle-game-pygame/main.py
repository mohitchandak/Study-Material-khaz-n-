import pygame
from pygame.locals import *
import time
import tkinter as tk
from tkinter import messagebox as tmsg
import random

root =tk.Tk()
root.withdraw()

end_time="0"
class Puzzle:
	def __init__(self):
		self.x =120
		self.y =150
		self.start = int(time.time())
	def draw(self, win):
		global end_time
		font = pygame.font.SysFont("comicsans",40)
		title = font.render("Solve the Puzzle:",True,(240,240,0))
		now = int(time.time())
		tp = now-self.start
		sec = tp%60
		minute= tp//60
		self.sho= str(minute)+":"+str(sec)
		end_time = self.sho
		t = font.render(f"Time passed: {self.sho}",True,(200,89,200))
		win.blit(title,(130,20))
		win.blit(t,(140,60))

		for i in range(4):
			pygame.draw.line(win,(200,200,200),(self.x-4, self.y+90*i),(self.x+5+3*90,self.y+90*i),10)
		for i in range(4):
			pygame.draw.line(win,(200,200,200),(self.x+90*i, self.y),(self.x+90*i,self.y+3*90),10)	

puzzle = Puzzle()

class Pieces:
	def __init__(self):
		pygame.font.init()
		self.font = pygame.font.SysFont("lucida", 60)
		self.wd = 90
		self.loc =[[126+self.wd*0,156+self.wd*0,1],[126+self.wd*1,156+self.wd*0,2],[126+self.wd*2,156+self.wd*0,3],
					[126+self.wd*0,156+self.wd*1,4],[126+self.wd*1,156+self.wd*1,5],[126+self.wd*2,156+self.wd*1,6],
					[126+self.wd*0,156+self.wd*2,7],[126+self.wd*1,156+self.wd*2,8]]
		self.solved_loc =[[126+self.wd*0,156+self.wd*0,1],[126+self.wd*1,156+self.wd*0,2],[126+self.wd*2,156+self.wd*0,3],
					[126+self.wd*0,156+self.wd*1,4],[126+self.wd*1,156+self.wd*1,5],[126+self.wd*2,156+self.wd*1,6],
					[126+self.wd*0,156+self.wd*2,7],[126+self.wd*1,156+self.wd*2,8]]
			
		self.empty_spot =[126+self.wd*2,156+self.wd*2,0]		
	def show(self,win):
		for l in self.loc:
			pygame.draw.rect(win,(50,30,20),(l[0],l[1],80,80))
			text = self.font.render(str(l[2]),True,(255,255,255))
			win.blit(text,(l[0]+25,l[1]+25))
	def check_solved(self):		
		if self.solved_loc==self.loc:
			tmsg.showinfo("Solved",f"Congratulations! You have solved the puzzle in {end_time} mins")	
			shuffle(self)
			return False
		else: 
			return True
	def search_and_shift(self,pos):
		pressed =False
		for i in range(len(self.loc)):
			if pos[0]>self.loc[i][0] and pos[0]<self.loc[i][0]+80 and pos[1]>self.loc[i][1] and pos[1]<self.loc[i][1]+80:
				pressed =True
				break
		if pressed:		
			if self.loc[i][0]+90==self.empty_spot[0] and self.loc[i][1]==self.empty_spot[1]:
				temp = self.loc[i]
				self.empty_spot[2]= self.loc[i][2]
				self.loc[i] = self.empty_spot
				self.empty_spot = temp
				self.empty_spot[2]=0

			elif self.loc[i][0]-90==self.empty_spot[0] and self.loc[i][1]==self.empty_spot[1]:
				temp = self.loc[i]
				self.empty_spot[2]= self.loc[i][2]
				self.loc[i] = self.empty_spot
				self.empty_spot = temp
				self.empty_spot[2]=0

			elif self.loc[i][0]==self.empty_spot[0] and self.loc[i][1]+90==self.empty_spot[1]:
				temp = self.loc[i]
				self.empty_spot[2]= self.loc[i][2]
				self.loc[i] = self.empty_spot
				self.empty_spot = temp
				self.empty_spot[2]=0

			elif self.loc[i][0]==self.empty_spot[0] and self.loc[i][1]-90==self.empty_spot[1]:
				temp = self.loc[i]
				self.empty_spot[2]= self.loc[i][2]
				self.loc[i] = self.empty_spot
				self.empty_spot = temp
				self.empty_spot[2]=0
			


pieces = Pieces()
def shuffle(pieces):
	for _ in range(1000):
		i = random.randint(0, 7)
		if pieces.loc[i][0]+90==pieces.empty_spot[0] and pieces.loc[i][1]==pieces.empty_spot[1]:
			temp = pieces.loc[i]
			pieces.empty_spot[2]= pieces.loc[i][2]
			pieces.loc[i] = pieces.empty_spot
			pieces.empty_spot = temp
			pieces.empty_spot[2]=0

		elif pieces.loc[i][0]-90==pieces.empty_spot[0] and pieces.loc[i][1]==pieces.empty_spot[1]:
			temp = pieces.loc[i]
			pieces.empty_spot[2]= pieces.loc[i][2]
			pieces.loc[i] = pieces.empty_spot
			pieces.empty_spot = temp
			pieces.empty_spot[2]=0

		elif pieces.loc[i][0]==pieces.empty_spot[0] and pieces.loc[i][1]+90==pieces.empty_spot[1]:
			temp = pieces.loc[i]
			pieces.empty_spot[2]= pieces.loc[i][2]
			pieces.loc[i] = pieces.empty_spot
			pieces.empty_spot = temp
			pieces.empty_spot[2]=0

		elif pieces.loc[i][0]==pieces.empty_spot[0] and pieces.loc[i][1]-90==pieces.empty_spot[1]:
			temp = pieces.loc[i]
			pieces.empty_spot[2]= pieces.loc[i][2]
			pieces.loc[i] = pieces.empty_spot
			pieces.empty_spot = temp
			pieces.empty_spot[2]=0

def draw_win(win):
	win.fill((0,0,0))
	puzzle.draw(win)
	pieces.show(win)
	pygame.display.update()


def before_start(win):
	prefont =pygame.font.SysFont("lucida", 40)
	win.fill((0,0,0))
	p= prefont.render("8 PUZZLE GAME",True,(250,239,10))
	q= prefont.render("Enter any button to play.",True,(250,89,170))
	win.blit(p,(135,100))
	win.blit(q,(90,170))
	pygame.display.update()

def main():
	pygame.init()
	shuffle(pieces)
	width= 510
	height = 500
	win = pygame.display.set_mode((width,height))
	pygame.display.set_caption("8 PUZZLE GAME (by Sritiman Adak)")
	game = True
	run = False

	while(game):
		if not run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game =False
				if event.type == pygame.KEYDOWN:
					run =True
					
		if run:	
			run =pieces.check_solved()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game =False
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					pieces.search_and_shift(pos)	
				
			draw_win(win)	
		if not run:
			puzzle.start = int(time.time())
			before_start(win)	

	pygame.quit()
	


if __name__ =="__main__":
	main()		