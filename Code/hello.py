"""Run a Python script from the Terminal by passing it to the Interpreter."""

print("\nHello Friend!!  ...at least I didn't say World.\n")

"""edition done 18Aug 2021 """

myFav = 8

def add(num1, num2):
	result = num1+num2
	return result

def multiply(num1, num2):
	result = num1*num2
	return result


answer = input ("What's your favourite number?: ")
answer = int(answer)


if (answer < 5):
	print("\nWow! ", answer, "is also my favourite!")
	print("\nThe sum of our favourite numbers is:", add(answer,answer))
	print("The product of our favourite numbers is:", multiply(answer,answer))
else:
	print("\nThat's not my favourite!. Mine is 8")
	print("\nThe sum of our favourite numbers is:", add(myFav,answer))
	print("The product of our favourite numbers is:", multiply(myFav,answer))


print("\nBye! A pleasure to meet you!")



	


