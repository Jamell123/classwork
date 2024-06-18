def main():
    print("jamell")
    dictionary=[]

    with open('dictionary.txt') as f:
        for line in f:
            dictionary.append(line.strip())

    print(dictionary)
    dictionary.sort()
    print("BIRD" in dictionary)
    print("BEARD" in dictionary)
    print("TECH" in dictionary)
if __name__ == '__main__':
    main()