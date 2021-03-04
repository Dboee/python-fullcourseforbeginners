employees = open("./20_externalfile.txt", "r") # r for read, w for write, a for append(add to end, but not remove), r+ for full access

if(employees.readable()):
    print(employees.read())
print("===================")



# if(employees.readable()):
#     for line in employees.readlines():
#         print(line)

employees.close()