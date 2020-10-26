#!/usr/bin/python
r=input('enter the resistor value')
u=input('enter the unit:1 for ohm,2 for kiloohm,3 for megaohm')
def color_code(t,o,p):
			d={0:'black',1:'brown',2:'red',3:'orange',4:'yellow',5:'green',6:'blue',7:'violet',8:'gray',9:'white',10:'no_band'}
			print 'band1=',d[t]
			print 'band2=',d[o]
			print 'band3=',d[p]

if u==1:
		if r<10:
			flag=isinstance(r,int)
			if flag==1:
					color_code(10,r,10)
			else:
				print "invalid input"
		elif r > 9 and r <100:
	  				color_code(r/10,r%10,10)
		elif r > 99 and r < 1000:
						if r%10==0:
								color_code(r/100,((r/10)%10),1)
						else:	
							print "invalid input"
		
elif u==2:
		e=3			
		if r<10:
			flag=isinstance(r,int)
			if flag==1:
					color_code(r,0,e-1)
			else:
				r1=r*10
				color_code(int(r1)/10,int(r1)%10,e-1)
		elif r in range(10,100):
					color_code(r/10,r%10,e)
		elif r>99  and r<1000:	
					if r%10==0:
							color_code(r/100,((r/10)%10),e+1)
					else:
						print "invalid input"
					
else:
		e=6
		if r<10:
			flag=isinstance(r,int)
			if flag==1:
					color_code(r,0,e-1)
			else:
					r1=r*10
					color_code(int(r1)/10,int(r1)%10,e-1)
							
		elif r in range(10,100):
					color_code(r/10,r%10,e)
		elif r>99  and r<1000:	
					if r%10==0:
							color_code(r/100,((r/10)%10),e+1)
					else:
						print "invalid input"
		
							