angka1 = input().split(" ")
if len(angka1) <= 3:
    angka = list(map(int, angka1))
    print(angka)
else :
    print("masukan jumlah angka = 3")
a = angka[0]
b = angka[1]
c = angka[2]
if a >= b + c or b >= a + c or c >= b + a:
    print("bukan segitiga")
else:
    if a == b and b == c:
        print("segitiga sama sisi")
    elif a == b or b == c or a == c:
        print("segitiga sama kaki")
    else :
        print("segitiga sembarang")