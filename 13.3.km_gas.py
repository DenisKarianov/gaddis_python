# count gasoline consumption per 1 km

import tkinter

class MyGUI:
	def __init__(self):
		# make main window widget
		self.main_window = tkinter.Tk()
		self.main_window.title('km/l')
		# make 3 frames
		self.top_frame = tkinter.Frame(self.main_window)
		self.mid_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		# make variable to show in labels when press calculate button
		self.result = tkinter.StringVar()
		
		# make label and enty for top frame
		self.top_txt_label = tkinter.Label(self.top_frame, text='Full tank, l ')
		self.top_entry = tkinter.Entry(self.top_frame)
		# pack top
		self.top_txt_label.pack(side='left')
		self.top_entry.pack(side='left')
		
		# make label and entry for mid frame
		self.mid_txt_label = tkinter.Label(self.mid_frame, text='Full tank, km ')
		self.mid_entry = tkinter.Entry(self.mid_frame)
		# pack mid
		self.mid_txt_label.pack(side='left')
		self.mid_entry.pack(side='left')
		
		# make button and label for bottom frame
		self.calc_button = tkinter.Button(self.bottom_frame, text='Count', command=self.count)
		self.result_label = tkinter.Label(self.bottom_frame, textvariable=self.result)
		# pack bottom
		self.calc_button.pack(side='left')
		self.result_label.pack(side='left')
		
		# pack frames
		self.top_frame.pack(side='top')
		self.mid_frame.pack(side='top')
		self.bottom_frame.pack(side='top')

		# enter main loop tkinter
		tkinter.mainloop()

		
	def count(self):
		gas = float(self.top_entry.get())
		km = int(self.mid_entry.get())
		self.result.set(f'{km / gas} km for 1 litre.')
		
	

def main():
	my_gui = MyGUI()



# Call the main function.
if __name__ == '__main__':
	main()
