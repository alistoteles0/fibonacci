#Fibonacci sayı dizisini yazdıran program.
a = 1
b = 1
fibonacci = [a,b]
#range('20') değeri değiştirilebilir. Buna göre girdiğiniz bir değerin 2 fazlası kadar terim oluşur.
for i in range(20):
    a,b = b,a+b
    fibonacci.append(b)
print(fibonacci)
        