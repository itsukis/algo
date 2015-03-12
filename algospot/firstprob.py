import sys

def main():
	n = sys.stdin.readline()
	for i in range(0, int(n)):
		print "Hello, %s!" % (sys.stdin.readline().strip())

if __name__ == '__main__':
	main()