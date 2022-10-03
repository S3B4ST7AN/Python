f = open("Archivo.txt", "r")

for line in f:
    line = line.strip()
    line = line.split(',')
    print (line[1])

f = open("Archivo.txt", "a")

f.write("Durrazno,5,10\n")

f = open("Archivo.txt", "w")

f.write("HOLA MUNDO!")