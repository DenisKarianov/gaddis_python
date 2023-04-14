# convert celsius to farenheit

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()

		# make 3 frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.mid_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		# make variable to show in labels when press convert button
		self.faren = tkinter.StringVar()
		
		# make label and enty for top frame
		self.top_txt_label = tkinter.Label(self.top_frame, text='Celsius: ')
		self.top_entry = tkinter.Entry(self.top_frame)
		# pack top
		self.top_txt_label.pack(side='left')
		self.top_entry.pack(side='left')
		
		# make labels for mid frame
		self.mid_txt_label = tkinter.Label(self.mid_frame, text='Farenheit: ')
		self.mid_result_label = tkinter.Label(self.mid_frame, textvariable=self.faren)
		# pack mid
		self.mid_txt_label.pack(side='left')
		self.mid_result_label.pack(side='left')
		
		# make buttons for bottom frame
		self.convert_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
		# pack bottom
		self.convert_button.pack(side='left')
		self.quit_button.pack(side='left')
		
		# pack frames
		self.top_frame.pack(side='top')
		self.mid_frame.pack(side='top')
		self.bottom_frame.pack(side='top')

		# enter main loop tkinter
		tkinter.mainloop()

		
	def convert(self):
		celsius = float(self.top_entry.get())
		faren = 9 * celsius / 5 + 32
		self.faren.set(f'{faren} degrees')
		
	

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
