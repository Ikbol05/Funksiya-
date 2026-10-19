import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here



def mashina(brend):
    if brend.lower() == "chevrolet":
        print("AQSH")
    elif brend.lower() == "bmw":
        print("Germaniya")
    elif brend.lower() == "mercedes":
        print("Germaniya")
    elif brend.lower() == "toyota":
        print("Yaponiya")
    elif brend.lower() == "kia":
        print("Janubiy Koreya")
    elif brend.lower() == "hyundai":
        print("Janubiy Koreya")
    elif brend.lower() == "byd":
        print("Xitoy")
    elif brend.lower() == "ferrari":
        print("Italiya")
    elif brend.lower() == "tesla":
        print("AQSH")
    elif brend.lower() == "volvo":
        print("Shvetsiya")
    else:
        print("Bu brend ro'yxatda yo'q")

brend = input("Mashina brendini kiriting: ")
mashina(brend)



