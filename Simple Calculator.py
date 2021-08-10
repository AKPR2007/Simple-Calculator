#welcome to the brain of Simple Calculator. This code is 100% free and opensource. Feel free to do any changes to this. Lastly dont forget to click save ! <note by AK PR>
print ("Simple Calculator")
print ("made by AK PR")
print ("version 1.0")
print ("100% pure python")
print ("opensource repo at github.com/AKPR2007")

a = input("Enter 1st Digit: ")
c = int(input("Enter Process Code {add=1,subtract=2,multiply=3,divide=4}: "))
b = input("Enter 2nd Digit: ")

if c == 1 :
	A = float(a) + float(b)
	print ("your answer= " + str(A))
elif c == 2 :
	B = float(a) - float(b)
	print ("your answer= " + str(B))
elif c == 3 :
	C = float(a) * float(b)
	print ("your answer= " + str(C))
elif c == 4 :
	D = float(a) / float(b)
	print ("your answer= " + str(D))