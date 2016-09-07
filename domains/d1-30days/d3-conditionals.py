# Day 3: Intro to Conditional Statements 

q = "Weird";
r = "Not Weird";
num = int(input())

if num % 2  == 0:
   if num in range(2,5):
    	print(r)
   else :
   		if num in range(6,21):
   			print(q)
   		else : 
   			if num > 20 and num % 2 == 0:
   				print(r)
else :
	print(q)
