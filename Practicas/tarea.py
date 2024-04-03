def primer_elemento_repetido(arr):
    n = len(arr)
    # Crear un diccionario para almacenar el índice de la primera aparición de cada elemento
    first_occurrence = {}
    
    # Iterar sobre el array
    for i in range(n):
        if arr[i] in first_occurrence:
            # Si el elemento ya está en el diccionario, significa que se ha repetido
            # Devolver el índice de la primera aparición
            return first_occurrence[arr[i]] + 1
        else:
            # Si es la primera aparición, almacenar su índice
            first_occurrence[arr[i]] = i
    
    # Si no se encuentra ningún elemento repetido, devolver -1
    return -1

# Ejemplo de uso
arr = [1, 5, 3, 4, 3, 5, 6]
resultado = primer_elemento_repetido(arr)
print("salida:", resultado)
