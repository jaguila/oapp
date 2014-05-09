import Tkinter
from tasksclass import tasks
import sqlite3
import time
import thread


class tasksapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		#must always initialize your imported classes first
		self.tasks=tasks()
		self.initialize()
		self.conn=sqlite3.connect('task.db')
		self.c=self.conn.cursor()
		
	

	def initialize(self):
	#setup layout of grid	
		self.grid()
		#create widgets
		self.messageinit=Tkinter.Message(self,text="Welcome to the task app", relief=Tkinter.RAISED, width=100)
		self.messageinit.grid(column=0, row=0, sticky='EW')
#		self.messageinit.pack()
		
		
		#task list
		self.var1=Tkinter.StringVar()
		self.message1=Tkinter.Message(self,textvariable=self.var1, relief=Tkinter.RAISED, width=100)
		self.message1.grid(column=1, row=0, sticky='EW')
		self.var1.set("tasks?")
#		self.message1.pack()
		
		#entry
		#tasks.new_t(self.entry)
		self.label=Tkinter.Label(self, text="Category")
		self.entry=Tkinter.Entry(self)
		self.var2=Tkinter.StringVar()
		self.label.grid(column=0, row=1, sticky='EW')
		self.entry.grid(column=1, row=1, sticky='EW')
		self.entry.bind("<Return>",self.OnButtonClick1)
#		self.entry.pack()

		#fake button

	#	self.b.pack()		
		
		#entry2
		self.labelentry2=Tkinter.Label(self, text='Task')
		self.entry2=Tkinter.Entry(self)
		self.labelentry2.grid(column=0, row=2, sticky='EW')
		self.entry2.grid(column=1, row=2, sticky='EW')
		
		#submit new tasks
		self.submit=Tkinter.Button(self, text='submit new', width=10, command=self.OnButtonSubmit)
		self.submit.grid(column=2, row=2, sticky='EW')
		
		#Complete entry
		self.labelentry3=Tkinter.Label(self, text='Rowid(for completed or Delete)')
		self.entry3=Tkinter.Entry(self)
		self.labelentry3.grid(column=0, row=3, sticky='EW')
		self.entry3.grid(column=1, row=3, sticky='EW')
		comprow=self.entry3.get()
		self.button3=Tkinter.Button(self, text="Comp", width=5, command=self.Compbutton)
		self.button3.grid(column=2, row=3, sticky='EW')
		self.button4=Tkinter.Button(self, text="Del", width=5, command=self.Delbutton)
		self.button4.grid(column=3, row=3, sticky='EW')		
		
		
		#self.entry2.pack()
		
		#submit button

		self.b=Tkinter.Button(self, text="refresh list", width=10, command=self.OnButtonP)
		self.b.grid(column=0, row=6, sticky='EW')
		#self.submit.pack()
		#print entry
		
		#stretch button
		self.b2=Tkinter.Button(self, text="Stretch reminder", width=10, command=self.stretch)
		self.b2.grid(column=1, row=6, sticky='EW')
		
		#self.message2=Tkinter.Message(self, width=10, text=self.entry.get())
		#self.message2.grid(row=5, column=1, sticky='EW')	
		self.resizable(True, True)

	def makemessage(self,tkinst, **options):
		message=Tkinter.Message(tkinst, **options)
		message.pack()
		return message

		
	def OnButtonClick1(self):
		new=self.makemessage(text=self.entry.get())
		return new
	def OnButtonSubmit(self):		
		sub=self.tasks.new_t(self.entry.get(),self.entry2.get())
		self.entry.delete(0, Tkinter.END)
		self.entry2.delete(0, Tkinter.END)
		return sub
	def OnButtonP(self):
		self.conn.text_factory = str
		self.c.execute('select rowid, category, task, time from task WHERE completed="n"')
		#c.execute('select rowid, category, task, completed, tasktime from tasks')
		root=Tkinter.Tk()
		root.wm_title("Current not completed task list")
		p=self.c.fetchall()
	

		
		i=1
		for row in p:
			#n=self.makemessage(text=row)
			rlabel=self.makemessage(root,text='rowid', width=100)
			rlabel.grid(column=0, row=0)
			catlabel=self.makemessage(root,text='category', width=100)
			catlabel.grid(column=1, row=0)
			tlabel=self.makemessage(root,text='task')
			tlabel.grid(column=2, row=0)
			tmlabel=self.makemessage(root,text='time')
			tmlabel.grid(column=3, row=0)
			
			j=0
			for	tup in row:

				n=self.makemessage(root, text=row[j], width=100)
				n.grid(column=j, row=i)
				j=j+1
			i=i+1
		root.mainloop()
		
		return p
		
	def stretch(self):
		thread.start_new_thread(self.delay,(2,))
		#root2.wm_title("Stretch reminder")
		#Tkinter.Message(root2,text="stuff")
		#thread.start_new_thread(root2.destroy, )
		#root2.mainloop()
		
	def delay(self, secs):
		time.sleep(secs)
		root2=Tkinter.Tk()
		root2.after(2000, root2.destroy)
		#root2.wm_title("Stretch reminder")
		#time.sleep(secs)
		#root2.destroy()
		root2.mainloop()

		
	def Compbutton(self):
		comp=self.tasks.comp_t(self.entry3.get())
		self.entry3.delete(0, Tkinter.END)
		return comp
	
	def Delbutton(self):
		delbut=self.tasks.delete_t(self.entry3.get())
		self.entry3.delete(0, Tkinter.END)
		return delbut
	
	def hrbutton(self):
		self.stopsig=0
		if self.stopsig==0:
			time.sleep(5)
			self.root2=Tkinter.Tk()
			self.root2.wm_title("Stretch reminder")
			hr1=self.makemessage(self.root2,text='Get up and stretch', width=100)
			hr2=Tkinter.Button(self.root2, text="Stretched?", width=10, command=(self.hrstop("Y")))
			hr3=Tkinter.Button(self.root2, text="Not Stretched?", width=10, command=(self.hrstop("N")))
			hr1.grid(column=0, row=0)
			hr2.grid(column=0, row=1)
			hr3.grid(column=1, row=1)
			self.root2.mainloop()


	def hrstop(self, ans):
		self.tasks.str_t(ans)
		
		
		
		
		
#	def listtable(self):
#		self.table=

if __name__=="__main__":
	app=tasksapp_tk(None)
	#app=thread.start_new_thread(tasksapp_tk,(None,))
	app.title('task app')
	app.mainloop()
	