"""

Python Assignment Week 1

Calculate Area


"""

def calculate_area (width, height):
    return width * height

w = 10
h = 20

print(w, h, calculate_area(w,h))



def make_uppercase(word):
    return word.upper()

letters = 'abc'
print(letters, make_uppercase(letters))



def validate_area(a):
    if a < 25:
        return True
    else: 
        return False

area_1 = 20
area_2 = 50

print(area_1, validate_area(area_1))
print(area_2, validate_area(area_2))

