jawab = "y"
no = 0
nama = []
nim = []
n_tugas = []
n_uts = []
n_uas = []
while (jawab == "y"):
    nama.append(input("Nama :"))
    nim.append(input("NIM :"))
    n_tugas.append(input("Nilai Tugas :"))
    n_uts.append(input("Nilai UTS :"))
    n_uas.append(input("Nilai UAS :"))
    jawab = input ("Tambah data (y/t)?")
    no +=1
print("=======================================================================")
print("| No |     Nama     |     NIM     | Tugas |  UTS  |  UAS  |   Akhir   |")
print("=======================================================================")
for n in range(no):
    nt = int(n_tugas[n])
    nu = int(n_uts[n])
    na = int(n_uas[n])
    akhir = (nt*30/100) + (nu*35/100) + (na*35/100)
    print("| {} | {}   | {}   | {}   | {}   | {}   | {}   |".format(n+1,nama[n],nim[n],n_tugas[n],n_uts[n],n_uas
    [n],akhir))
