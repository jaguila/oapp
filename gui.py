#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter

#start of app
class simpleapp_tk(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

#creates all the gui elements. pass does nothing
	def initialize(self):
#sets up layout
		self.grid()
		#create widget then add it to layout manager(grid)
		self.entry=Tkinter.Entry(self)
		#sticky is saying wheree it goes EW=east west
		self.entry.grid(column=0,row=0,sticky='EW')
		#bind certain keystrokes
		self.entry.bind("<Return>", self.OnPressEnter)
		
		button = Tkinter.Button(self, text=u"Click me!", command=self.OnButtonClick)
		button.grid(column=1, row=0)
		
		#label, text alignment:anchor=left alightned, fg=foreground bg=background
		label = Tkinter.Label(self, anchor="w", fg="white", bg="blue")
		label.grid(column=0, row=1,columnspan=2,sticky='EW')
		
		#will resize
		self.grid_columnconfigure(0,weight=1)
		#prevent vertical resizing
		self.resizable(True,False)
	#	self.dialog=Pmw.SelectionDialog(self, title)
		
		
	def OnButtonClick(self):
		print "You clicked the button!"
		
	def OnPressEnter(self,event):
		print "You pressed enter !"
		
if __name__ =="__main__":
	app = simpleapp_tk(None)
	app.title('myapplication')
	#tells the program to loop until something happens)
	app.mainloop()
	
	
		