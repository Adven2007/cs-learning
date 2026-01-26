def main():
    time = input("What time is it? ")
    num = convert(time)
    if (num >= 7 and num <= 8):
        print("breakfast time")
    elif (num >= 12 and num <= 13):
        print("lunch time")
    elif (num >= 18 and num <= 19):
        print("dinner time")

def convert(time):
    plus = 0
    index = time.rfind(" ")
    if (index != -1):
        time, suffix = time.split(" ")
        if (suffix == ".p.m"):
            plus = 1
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    num = hour + float(minute / 60) + 12 * plus
    return num

if __name__ == "__main__":
    main()