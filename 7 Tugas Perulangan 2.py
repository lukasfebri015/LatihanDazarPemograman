print("Program Menghitung Huruf Vokal")

kata = input("Masukan Kata = ")

vokal = 0
for kar in kata :
    if kar.lower() in "aiueo" :
        vokal = vokal + 1
print("Banyaknya Huruf Vokal = ", vokal)