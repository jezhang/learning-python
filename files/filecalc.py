import hashlib
import os,sys

def calc_sha1(filepath):
	with open(filepath,'rb') as f:
		sha1 = hashlib.sha1()
		sha1.update(f.read())
		hash = sha1.hexdigest()
		print(hash)
		return hash

def calc_md5(filepath):
	with open(filepath,'rb') as f:
		md5 = hashlib.md5()
		md5.update(f.read())
		hash = md5.hexdigest()
		print(hash)
		return hash

def main():
	for item in sys.argv:
		print item
	if len(sys.argv) == 2:
		hashfile = sys.argv[1]		
		if not os.path.exists(hashfile):
			hashfile = os.path.join(os.path.dirname(__file__),hashfile)
			if not os.path.exists(hashfile):
				print("can not found the file: %s" %hashfile)
			else:
				calc_md5(hashfile)
				calc_sha1(hashfile)
		else:
			calc_md5(hashfile)
			calc_sha1(hashfile)
	else:
		print("no filename entered.")

if __name__ == '__main__':
	main()

