from tkinter import *
from tkinter.messagebox import *
root = Tk()

def about():
	showinfo("About","Guise Your Gender version 1.0")
	
def author():
	showinfo('Author','This App is made by Md. Almas Ali\n\tin Bangladesh')

mainmenu = Menu(root)
mainmenu.add_command(label='About', command=about)
#mainmenu.add_separator()
mainmenu.add_command(label='Author', command=author)
mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)


def nameTest():
	if name.get() == '':
		showinfo('Result','You haven’t enter anyname in box. ')
	try:
		nam = name.get().lower()
		enm = nam[-1]
		enm2 = nam[-2:]
		enm3 = nam[-3:]
	except:
		pass
	else:
		if enm == 'a':
			showinfo('Result','You are Female.')
		elif enm == 'b':
			showinfo('Result','You are Male.')
		elif enm == 'c':
			showinfo('Result','You are Male. ')
		elif enm == 'd':
			showinfo('Result','You are Male. ')
		elif enm == 'e':
			if nam == 'rone':
				showinfo('Result','You can be Male/Female.')
			else:
			    showinfo('Result','You are Male.')
		elif enm == 'f':
			showinfo('Result','You are *Male. ')
		elif enm == 'g':
			showinfo('Result','You are *Male. ')
		elif enm == 'h':
			showinfo('Result','You are *Male. ')
		elif enm == 'i':
			if nam == 'roni':
				showinfo('Result','You can be Male/Female.')
			elif nam == 'ali':
				showinfo('Result','You are Male.')
			else:
				showinfo('Result','You are Female. ')
		elif enm == 'j':
			showinfo('Result','You are *Male. ')
		elif enm == 'k':
			showinfo('Result','You are *Male. ')
		elif enm == 'l':
			showinfo('Result','You are Male.')
		elif enm == 'm':
			if nam == 'mim':
				showinfo('Result','You can be Male/Female.')
			elif enm3 == 'mim':
				showinfo('Result','You can be Female.')
			else:
				showinfo('Result','You are *Male. ')
		elif enm == 'n':
			if enm3 == 'lin':
				showinfo('Result','You are Female')
			elif enm3 == 'rin':
				showinfo('Result','You are Female')
			else:
				showinfo('Result','You are Male')
		elif enm == 'o':
			showinfo('Result','You are Male. ')
		elif enm == 'p':
			showinfo('Result','You are *Male. ')
		elif enm == 'q':
			showinfo('Result','You are *Male. ')
		elif enm == 'r':
			if nam == 'nur':
				showinfo('Result','You are Male. ')
			else:
				showinfo('Result', 'You are male.')
		elif enm == 's':
			showinfo('Result','You are Male. ')
		elif enm == 't':
			showinfo('Result','You are *Male. ')
		elif enm == 'u':
			showinfo('Result','You are Female. ')
		elif enm == 'v':
			showinfo('Result','You are *Male. ')
		elif enm == 'w':
			showinfo('Result','You are *Male. ')
		elif enm == 'x':
			showinfo('Result','You are *Male. ')
		elif enm == 'y':
			if nam == 'rony':
				showinfo('Result','You can be Male/Female.')
			else:
				showinfo('Result','You are Female.')
		elif enm == 'z':
			showinfo('Result','You are Male. ')
		else:
			showinfo('Result','Error Name! ')
	

root.title('Guise Your Gender ')
root.geometry("500x400")

f1 = Frame(root, bg="lightblue", borderwidth=6, relief=SUNKEN)
f1.pack(side='top', fill='x')

f2 = Frame(root, bg='black')
f2.pack(side='bottom',fill="x")

f3 = Frame(root, bg='lightblue')
f3.pack(side='top',fill='both')

Label(f1, text='Guise Your Gender', fg='blue', bg="lightblue", font="Arial 18 bold").pack(padx=20,pady=40)

Label(f1, text='Enter Your Name : ', bg="lightblue", font='Arial 8 bold', fg='orange').pack(pady=20)

Label(f2, text="© Copyright collected by Md. Almas Ali.",fg='red', bg='black', font="Arial 8 bold").pack()

name = StringVar()
Entry(f1, textvariable=name, bg='lightblue',fg='red', font="Arial 8 italic").pack()
Button(f1, text='Test', bg='red', fg='white', command=nameTest).pack(pady=30)

photo = PhotoImage(file='./img/author.png')
Label(f3, image=photo).pack()

Label(f3, text='Md. Almas Ali', font='Arial 10', fg='darkblue', bg='lightblue').pack(pady=8)

Label(f3, text='Diploma in Engineering in Computer Technology', fg='darkblue', bg='lightblue', font='Arial 6').pack()

Label(f3, text='2nd Semester, 2nd Shift', fg='darkblue', bg='lightblue', font='Arial 6').pack()

Label(f3, text='Chapai Nawabganj Polytechnic Institute, Chapai Nawabganj.', fg='darkblue', bg='lightblue', font='Arial 6').pack()

Label(f3, text='Contact: almaspr3@gmail.com', fg='darkblue', bg='lightblue', font='Arial 6').pack()

root.mainloop()