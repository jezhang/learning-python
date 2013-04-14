f = open('data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()


f = open('data.txt')

for line in f.readlines():
	print(line)
f.seek(0)
text = f.read()
print(text)
f.close()

print(text.split())