from random import randint

print("Nhập Dam, La, Keo:")
player = input()

computer = randint(0,2)

if computer == 0:
	computer = "Dam"

if computer == 1:
	computer = "La"

if computer == 2:
	computer = "Keo"

input("---")
input("You choose: " + player)
input("Computer chooses: " + computer)
input("---")

if player == computer:
	print("Hòa")

else:
	if player == "Dam":
		if computer == "Keo":
			print("Bạn thắng")
		else:
			print("Bạn thua")

	elif player == "La":
		if computer == "Dam":
			print("Bạn thắng")
		else:
			print("Bạn thua")

	elif player == "Keo":
		if computer == "Dam":
			print("Bạn thua")
		else:
			print("Bạn thắng")

	else: 
		print("Nhập sai!")