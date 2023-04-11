# study gui with tkinter module

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()
		# make canvas widget
		self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
		# make some line
		self.canvas.create_line(0, 0, 199, 199, width=3, fill='blue')
		# rectangle
		self.canvas.create_rectangle(50, 50, 100, 100, fill='black', outline='red')
		# circle
		self.canvas.create_oval(50, 50, 150, 150, fill='green')
		# arc
		self.canvas.create_arc(20, 20, 180, 180, start=0, extent=90, fill='blue')
		# pack
		self.canvas.pack()
		# enter main loop tkinter
		tkinter.mainloop()

		


def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
