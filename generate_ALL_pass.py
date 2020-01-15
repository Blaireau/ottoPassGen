alphabet = 'qw2rty534plkjhgfds1zxcvbnm'
alpha_dict = {'q':0,'w':1,'2':2,'r':3,'t':4,'y':5,'5':6,'3':7,'4':8,'p':9,'l':10,'k':11,'j':12,'h':13,'g':14,'f':15,'d':16,'s':17,'1':18,'z':19,'x':20,'c':21,'v':22,'b':23,'n':24,'m':25}
list_out = open("full_pass_list","w")

def reduction(my_letter):
	while my_letter >= 0:
		my_letter = my_letter-26
	return my_letter+26

for letter1 in alphabet:
	for letter2 in alphabet:
		for letter3 in alphabet:
			for letter4 in alphabet:
				for letter5 in alphabet:
					a = alpha_dict[letter1]
					b = alpha_dict[letter2]
					c = alpha_dict[letter3]
					d = alpha_dict[letter4]
					e = alpha_dict[letter5]
					a = reduction(a)
					b = reduction(b+a)
					c = reduction(b+c)
					d = reduction(d+c)
					
					if d==e:
						list_out.write(letter1+letter2+letter3+letter4+letter5+'\n')

list_out.close()
