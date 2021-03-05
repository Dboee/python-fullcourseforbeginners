employees_old = open("./20_externalfile.txt", "a") # r for read, w for write, a for append(add to end, but not remove), r+ for full access
employees = open("./20_externalfilecreatedwithpython.txt", "w") # r for read, w for write, a for append(add to end, but not remove), r+ for full access

#OBS! ".write()" will overwrite the entrire file

# Python is a great language for readingand writing files, it does not have to be .txt for this to work.


employees.write("\nKelly - Customer Service")



employees.close()