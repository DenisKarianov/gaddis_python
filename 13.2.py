# empty gui window with tkinter module

import tkinter
import tkinter.messagebox as msg

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()
		# make 'press' button widget
		self.my_button = tkinter.Button(self.main_window, text='Press me!', command=self.just_do, borderwidth=1, relief='raised')
		self.my_button.pack()
		# make 'quit' button widget
		self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy, borderwidth=1, relief='raised')
		self.quit_button.pack()
		# enter main loop tkinter
		tkinter.mainloop()
		
	def just_do(self):
		# show info window
		msg.showinfo("Reaction", "Thanks for pressing!")

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
