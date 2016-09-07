numCmd = input()
line = input()
cmd = line.split()
arr = list()
#print(position)
#print(element)
position = int(cmd[1])
element =  int(cmd[2])
s1 = 'insert'
s2 = 'remove'
s3 = 'append'
s4 = 'print'

if cmd[0] == s1:
   if cmd[0] == s2:
       arr.insert(position,element)
       arr.remove(position)
   else :
   		print("wrong data")

else :
	print(q)




print(arr)
