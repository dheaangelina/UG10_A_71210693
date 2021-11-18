inputan1 = input("Mendatar/Menurun?: ")

if inputan1 == "Mendatar":
    inputan2 = int(input("Masukkan kolom: "))
    print("#"* inputan2)
elif inputan1 == "Menurun":
    inputan2 = int(input("Masukkan baris: "))
    print("*\n"* inputan2)
else:
    print("Pola tidak dikenali")
