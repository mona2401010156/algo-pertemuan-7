#2. Penggunaan Percabangan if
" # blok kode yang dijalankan jika kondisi benar"

x= 10
if x > 5:
    print ("x lebih besar dari 5")
    print()


#3. Penggunaan Percabangan if else
    "blok kode yang dijalankan jika kondisi benar"
#else:
    "blok kode yang dijalankan jika kondisi salah"

x = 4
if x > 5:
    print("x lebih besar dari 5")
else:
    print ("x tidak lebih besar dari 5")
    print()
    

#4. Penggunaan Nested 
    #if kondisi2:
    "blok kode yang dijalankan jika kondisi1 dan kondisi2 benar"
x = 10
y = 20
if x > 5:
    if y > 15:
        print ("x tidak lebih besar dari 5 dan y lebih besar dari 15")

#5. Penggunaan switch
        
int-hari = 3;
switch (hari) {
    case 1:
        print("Senin");
        break;
    case 2:
        print("Selasa");
        break;
    case 3:
        print("Rabu");
        break;
    default:
        print("Hari tidak valid");
}
