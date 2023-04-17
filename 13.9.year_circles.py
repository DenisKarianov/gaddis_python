# paint tree year circles by using canvas

import tkinter

# constants
YEARS = 5
CAN_WIDTH = 1000
CAN_HEIGHT = 1000
KOEF = 20

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()

		# make canvas widget
		self.canvas = tkinter.Canvas(self.main_window, width=CAN_WIDTH, height=CAN_HEIGHT)
		# draw tree circles
		for i in range(YEARS + 1):
			self.canvas.create_oval(CAN_WIDTH / 2 - CAN_WIDTH / 2 / KOEF * (i + 1), CAN_HEIGHT / 2 - CAN_HEIGHT / 2 / KOEF * (i + 1),
									CAN_WIDTH / 2 + CAN_WIDTH / 2 / KOEF * (i + 1), CAN_HEIGHT / 2 + CAN_HEIGHT / 2 / KOEF * (i + 1))
			if i != YEARS:  # condition to not draw year number on outer circle
				self.canvas.create_text(CAN_WIDTH / 2 - CAN_WIDTH / 2 / KOEF * (i + 1), (CAN_HEIGHT / 2 - CAN_HEIGHT / 2 / KOEF * (i + 1)) 
								   + (((CAN_HEIGHT / 2 + CAN_HEIGHT / 2 / KOEF * (i + 1)) - (CAN_HEIGHT / 2 - CAN_HEIGHT / 2 / KOEF * (i + 1))) / 2), 
								   text=i + 1, anchor=tkinter.W)
			
		
		# pack canvas
		self.canvas.pack()

		# enter main loop tkinter
		tkinter.mainloop()
		
	
def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
