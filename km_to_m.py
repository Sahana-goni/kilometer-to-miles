import sys
def km_to_m(k):
    return k * 0.621371
if __name__ == "__main__":
    try:
        k = float(sys.argv[1])
    except IndexError:
        k = float(input("Enter the number: "))
    except ValueError:
        print("Please enter a valid number!")
        sys.exit(1)

    result = km_to_m(k)
    print(f"{k} km = {result} miles")
