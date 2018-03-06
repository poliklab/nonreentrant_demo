"""
A prototype for buffering keyboard inputs
This concept will be used in the to sreamline threads in PyScan
Peter Timperman
"""
from collections import deque
from Tkinter import *
import time
import threading
import pdb 
root = Tk()

key_buffer = deque()
bindings_dict = dict()
block_flag = False 
def print_a():
	print "The key \'a\' was pressed" 
def print_b():
	print "The key \'b\' was pressed" 
def stop():
	block_flag = False
bindings_dict["a"]=(lambda a: print_a) 
bindings_dict["b"]=(lambda b: print_b) 
bindings_dict["s"]=(lambda stop: s) 

def empty_buffer():
	while len(key_buffer) != 0:
		key = key_buffer.popleft() 
		print key
		#pdb.set_trace()
		print bindings_dict
		bindings_dict[key]

def buffer_keys(event):
	print "buffered"

	key_buffer.append(str.replace(repr(event.char), '\'', ""))


def print_loop():
		print "entering"
		block_flag = True 
		while block_flag: 	
			print "Loooping......:)"
			time.sleep(1)
			empty_buffer()
def start_print_loop():
	p = threading.Thread(target=print_loop)
	p.start()





frame = Frame(root, width=100, height=100)
frame.bind("<a>", buffer_keys)
frame.bind("<b>", buffer_keys)
frame.bind("<s>", lambda s: buffer_keys)
frame.bind("<p>", lambda p: start_print_loop())
frame.pack()
frame.focus_set()

root.mainloop()


