# Program untuk input nilai dan menampilkan grade

# Menentukan grade berdasarkan nilai


# Input nilai dari pengguna
nilai = float(input("Masukkan nilai (0-100): "))

if nilai >= 86:
    grade = 'A'
if nilai >= 76:
    grade = 'B'
if nilai >= 61:
    grade = 'C'
if nilai >= 41:
    grade = 'D'
else:
    grade = 'E'


print(f"Grade Anda: {grade}")



