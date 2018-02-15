from argparse import ArgumentParser

def main():
	ap = ArgumentParser()

	ap.add_argument('-a', '--add', type = int, nargs = '*', help = 'add all numbers')
	ap.add_argument('-m', '--minus', type = int, nargs = '*', help = 'minus numbers')
	ap.add_argument('-mu', '--multiply', type = int, nargs = '*', help = 'multiply all numbers')
	ap.add_argument('-d', '--divide', type = int, nargs = '*', help = 'dvide numbers')
	ap.add_argument('-p', '--percent', type = int, nargs = '*', help = 'num percent')
	ap.add_argument('-s', '--square', type = int, nargs = '*', help = 'square number')
	ap.add_argument('-r', '--root', type = int, nargs = '*', help = 'squared root of number')
	ap.add_argument('-l', '--ln', type = int, nargs = '*', help = 'natural log of number')

	args = ap.parse_args()

	if args.add != None:
		print("add")
	elif args.minus != None:
		print("minus")
	elif args.multiply != None:
		print("multiply")
	elif args.divide !=None:
		print("divide")
	elif args.percent != None:
		print("percent")
	elif args.square != None:
		print("square")
	elif args.root != None:
		print("root")
	elif args.ln != None:
		print("ln")


if __name__ == "__main__":
	# calling the main function
	main()