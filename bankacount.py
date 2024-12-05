
totaldeposit = 0

reply = int(input("How many transaction do you want to do? "))

while answerentered <= reply:
	answerentered = int(input('enter response '))	
	answer = int(input("Do you want to withdraw or deposit ? " +
		"press 1 to deposit and 2 to withdraw "))
	if answer == 1:
		print("Continue to deposit press 0 ")
		response = int(input())
		while response != 2:
			deposit = int(input('Amount to deposit '))
			totaldeposit += deposit
			response = int(input("Do you want to continue or exit? " +
			"press 1 to continue and 2 to terminate"))
		print(totaldeposit)
	elif answer == 2:
		print("Continue to withdrawal press 0")
		feedback = int(input())
		while feedback != 2:
			withdrawal = int(input('amount to withdraw '))
			balance = totaldeposit - withdrawal
			feedback = int(input("Do you want to continue or exit ? " +
				"press 1 to continue and 2 to terminate "))
	print("balance is " , balance)
	
print('Total deposit is' , totaldeposit)
