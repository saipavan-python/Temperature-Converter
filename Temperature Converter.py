
# Simple Temperature Converter (Celsius, Fahrenheit, Kelvin)

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    # F -> C -> K
    c = fahrenheit_to_celsius(f)
    return celsius_to_kelvin(c)

def kelvin_to_fahrenheit(k):
    # K -> C -> F
    c = kelvin_to_celsius(k)
    return celsius_to_fahrenheit(c)


def main():
    print("Welcome to Temperature Converter (Python)")

    while True:
        print("""
Choose conversion:
1. Celsius  -> Fahrenheit
2. Fahrenheit -> Celsius
3. Celsius  -> Kelvin
4. Kelvin   -> Celsius
5. Fahrenheit -> Kelvin
6. Kelvin   -> Fahrenheit
0. Exit
""")
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid choice. Try again.")
            continue

        try:
            value = float(input("Enter temperature value: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == "1":
            result = celsius_to_fahrenheit(value)
            print(f"{value} °C = {result:.2f} °F")
        elif choice == "2":
            result = fahrenheit_to_celsius(value)
            print(f"{value} °F = {result:.2f} °C")
        elif choice == "3":
            result = celsius_to_kelvin(value)
            print(f"{value} °C = {result:.2f} K")
        elif choice == "4":
            result = kelvin_to_celsius(value)
            print(f"{value} K = {result:.2f} °C")
        elif choice == "5":
            result = fahrenheit_to_kelvin(value)
            print(f"{value} °F = {result:.2f} K")
        elif choice == "6":
            result = kelvin_to_fahrenheit(value)
            print(f"{value} K = {result:.2f} °F")

        print("-" * 40)

        again = input("\nDo you want to use the converter again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you! Exiting...")
            break


if __name__ == "__main__":
    main()
