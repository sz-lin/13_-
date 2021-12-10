x=1
while 	True:
	password = input('請輸入密碼:')
	if password =='a123456':
		print('登入成功')
		break	
	else:
		if x < 3:
			print('密碼錯誤! 還有',3-x,'機會')
		x=x+1
		if x == 4:
			print('密碼錯誤! ')
			break