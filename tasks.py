#tasks app
import sqlite3
import time

dot="new tasks?(ntask), completed a task?(comp), print tasks(ptask),delete a task?(d), view not completed tasks(nc), view completed tasks(c), add timer for task(t)???"
dotdot = raw_input(dot);
task=[];
conn=sqlite3.connect('task.db');

c = conn.cursor();

c.execute('''CREATE TABLE IF NOT EXISTS tasks (category text, task text, completed text(1), time decimal(6,2))''')
conn.commit()


while dotdot != 'stop':
	if dotdot=='new task' or dotdot=='ntask' or dotdot=='n':
		catn=raw_input('What is the category of you task?');
		taskn=raw_input('What is your task?');
		compn='n';
		tasktime=0;
		faketask=0;
		c.execute('INSERT INTO tasks VALUES (?,?,?,?,?)', (catn,taskn,compn,faketask, tasktime));
		conn.commit();
		dotdot = raw_input(dot);
	elif dotdot=='count':
		print len(task);
		dotdot = raw_input(dot);
	elif dotdot=='ptask' or dotdot=='print tasks' or dotdot=='p':
#		for item in task:
#			print item;
		for row in c.execute('select rowid, category, task, completed, tasktime from tasks'):
			print str(row)
		conn.commit();
		dotdot = raw_input(dot);
	elif dotdot=='comptask'or dotdot=='c':
		for row in c.execute('select rowid, category, task, from tasks where completed="y"'):
			print str(row)
		conn.commit();
		dotdot = raw_input(dot);
	elif dotdot=='nocomptask' or dotdot=='nc':
		for row in c.execute('select rowid, category, task, timer from tasks where completed="n"'):
			print str(row)
		conn.commit();
		dotdot = raw_input(dot);
	elif dotdot=='completed' or dotdot=='comp':
		compnum=raw_input("what task number was compeleted");
		compquery="UPDATE tasks SET completed='y' WHERE rowid=%s" %compnum
		c.execute(compquery);
		conn.commit();
		dotdot=raw_input(dot);
	elif dotdot=='d':
		delete=raw_input("which row id would you like to delete?");
		dquery = "delete from tasks where rowid= %s" % delete
		#c.execute('DELETE FROM tasks WHERE rowid=', (delete,));
		c.execute(dquery);
		conn.commit();
		dotdot = raw_input(dot);
	elif dotdot=='t':
		tin=raw_input("which row id would you like to add a timer for the task?")
		prompt=raw_input("would you like an hour prompt(1) or start a timer(2) or end a timer(3)?")
		if prompt=='1':
			stim=time.time()
			print "timer started"
			etim = time.time()
			if etim - stim == 3600:
				print "Hour has passed"
		elif prompt=='2':
			stim2=time.time()
			print "timer started"
		elif prompt=='3':
			etim2=time.time()
			print "Timer Ended"
			dtim=(etim2 - stim2)/60.0
			tquery="UPDATE tasks SET timer=%s WHERE rowid=%s" %(dtim, tin)
			c.execute(tquery);
			conn.commit();
		else:
			print "try again"
		dotdot = raw_input(dot);
	
				
				
			
		
	else:
		print "what? try again"
		dotdot = raw_input(dot);

x=0

#var_string = '?'
#var_string = ', '.join('?' * len(task))
#print var_string
#turns it into (?,?,?,?,?), must use the ? to prevent #sqlattacks
#query_string= 'INSERT INTO tasks VALUES(%s);' % var_string
#print query_string
#c.execute(query_string, (task,))
#for i in task:
#	c.execute(query_string, (task[x],))
	#normal syntax is c.executemany('INSERT INTO stocks VALUES #(?,?,?,?,?)', purchases) but  query_string replaces insert #into, task replaces purchases	
#	conn.commit()
#	x=x+1

for row in c.execute('select * from tasks'):
	print row
conn.commit()

c.close()

