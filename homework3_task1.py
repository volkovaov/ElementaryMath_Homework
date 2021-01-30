import math

#var1
a = input("Введите координаты вектора (x,y)  через запятую без пробела: ")

vect_1 = a.split(",")
# зная, что длина вектора вычисляется по формуле: |n|=sqrt(x**2 + y**2)

for i in range(len(vect_1)):
    length_vect = math.sqrt(int(vect_1[1])**2 + int(vect_1[i])**2)

print(length_vect)

#var2
a = input("Введите координаты начала вектора (x1,y1)  через запятую без пробела: ")
b = input("Введите координаты конца вектора(x2,y2) через запятую без пробела: ")

vect_start = a.split(",")
vect_end = b.split(",")
# зная, что длина вектора вычисляется по формуле: |n|=sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = int(vect_start[0])
y1 = int(vect_start[1])
x2 = int(vect_end[0])
y2 = int(vect_end[1])
length_vect = math.sqrt(((x2-x1)**2 + (y2-y1)**2))

print(length_vect)