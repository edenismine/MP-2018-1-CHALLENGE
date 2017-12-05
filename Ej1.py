archivo = open("input1.txt","r")

lista = []

def cuentaLineas(nombreArchivo):
    archivo = open(str(nombreArchivo), "r")
    numLineas = len(archivo.readlines())
    return numLineas




def contarVerticales(longitudMatriz,nombreArchivo):
    numeroHola = 0

    archivo = open(str(nombreArchivo), "r")
    for j in range(longitudMatriz):
        for i in archivo.readlines():
            lista.append(i[0].lower())
    numeroHola+=lista.count("hola")
    archivo.close()
    return numeroHola





# Contar holas en posicion horizontal
def contarHorizontales(nombreArchivo):
    numeroHola = 0
    archivo = open(str(nombreArchivo), "r")
    for i in archivo.readlines():
        i = i.lower()
        numeroHola+=i.count("hola")
    archivo.close()
    return numeroHola


print(contarHorizontales("input1.txt"))
print(contarVerticales(cuentaLineas("input1.txt"),"input1.txt"))


totalHolas = contarHorizontales("input1.txt") + contarVerticales(cuentaLineas("input1.txt"),"input1.txt")

print(totalHolas)
