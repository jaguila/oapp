#redo of task with classes
import sqlite3
import time
import datetime
class tasks:
	def __init__(self):
#		self.ques=raw_input("new tasks?(ntask), completed a task?(comp), print tasks(ptask),delete a task?(d), view not completed tasks(nc), view completed tasks(c), add timer for task(t)???")
		self.conn=sqlite3.connect('task.db');
		self.c=self.conn.cursor();
		self.c.execute('''CREATE TABLE IF NOT EXISTS task (category text, task text, completed text(1), time decimal(6,2), hrup decimal(6,2))''')
		self.c.execute('''CREATE TABLE IF NOT EXISTS str (date int, time int, hrup char(2))''')
		self.conn.commit()

		
	def new_t(self,catn,taskn):
#		catn=raw_input('What is the category of your task?');
		#catn="j2"
#		taskn=raw_input('what is your task?')
#		taskn='j'
		compn='n';
		timen=0;
		hrupn=0;
	 	self.c.execute('INSERT INTO task VALUES(?,?,?,?)', (catn, taskn,compn,timen));
		self.conn.commit();
		
	def p_t(self):
		self.c.execute('select * from task')
		self.table=[]
		rows=self.c.fetchall()
		for row in rows:
			self.table.append(t[1])
		return self.table
		
			
	def comp_t(self,rowid):
		comp="UPDATE task SET completed='y' WHERE rowid= %s" % rowid
		self.c.execute(comp);
		self.conn.commit();
	
	def delete_t(self, rowid):
		delete="DELETE FROM task WHERE rowid= %s" %rowid
		self.c.execute(delete)
		self.conn.commit();
	
	def str_t(self,str_ans):
		daten=time.strftime("%d/%m/%Y")
		timen=time.strftime("%H:%M:%S")
		strn=str_ans
		self.c.execute('INSERT INTO str VALUES(?,?,?)',(daten, timen, strn));
		self.conn.commit();
		
		
	
		
		
	def poop(self):
		print "poop"
#		print "task %s has been created" %catn
#		quest=self.ques
#		return quest
#	def run(self):
#		quest=self.ques
#		if quest=='n':
#			print "new task"
#		elif quest=='t':
##			print "time"
#		else:
#			print "ok"
##			


d=tasks()
d

#d.quest()
#d.run()
#d.ques


