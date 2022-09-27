# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

from math import sqrt


print("Введите X точки А: ")
x1 = int(input()) 
print("Введите Y точки А: ")
y1 = int(input()) 
print("Введите X точки В: ")
x2 = int(input()) 
print("Введите Y точки В: ")
y2 = int(input()) 
lenX = x1 - x2
lenY = y1 - y2
distance = sqrt(lenX * lenX + lenY * lenY)
print(distance)
