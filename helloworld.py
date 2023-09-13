def CheckNumber(bilangan):
    isNumber = bilangan.isnumeric()
    return isNumber

if __name__ == 'Main':
    bilangan = input("Masukan bilangan:")
    if(CheckNumber(bilangan)):
        print(bilangan)
    else:
        print("Masukan angka!")