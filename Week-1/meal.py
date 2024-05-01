def main():
    T = input("What time is it? ")
    actual_time = convert(T)
    if 7 <= actual_time <= 8:
        print("breakfast time")
    elif 12 <= actual_time <= 13:
        print("lunch time")
    elif 18 <= actual_time <= 19:
        print("dinner time")


def convert(time):
    hrs, min = time.split(sep=":")
    return round(float(hrs)+(float(min)/60), 2)


if __name__ == "__main__":
    main()
