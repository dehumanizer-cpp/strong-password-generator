import string,random,os


txt_name=input("txt name>>>")
loop=int(input("loop>>>"))#amount of password
leng=int(input("password length>>>"))

k=[string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation]

txt=open(f"{txt_name}.txt","a+")


for y in range(loop):
	password=""
	for i in range(leng):
		value=random.choice(k)

		password+=value[random.randint(0,len(value)-1)]
	txt.write(password+"\n")
	
	print(password)

os.startfile(f"{txt_name}.txt")
txt.close()
