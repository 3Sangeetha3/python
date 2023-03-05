
a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))

d = (b**2)-(4*a*c)

sol1 = (-b-(d)**0.5)/(2*a)
sol2 = (-b+(d)**0.5)/(2*a)
print((sol1,sol2))