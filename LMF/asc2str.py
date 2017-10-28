def asc2str(asc_num):
	r_str = ''
	t_str = ''
	i = 0
	while(i != len(asc_num)):
		if asc_num[i] == '1':
			t_str += asc_num[i]
			t_str += asc_num[i+1]
			t_str += asc_num[i+2]
			i = i+3
			r_str +=chr(int(t_str))
			t_str = ''
		else:
			t_str += asc_num[i]
			t_str += asc_num[i+1]
			i = i+2
			r_str += chr(int(t_str))
			t_str = ''
	return r_str