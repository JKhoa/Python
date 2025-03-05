from tkinter import *

# globally declare the expression variable 
expression = ""

# Function to update expression 
def press(num): 
	global expression 
	expression = expression + str(num)
	equation.set(expression)

# Function to evaluate the final expression 
def equalpress(): 
	try: 
		global expression 
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except: 
		equation.set(" error ")
		expression = ""

# Function to clear the contents of text entry box 
def clear(): 
	global expression 
	expression = ""
	equation.set("")

# Function to remove the last character from the expression
def back():
	global expression
	expression = expression[:-1]
	equation.set(expression)

# Function to close the application
def close():
	gui.destroy()

if __name__ == "__main__": 
	gui = Tk() 
	gui.configure(background="#99E6A6") 
	gui.title("Calculator") 
	gui.geometry("270x150") 
	equation = StringVar() 
	expression_field = Entry(gui, textvariable=equation) 
	expression_field.grid(columnspan=4, ipadx=70)

	buttons = [
		('Clear', clear, 1, 0),
		('Back', back, 1, 1),
		('', None, 1, 2),
		('Close', close, 1, 3),
		('7', lambda: press(7), 2, 0),
		('8', lambda: press(8), 2, 1),
		('9', lambda: press(9), 2, 2),
		('/', lambda: press('/'), 2, 3),
		('4', lambda: press(4), 3, 0),
		('5', lambda: press(5), 3, 1),
		('6', lambda: press(6), 3, 2),
		('*', lambda: press('*'), 3, 3),
		('1', lambda: press(1), 4, 0),
		('2', lambda: press(2), 4, 1),
		('3', lambda: press(3), 4, 2),
		('-', lambda: press('-'), 4, 3),
		('0', lambda: press(0), 5, 0),
		('.', lambda: press('.'), 5, 1),
		('=', equalpress, 5, 2),
		('+', lambda: press('+'), 5, 3)
	]

	for (text, command, row, col) in buttons:
		Button(gui, text=text, fg='black', bg='lightgrey',
			command=command, height=1, width=7).grid(row=row, column=col)

	gui.mainloop()
