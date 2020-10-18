f = open("Adi.txt", "rt") #comma ke baad wala mode hai
AdiKaContent= f.read(63353)
print(AdiKaContent)

f.close()
