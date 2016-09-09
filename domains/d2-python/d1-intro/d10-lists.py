# Pyton List Eg
line = input()
cmd = line.split()
arr = list()
# print(position) unit testing
# print(element) unit testing
position = int(cmd[1])
element = int(cmd[2])
s1 = 'insert'
s2 = 'remove'
s3 = 'append'
s4 = 'print'

if cmd[0] == s1:                    # cmd[0] must beS1
    arr.insert(position, element)
else:
    if cmd[0] == s2:
        arr.remove(element)
    else:                       # cmd[0] must beS3
        if cmd[0] == s3:
            arr.append(element)
        else:                   # cmd[0] must beS4
            if cmd[0] == s4:
                print(arr)
            else:
                print("WrongInput")

print(arr)
