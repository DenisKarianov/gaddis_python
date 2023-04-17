# count value of phone calls by using radiobuttons

import tkinter

# constants
DAY_PRICE = 10
EVENING_PRICE = 12
NIGHT_PRICE = 5


class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()

		# make 3 frames
		self.top_frame = tkinter.Frame(self.main_window)  # radiobuttons
		self.mid_frame = tkinter.Frame(self.main_window)  # entry
		self.bottom_frame = tkinter.Frame(self.main_window)  # count button and label with result info
		
		# stringvar to show value
		self.total_value = tkinter.StringVar()
		
		# intvar for radiobuttons
		self.radio_var = tkinter.IntVar()
		
		# assign 1 to intvar (first variant by default)
		self.radio_var.set(1)
		
		# make info label and radiobuttons inside top frame
		self.top_label = tkinter.Label(self.top_frame, text='Choose your call time')
		self.rb1 = tkinter.Radiobutton(self.top_frame, text='Day time (6:00-17:59)', variable=self.radio_var, value=1)
		self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening time (18:00-23:59)', variable=self.radio_var, value=2)
		self.rb3 = tkinter.Radiobutton(self.top_frame, text='Night time (0:00-5:59)', variable=self.radio_var, value=3)
		
		# pack top
		self.top_label.pack(side='top')
		self.rb1.pack(side='top')
		self.rb2.pack(side='top')
		self.rb3.pack(side='top')
		
		# make label and entry for mid frame
		self.mid_label = tkinter.Label(self.mid_frame, text="Enter minutes' quantity: ")
		self.mid_entry = tkinter.Entry(self.mid_frame)
		# pack mid
		self.mid_label.pack(side='left')
		self.mid_entry.pack(side='left')
		
		
		# make button and label for bottom frame
		self.count_button = tkinter.Button(self.bottom_frame, text='Count value', command=self.count_value)
		self.value_label = tkinter.Label(self.bottom_frame, textvariable=self.total_value)
		# pack bottom
		self.count_button.pack(side='left')
		self.value_label.pack(side='left')
		
		# pack frames
		self.top_frame.pack(side='top')
		self.mid_frame.pack(side='top')
		self.bottom_frame.pack(side='top')

		# enter main loop tkinter
		tkinter.mainloop()

		
	def count_value(self):
		total = 0.0
		l = float(self.mid_entry.get())
		if self.radio_var.get() == 1:
			total = l * DAY_PRICE
		elif self.radio_var.get() == 2:
			total = l * EVENING_PRICE
		elif self.radio_var.get() == 3:
			total = l * NIGHT_PRICE
		self.total_value.set(f'${total}')
		
	

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
