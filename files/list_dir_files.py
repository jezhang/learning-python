import os

dir = 'C:\\Windows\\System32\\drivers'
for root,dirs,files in os.walk(dir):
	for filespath in files:		
		print(os.path.join(root,filespath))