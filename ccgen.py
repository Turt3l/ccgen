import random
from faker import Faker
fake = Faker()
valid = False
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10
def ExpDate():
    rand_month = random.randint(1, 12)
    rand_year = random.randint(22, 26)
    print("EXP DATE: " + str(rand_month) + "/" + str(rand_year))
def cvc():
    rand_cvc = random.randint(100, 900)
    print("CVC:" + str(rand_cvc))
usinput = input("1.VISA(More to come soon): ")
choices = ["VISA"]
try:
    if (choices[int(usinput) - 1]) == "VISA":
        while valid == False:
            visa_number = random.randint(4000000000000000, 4999999999999999)
            if luhn_checksum(visa_number)== 0:
                valid = True
                print("CARD NUM:" + str(visa_number))
            else:
                continue
            ExpDate()
            cvc()
            print("BILLING ADDRESS: " + fake.address())
            print("NAME: " + fake.name())

except:
    print("invalid input")
    ValueError()
