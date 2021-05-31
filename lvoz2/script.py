import random
from browser import document
def main():
    for i in range (999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        for s in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
		colour = "#"
		for c in range(6):
			x = random.randrange(15)
			if x == 0:
				r = "0"
			if x == 1:
				r = "1"
			if x == 2:
				r = "2"
			if x == 3:
				r = "3"
			if x == 4:
				r = "4"
			if x == 5:
				r = "5"
			if x == 6:
				r = "6"
			if x == 7:
				r = "7"
			if x == 8:
				r = "8"
			if x == 9:
				r = "9"
			if x == 10:
				r = "A"
			if x == 11:
				r = "B"
			if x == 12:
				r = "C"
			if x == 13:
				r = "D"
			if x == 14:
				r = "E"
			if x == 15:
				r = "F"
			colour = colour + r
		document["output"].style.backgroundColor = colour
for x in range(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
	main()

