from kandinsky import*
ci=''
i=0
rl=0
stop=False
if ci[0]=='0':cc='1'
else:cc='0'
for x in range(320):
	for y in range(240):
		if stop:break
		if rl==0:
			if cc=='0':cc='1'
			else:cc='0'
			try:
				num_str=''
				while ci[i]!='|':num_str+=ci[i];i+=1
				i+=1;rl=int(num_str)
			except:stop=True;break
		rl-=1
		if cc=='0':set_pixel(x,y,(0,0,0))
