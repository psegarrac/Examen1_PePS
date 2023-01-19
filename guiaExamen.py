import os
path = input ("Dame la ruta:")
dirCount = 0
fileCount = 0

for ruta, dirs, files in os.walk(path):
    print ('looking in:'    , ruta)
    for directories in dirs:
        dirCount += 1
    for ficheros in files:
        nombreDirectorio = os.path.basename(ruta)
        
        if nombreDirectorio != 'psegarra':
            nombreFichero = os.path.basename(ficheros)
            print(nombreFichero)
            fileCount += 1

print('Número de ficheros: ', fileCount)
print('Número de directorios: ', dirCount)
print('Total: ', fileCount + dirCount)  

