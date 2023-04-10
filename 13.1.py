# empty gui window with tkinter module

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()
		# make widget Label1
		self.label1 = tkinter.Label(self.main_window, text="Hello, world!", borderwidth=1, relief='raised')
		# make widget Label2
		self.label2 = tkinter.Label(self.main_window, text="It's my GUI program.", borderwidth=1, relief='solid')
		# call widget Label's method pack
		self.label1.pack(padx=20, pady=20, ipadx=20, ipady=20)
		self.label2.pack(ipadx=20, ipady=20)
		# enter main loop tkinter
		tkinter.mainloop()

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
