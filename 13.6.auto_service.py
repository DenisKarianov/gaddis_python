# count value of auto services by using checkbuttons

import tkinter

# constants
OIL_CHANGE = 500
LUBRICATION_WORK = 300
FLUSH_RADIATOR = 700
TRANSMISSION_FLUID_CHANGE = 1000
CHECKUP = 800
MUFFLER_REPLACEMENT = 1300
TIRE_SWAP = 1300


class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()

		# make 2 frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)
		
		# stringvar to show costs
		self.total_value = tkinter.StringVar()
		
		# make intvars for checkbuttons
		self.cb_var1 = tkinter.IntVar()
		self.cb_var2 = tkinter.IntVar()
		self.cb_var3 = tkinter.IntVar()
		self.cb_var4 = tkinter.IntVar()
		self.cb_var5 = tkinter.IntVar()
		self.cb_var6 = tkinter.IntVar()
		self.cb_var7 = tkinter.IntVar()
		
		# assign 0 to intvars
		self.cb_var1.set(0)
		self.cb_var2.set(0)
		self.cb_var3.set(0)
		self.cb_var4.set(0)
		self.cb_var5.set(0)
		self.cb_var6.set(0)
		self.cb_var7.set(0)
		
		# make checkbuttons inside top frame
		self.cb1 = tkinter.Checkbutton(self.top_frame, text='Oil change', variable=self.cb_var1)
		self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lubrication work', variable=self.cb_var2)
		self.cb3 = tkinter.Checkbutton(self.top_frame, text='Flushing the radiator', variable=self.cb_var3)
		self.cb4 = tkinter.Checkbutton(self.top_frame, text='Transmission fluid change', variable=self.cb_var4)
		self.cb5 = tkinter.Checkbutton(self.top_frame, text='Checkup', variable=self.cb_var5)
		self.cb6 = tkinter.Checkbutton(self.top_frame, text='Muffler replacement', variable=self.cb_var6)
		self.cb7 = tkinter.Checkbutton(self.top_frame, text='Tire swapping', variable=self.cb_var7)
		# pack top
		self.cb1.pack(side='top')
		self.cb2.pack(side='top')
		self.cb3.pack(side='top')
		self.cb4.pack(side='top')
		self.cb5.pack(side='top')
		self.cb6.pack(side='top')
		self.cb7.pack(side='top')
		
		
		# make button and label for buttons frame
		self.show_button = tkinter.Button(self.button_frame, text='Show costs', command=self.show_costs)
		self.total_label = tkinter.Label(self.button_frame, textvariable=self.total_value)
		# pack bottom
		self.show_button.pack(side='left')
		self.total_label.pack(side='left')
		
		# pack frames
		self.top_frame.pack(side='top')
		self.button_frame.pack(side='top')

		# enter main loop tkinter
		tkinter.mainloop()

		
	def show_costs(self):
		total = 0.0
		if self.cb_var1.get() == 1:
			total += OIL_CHANGE
		if self.cb_var2.get() == 1:
			total += LUBRICATION_WORK
		if self.cb_var3.get() == 1:
			total += FLUSH_RADIATOR
		if self.cb_var4.get() == 1:
			total += TRANSMISSION_FLUID_CHANGE
		if self.cb_var5.get() == 1:
			total += CHECKUP
		if self.cb_var6.get() == 1:
			total += MUFFLER_REPLACEMENT
		if self.cb_var7.get() == 1:
			total += TIRE_SWAP
		self.total_value.set(total)
		
	

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
