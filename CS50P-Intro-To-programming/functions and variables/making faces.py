def main():
    x=input("write : ")
    r=convert(x)
    print(r)
def convert(text):
    text=text.replace(':)','🙂')
    text=text.replace(':(','🙁')
    return text
main()
