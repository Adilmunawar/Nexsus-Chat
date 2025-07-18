try:
	with open("status.md" , "r") as f:
		text = f.readline()
		num = [int(x) for x in text.split() if x.isdigit()][0]
		num += 1
	
	if num<= 1024:
		with open("status.md" , 'w') as f:
			if num in range(16):
				
