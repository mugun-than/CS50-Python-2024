def main():
    String = input()
    print(convert(String))

def convert(string):
    string = string.replace(':)','🙂')
    string = string.replace(':(','🙁')
    return string

main()
