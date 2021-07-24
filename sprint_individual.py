'''
SPRINT DE ENTREGA:

Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante el Módulo 1 de Python básico. Por tanto, se debe poner 
foco en lo siguiente:

● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu aplicación (pueden ser personas, pacientes, organizaciones 
sociales o instituciones públicas).
● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
● Por cada cuenta debe pedir un número telefónico para contactarse.
● El programa no terminará de preguntar por los números hasta que todas las organizaciones tengan un número de contacto asignado.
● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
● Se debe guardar como un string.
A modo de entrega, se debe disponer un documento Word o PDF en el que se indique:
- Ruta del repositorio en GitHub
Consideraciones adicionales
- El código debe estar debidamente indentado
- El formato del documento Word queda a criterio del equipo.

'''
import random
import string

# 1.Lista con los nombres de 10 de sus futuros usuarios de tu aplicación
usuarios = ['usu1','usu2','usu3','usu4','usu5','usu6','usu7','usu8','usu9','usu10']
# Cuentas creadas de usuarios
cuentas_usuarios = []
# Contraseñas creadas de usuarios
pass_usuarios = []
# Variable con Usuario y Contraseña
cuentas = []


# Función para crear cuentas de usuario (@dominio.com puede ser reemplazado por cualquier valor)
def crear_usuario(lista):
    for usuario in lista:
        cuentas_creadas = usuario+'@dominio.com'
        cuentas_usuarios.append(cuentas_creadas)
        #print(f'La cuenta de usuario para {usuario} es: {cuentas_usuarios}')

# Función para crear contraseñas aleatorias
def crear_pass(inicio,final):
    for i in range(inicio, final):
        #Cadena completa de los caracteres a elegir aleatoriamente
        cadena = string.ascii_letters + string.digits + str('*/|+$%')  
        #eleccion aleatoria y rango de longitud
        password = "".join(random.choice(cadena)  for j in range(random.randint(10,50)))
        pass_usuarios.append(password)

# Función para asignar cuenta de usuario y password a la variable cuentas
def cuentas_creadas(lista1, lista2):

    for tupla in zip(lista1, lista2):
        user_pass = (f'El usuario es: {tupla[0]}',f' y su contraseña es: {tupla[1]}' )
        cuentas.append(user_pass)


crear_usuario(usuarios)
#print(cuentas_usuarios)

crear_pass(1,11)
#print(pass_usuarios)

cuentas_creadas(cuentas_usuarios, pass_usuarios)
print(cuentas)
