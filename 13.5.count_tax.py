# count property tax

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()

		# make 4 frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.mid_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)
		
		# make variable to show in labels when press count button
		self.value = tkinter.StringVar()
		self.tax = tkinter.StringVar()
		
		# make label and enty for top frame
		self.top_price_label = tkinter.Label(self.top_frame, text='Price: ')
		self.top_entry = tkinter.Entry(self.top_frame)
		# pack top
		self.top_price_label.pack(side='left')
		self.top_entry.pack(side='left')
		
		# make labels for mid frame
		self.mid_txt_label = tkinter.Label(self.mid_frame, text='Assessed value, $: ')
		self.mid_value_label = tkinter.Label(self.mid_frame, textvariable=self.value)
		# pack mid
		self.mid_txt_label.pack(side='left')
		self.mid_value_label.pack(side='left')
		
		# make labels for bottom frame
		self.bottom_txt_label = tkinter.Label(self.bottom_frame, text='Tax, $: ')
		self.bottom_value_label = tkinter.Label(self.bottom_frame, textvariable=self.tax)
		# pack bottom
		self.bottom_txt_label.pack(side='left')
		self.bottom_value_label.pack(side='left')
		
		# make buttons for buttons frame
		self.count_button = tkinter.Button(self.button_frame, text='Count', command=self.count)
		self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
		# pack bottom
		self.count_button.pack(side='left')
		self.quit_button.pack(side='left')
		
		# pack frames
		self.top_frame.pack(side='top')
		self.mid_frame.pack(side='top')
		self.bottom_frame.pack(side='top')
		self.button_frame.pack(side='top')

		# enter main loop tkinter
		tkinter.mainloop()

		
	def count(self):
		ass_value = float(self.top_entry.get()) * 0.6
		self.value.set(ass_value)
		self.tax.set(ass_value * 0.0075)
		
	

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
