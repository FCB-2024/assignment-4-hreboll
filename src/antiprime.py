import sys
## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	x = int(input("Enter a positive prime number:"))
	i = int(1)
	sum1 = int(0)
	sum2 = int(0)
	y = x - 1

	while (i <= x):
		if (x % i == 0):
			sum1 = sum1 + 1
		i = i + 1
		
	while (y >= 1 and sum2 < sum1):
		i = 1 
		sum2 = 0
		while (i <= y):
			if (y % i == 0):
				sum2 = sum2 + 1
			i = i + 1
		y = y - 1
	if (sum2 < sum1):
		res = "anti-prime"
	else:
		res = "no anti-prime"

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	return(res)

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	x = int(sys.argv[1])
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(x))
