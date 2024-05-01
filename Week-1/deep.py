def main():
    String = input('What is the Answer to the Great Question of Life, the Univers, and Everything? ')
    String = String.lower().strip()
    l: list[str] = ['forty-two','42','forty two']
    if String in l:
        print("Yes")
    else:
        print("No")


main()
