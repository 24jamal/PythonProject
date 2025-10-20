f = open(r'ErrorAndExceptionsHandling/example.txt','w')

f.write("Write a new line")

fl = open(r'ErrorAndExceptionsHandling/example.txt','r')

vars = fl.read()
print(vars)