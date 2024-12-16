#Nomor 1: buat kode python untuk menghitung jumlah bilangan dari 1 hingga bilangan n
print("Menghitung jumlah bilangan dari 1 hingga n")
n = int(input("Masukan nilai n : "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Totalnya adalah", total)
