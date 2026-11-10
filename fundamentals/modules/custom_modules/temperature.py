# Module temperature.py functions

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 1)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 1)

if __name__ == '__main__':
    for n in range(0, 101, 25):
        print(f"Celsius:{n} = fahrenheit:{celsius_to_fahrenheit(n)}")