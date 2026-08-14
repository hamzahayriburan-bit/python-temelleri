'''

      Daire Alanı       :  πr²
      Daire Çevresi     :  2πr

      * Yarı çap verilen bır dairenin alanını ve çevresini
      hesaplayanız (r: 3.14)
      
'''
pi = 3.14

r = float(input("Yarı Çap: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("Alan: " + str(alan) + " Çevre: " + str(cevre))
