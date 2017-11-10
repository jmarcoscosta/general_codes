from tkinter import *
import time 
import random


tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()



class Bar:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id = canvas.create_rectangle(0,0,100,10,fill=color)
		self.canvas.move(self.id,200,300)
		self.x = 0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
		self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
	def draw(self):
		self.canvas.move(self.id,self.x,0)
		pos = self.canvas.coords(self.id)
		if pos[0] <=0:
			self.x = 0
		if pos[2] >= self.canvas_width:
			self.x = 0 
	def turn_right(self,event):
		pos = self.canvas.coords(self.id)
		if pos[2] < self.canvas_width:
			self.x = 4
		else:
			self.x = 0		
	def turn_left(self,event):
		pos = self.canvas.coords(self.id)
		if pos[0]>0:
			self.x = -4
		else:
			self.x = 0


class Ball:
	def __init__(self,canvas,color,paddle):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10,10,25,25,fill=color)
		self.canvas.move(self.id,245,100)
		starts = [-3, -2, -1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -1
		self.hit_bottom = False
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width  = self.canvas.winfo_width()
		self.level = 1
		self.level_label = canvas.create_text((50,50),text='Nível 1')

	def draw(self):
		self.canvas.move(self.id,self.x,self.y)
		pos = self.canvas.coords(self.id)
		if pos[0] <=0:
			self.x = self.level
		if pos[1] <=0:
			self.y = self.level
		if pos[2] >= self.canvas_width:
			self.x = -self.level
		if pos[3] >= self.canvas_height:
			self.hit_bottom = True
		if self.hit_paddle(pos):
			self.level+=1
			self.y = -self.level
			self.x = self.level
			canvas.itemconfigure(self.level_label,text="Nível: {}".format(self.level))

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
		return False	

paddle = Bar(canvas,'blue')
ball = Ball(canvas,'red',paddle)


while True:
	if not ball.hit_bottom:
		ball.draw()
	paddle.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)
