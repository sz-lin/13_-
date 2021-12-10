#最多輸入3次
#如果正確 就印出 "登入成功"
#如果不正確 就印出 "密碼錯誤! 還有_次機會"
password = '123456'
i = 3 #剩餘機會
while 	True:
	pwd = input('請輸入密碼:')
	if pwd ==password:
		print('登入成功')
		break	#跳出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有',i,'機會')
		if i == 0:
			print('密碼錯誤!機會用完了 ')
			break