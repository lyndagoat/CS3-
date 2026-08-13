"""
Ocampo
9-Balingkilat
08/13/26
"""

while True:
    year = int(input("Enter your birth year: "))
    if year >= 1900:
        break
    elif year < 1900:
        print("Invalid year, it should not be earlier than 1900")
    else:
        print("Please enter a year.")

def calculate():
    global number
    number = year-1900
    number = number%12+1

def zodiac(number):
    if number == 1:
        zodiac = "Rat (鼠 / Shǔ)"
    elif number == 2:
        zodiac = "Ox (牛 / Niú)"
    elif number == 3:
        zodiac = "Tiger (虎 / Hǔ)"    
    elif number == 4:
        zodiac = "Rabbit (兔 / Tù)"
    elif number == 5:
        zodiac = "Dragon (龙 / Lóng)"
    elif number == 6:
        zodiac = "Snake (蛇 / Shé)"
    elif number == 7:
        zodiac = "Horse (马 / Mǎ)"
    elif number == 8:
        zodiac = "Goat (羊 / Yáng)"
    elif number == 9:
        zodiac = "Monkey (猴 / Hóu)"
    elif number == 10:
        zodiac = "Rooster (鸡 / Jī)"
    elif number == 11:
        zodiac = "Dog (狗 / Gǒu)"
    elif number == 12:
        zodiac = "Pig (猪 / Zhū)"
    print(f"\nYour Chinese Zodiac is : {zodiac}")

calculate()
zodiac(number)
