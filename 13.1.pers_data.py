# simple gui window with tkinter module with personal data

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()
		# make two frames
		self.info_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)
		# make variable to show in labels when press show button
		self.address = tkinter.StringVar()
		self.name = tkinter.StringVar()
		# make labels
		self.address_label = tkinter.Label(self.info_frame, textvariable=self.address)
		self.name_label = tkinter.Label(self.info_frame, textvariable=self.name)
		# pack labels
		self.address_label.pack(padx=20, pady=10)
		self.name_label.pack(padx=20, pady=10)
		# make buttons
		self.show_button = tkinter.Button(self.button_frame, text='Show info', command=self.just_do, borderwidth=1, relief='raised')
		self.show_button.pack(side='left')
		# make 'quit' button widget
		self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy, borderwidth=1, relief='raised')
		self.quit_button.pack(side='left')
		# pack frames
		self.info_frame.pack()
		self.button_frame.pack()
		# enter main loop tkinter
		tkinter.mainloop()
	
	def just_do(self):
			# put data into variables
			self.address.set('One LEGOLAND Way, Winter Haven, 33884')
			self.name.set('Peppa Pig')
		
	

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
