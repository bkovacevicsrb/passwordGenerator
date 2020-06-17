import random
import string

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

print("Generator lozinke radi po principu nasumicnog odabira \n brojeva i slova. \n Preuzmite svoju lozinku : \n")

velikoSlovo1=chr(random.randint(65,90))
velikoSlovo2=chr(random.randint(65,90))
velikoSlovo3=chr(random.randint(65,90))
velikoSlovo4=chr(random.randint(65,90))

maloSlovo1=chr(random.randint(97,122))
maloSlovo2=chr(random.randint(97,122))
maloSlovo3=chr(random.randint(97,122))
maloSlovo4=chr(random.randint(97,122))

broj1=chr(random.randint(48,57))
broj2=chr(random.randint(48,57))
broj3=chr(random.randint(48,57))
broj4=chr(random.randint(48,57))


password = velikoSlovo1 + velikoSlovo2 + velikoSlovo3 + velikoSlovo4 + maloSlovo1 + maloSlovo2 + maloSlovo3 + maloSlovo4 + broj1 + broj2 + broj3 + broj4
password = shuffle(password)

print("Vasa lozinka je : \n", password)
