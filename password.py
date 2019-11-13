password = 'a123456'
i = 3
while True:
	psd = input('請輸入密碼：')
	if psd == password:
		print('登入成功！！')
		break
	else:
		i = i -1
		print('密碼錯誤，還剩', i , '次機會！')
		if i == 0:
			break