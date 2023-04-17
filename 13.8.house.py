# paint house by using canvas

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()

		# make canvas widget
		self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
		# draw house
		self.canvas.create_rectangle(30, 120, 130, 180)
		# roof
		self.canvas.create_line(30, 120, 80, 90)
		self.canvas.create_line(80, 90, 130, 120)
		# door
		self.canvas.create_rectangle(75, 150, 85, 170)
		# windows
		self.canvas.create_rectangle(45, 140, 60, 155)
		self.canvas.create_rectangle(100, 140, 115, 155)
		# ladder
		self.canvas.create_rectangle(70, 170, 90, 180)
		self.canvas.create_line(70, 175, 90, 175)
		
		# pack canvas
		self.canvas.pack()

		# enter main loop tkinter
		tkinter.mainloop()
		
	
def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
