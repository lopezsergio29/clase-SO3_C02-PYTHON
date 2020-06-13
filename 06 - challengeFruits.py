fruta = input("Escribe la fruta que quieres: ")
cantidad = int(input("Escribe la cantidad de la fruta que quieres: "))
total = 0

if fruta == "Manzana":
    total = cantidad * 1
elif fruta == "Piña":
    total = cantidad * 3
elif fruta == "Fresa":
    total = cantidad * (2 / 5)


print(f"Debe de pagar un total de $ {total}")
