# simple gui window with tkinter module with personal data

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()
		self.main_window.title('Translate')
		# make 3 frames
		self.left_frame = tkinter.Frame(self.main_window)
		self.mid_frame = tkinter.Frame(self.main_window)
		self.right_frame = tkinter.Frame(self.main_window)
		# make variable to show in labels when press show button
		self.top_word = tkinter.StringVar()
		self.mid_word = tkinter.StringVar()
		self.bottom_word = tkinter.StringVar()
		
		# make label and buttons for left frame
		self.left_empty_label = tkinter.Label(self.left_frame)
		self.top_button = tkinter.Button(self.left_frame, text='Translate', command=self.translate_top)
		self.mid_button = tkinter.Button(self.left_frame, text='Translate', command=self.translate_mid)
		self.bottom_button = tkinter.Button(self.left_frame, text='Translate', command=self.translate_bottom)
		# pack left
		self.left_empty_label.pack(side='top')
		self.top_button.pack(side='top')
		self.mid_button.pack(side='top')
		self.bottom_button.pack(side='top')
		
		# make labels for mid frame
		self.mid_header_label = tkinter.Label(self.mid_frame, text='Latin')
		self.mid_top_label = tkinter.Label(self.mid_frame, text='sinister')
		self.mid_mid_label = tkinter.Label(self.mid_frame, text='dexter')
		self.mid_bottom_label = tkinter.Label(self.mid_frame, text='medium')
		# pack mid
		self.mid_header_label.pack(side='top')
		self.mid_top_label.pack(side='top')
		self.mid_mid_label.pack(side='top')
		self.mid_bottom_label.pack(side='top')
		
		# make labels for right frame
		self.right_header_label = tkinter.Label(self.right_frame, text='English')
		self.right_top_label = tkinter.Label(self.right_frame, textvariable=self.top_word)
		self.right_mid_label = tkinter.Label(self.right_frame, textvariable=self.mid_word)
		self.right_bottom_label = tkinter.Label(self.right_frame, textvariable=self.bottom_word)
		# pack right
		self.right_header_label.pack(side='top')
		self.right_top_label.pack(side='top')
		self.right_mid_label.pack(side='top')
		self.right_bottom_label.pack(side='top')
		
		# pack frames
		self.left_frame.pack(side='left')
		self.mid_frame.pack(side='left')
		self.right_frame.pack(side='left')

		# enter main loop tkinter
		tkinter.mainloop()

		
	def translate_top(self):
		self.top_word.set('left')

		
	def translate_mid(self):
		self.mid_word.set('right')

		
	def translate_bottom(self):
		self.bottom_word.set('central')
		
	

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
