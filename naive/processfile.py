import os
flag=False
if flag:
	for i in range(1,30):
		filename='sports'+str(i)+'.txt'
		rfile='file'+str(i)+'.txt'
		f=open(filename,'r')
		g=open(rfile,'w')
		for i in f.readlines():
			g.write(i.strip())
		g.close()
		f.close()
		os.remove(filename)
		os.rename(rfile,filename)
else:
	filename='sample'+'.txt'
	rfile='file'+'.txt'
	f=open(filename,'r')
	g=open(rfile,'w')
	for i in f.readlines():
		g.write(i.strip())
	g.close()
	f.close()
	os.remove(filename)
	os.rename(rfile,filename)