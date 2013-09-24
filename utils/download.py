import urllib,urllib2

 
def urllib2_download(url,new_name=''):
	print "downloading with urllib2"
	f = urllib2.urlopen(url)
	data = f.read()
	with open(new_name,"wb") as op:
		op.write(data)
	print "finish with urllib2"

def urllib_download(url,new_name=''):
	print "downloading with urllib"
	urllib.urlretrieve(url, "2.pdf")
	print "downloading with urllib"
	'''
	downloading with urllib
	finished download
	[Finished in 219.7s]
	'''

def main():
	url = 'http://www.tutorialspoint.com/jsf/jsf_tutorial.pdf'
	urllib2_download(url,"3.pdf")
	
if __name__ == '__main__':
	main()
