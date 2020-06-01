def main():
    users_card = input("Enter your card number:\n")

    if len(users_card) == 13:
        print("VISA")

    elif len(users_card) == 15:
        if users_card.startswith("34") or users_card.startswith("37"):
            print("AMEX")
        else:
            print("INVALID")

    elif len(users_card) == 16:
        if users_card.startswith("4"):
            print("VISA")

        elif (
            users_card.startswith("51")
            or users_card.startswith("52")
            or users_card.startswith("53")
            or users_card.startswith("54")
            or users_card.startswith("55")
        ):
            print("MASTERCARD")

        else:
            print('INVALID')

    else:
        print('INVALID')


if __name__ == "__main__":
    main()
