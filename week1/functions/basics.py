def greet(name):
    return f"Hello {name} have a good day"

def add(a, b=0):
    return a + b

print(greet("Max Gonzalez"))
print(add(5, 10))
print(add(7))

def introduce(name, city="Guadalajara"):
    return f"My name is {name} and I live in {city}."

print(introduce(city="Monterrey", name="Luis"))