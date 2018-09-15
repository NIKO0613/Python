current_users=['admin', 'brother', 'wst', 'txz', 'ym', 'lbs', 'sister']
new_users=['sister', 'brother', 'father', 'mother', 'gradmother']
for new_user in new_users:
	leap=0
	for current_user in current_users:
		if current_user ==new_user:
			leap=1
	if leap==0:
		print(new_user+"\tthis user name don't use!")
	elif leap==1:
		print(new_user+'\tthis user name has used!\t'+'please input others users!')
