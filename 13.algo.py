# study gui with tkinter module

import tkinter
import tkinter.messagebox as msg

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()
		# make frame
		self.main_frame = tkinter.Frame(self.main_window)
		self.main_frame.pack()
		# frame for button
		self.button_frame = tkinter.Frame(self.main_window)
		self.button_frame.pack()
		# make label widget
		self.label1 = tkinter.Label(self.main_frame, text='Программировать - это круто!')
		self.label1.pack(side='left')
		self.label2 = tkinter.Label(self.main_frame, text='Hello, world!')
		self.label2.pack(side='left')
		# message window
		self.messasge = msg.showinfo('Program halted', 'Press OK, when ready')
		# make button
		self.button1 = tkinter.Button(self.button_frame, text='Calculate', command=self.calculate)
		self.button1.pack(side='left')
		# make quit button
		self.quit_button = tkinter.Button(self.button_frame, text='Exit', command=self.main_window.destroy)
		self.quit_button.pack(side='left')
		# enter main loop tkinter
		tkinter.mainloop()

	def calculate(self):
		self.messasge1 = msg.showinfo('Calculate', 'Calculations completed.')
		


def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
