def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        if not s.isalnum():
            return False
        for i, c in enumerate(s):
            if c.isdigit():
                if c == '0' or not s[i:].isdigit():
                    return False
                else:
                    return True


        return True

    return False



main()
