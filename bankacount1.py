totalbalance = 0
totaldeposit = 0
answerentered = 0

reply = int(input("\nHow many transaction do you want to do? "))

while answerentered < reply:
	answer = int(input("\nDo you want to withdraw or deposit ? " +
		"press 1 to deposit and 2 to withdraw "))
	if answer == 1:
		response = 0
		while response != 2:
			deposit = int(input('Amount to deposit '))
			totaldeposit += deposit
			totalbalance += deposit
			response = int(input("\nDo you want to continue or exit? " +
			"press 1 to continue and 2 to terminate"))
		print("total amount deposited is" , totaldeposit)
	elif answer == 2:
		feedback = 0
		while feedback != 2:
			withdrawal = int(input('amount to withdraw '))
			if totalbalance < withdrawal:
				print("INSUFFICIENT FUNDS",
				"PEASE GO TO DEPOSIT TO ADD FUNDS")
			balance = totalbalance - withdrawal
			feedback = int(input("\nDo you want to continue or exit ? " +
				"press 1 to continue and 2 to terminate "))
		print("balance is " , balance)
	answerentered += 1
print('Available balance is' , totalbalance)
