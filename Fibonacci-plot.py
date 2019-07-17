import matplotlib.pyplot as plt

a = int(input("Wieviele Zahlen sollen berechnet werden? "))
i = 0
x = 0
y = 1
Fibonacci=[]
Counter=[]

while i < a:

	x=x+y
	i+=1
	z = x
	Fibonacci.append(z)
	Counter.append(i)

	y=y+x
	i+=1
	z=y
	Fibonacci.append(z)
	Counter.append(i)

	pass

print("Es wurden",i,"Zahlen berechnet:")

for numbers in Fibonacci:
	print (numbers)

plt.scatter(Counter, Fibonacci, color="red")
plt.plot(Counter, Fibonacci, color="red")

plt.title("Fibonacci Zahlenreihe")
plt.xlabel("Counter")
plt.ylabel("Fibonacci")

plt.show()