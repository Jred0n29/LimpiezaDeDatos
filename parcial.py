from cgi import print_directory
import os 
import pandas as pd
#Este parcial es hecho por Daniel Fernando Castro
#Cuarto semestre de ingenieria Agroindustrial
#Justo fuentes

"""Los archivos que me tocaron fueron los siguientes [121, 122, 123, 124, 125, 126, 127, 128] """
"""Para ejecutar el archivo tenemos ue tener una carpeta dada por el profesor llamada city_temp 
una vez tengamos esa carpeta creamos una carpeta con el nombre cualquiera metemos esa carpeta y metemos el archivo
parcial.py y ya podemos ejecutar y correr todas las opciones disponible"""
archivos_extraidos= ["121POLISBON.txt","122PRLIMA.txt","123QTDOHA.txt","124RAALMATY.txt","124RAALMATY.txt","125RABSHKEK.txt","126RADUSNBE.txt","127RATASKNT.txt"]
def menu_DE_opciones():
    archivos = archivos_extraidos
    print("Menu de opciones a elegir")
    for i in range(8):
        print(i+1, archivos[i])
    print("9. LIMPIEZA DE ARCHIVOS")
    print("10. CONVERSION DE ARCHIVOS")
    print("11. RESUMENES")
    print("12. SALIR")
    print("ParciaL hecho por: Daniel fernando vasquez")
    try:
        opcion_escogida_User =int(input("INGRESE LA OPCION A ELEGIR: "))
        opcion = opcion_escogida_User
    except: print("Ups ha ocurrido un error")
    if 1<= opcion <= 8 :
        with open(f"city_temp/{archivos_extraidos[opcion+1]}") as f:
            print(f.read())
            print("EL ARCHIVO LEIDO ES " , archivos_extraidos[opcion+1]) 
    elif opcion==9:
        for i in archivos_extraidos:
            df = pd.read_fwf(f'city_temp/{i}', header=None)
            matriz = pd.DataFrame(df)
            matrix_new = matriz.set_index(0) 
            matriz_clean = matrix_new[matrix_new[3] != -99]
        print(matriz_clean)
    elif opcion==10:
            for i in archivos_extraidos:
                df = pd.read_fwf(f'city_temp/{i}', header=None)
                matriz = pd.DataFrame(df)
                matriz_clean = matriz.set_index(0) 
                matriz_clean = matriz_clean[matriz_clean[3] != -99]
                kelvin = round((matriz_clean[3] + 459.67 )/1.8 , 2)
                celsiu = (matriz_clean[3] - 32 )*0.55
                matriz_nueva = matriz_clean.assign(k = kelvin, c = celsiu)
                os.makedirs('archivos_convertidos', exist_ok=True)                
                matriz_nueva.to_csv(f'archivos_convertidos/{i}', header=None, sep=' ', mode='w+')
    elif opcion==11:
        for i in archivos_extraidos:
            df = pd.read_fwf(f'city_temp/{i}',  header=None)
            matriz = pd.DataFrame(df)
            matriz_sin_cabezera = matriz.set_index(0) 
            matriz_limpia = matriz_sin_cabezera[matriz_sin_cabezera[3] != -99]
            columna_tree = matriz_limpia[3]
            suma_col_tres = columna_tree.sum()
            promedio = suma_col_tres / (len(columna_tree))
            maximo_valor = max(columna_tree)
            minimo_valor = min(columna_tree)
            print( "|", i,"|", promedio ,"|",minimo_valor,"|", maximo_valor, "|") 
    elif opcion==12:print("EL PROGAMA CERRARA EN CUESTION DE SEGUNDOS, VUELVA PRONTO") 
    else:print("OPCION NO CONTEMPLADA , DIGITE UNA OPCION VALIDA")
menu_DE_opciones()