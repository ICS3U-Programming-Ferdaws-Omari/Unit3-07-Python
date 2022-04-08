#!/usr/bin/env python3
# Created By: Ferdaws
# Date: Jan 3, 2022
# This program shows compatible spouses for people.
def main():
    # Get the user input
    user_age_as_string = input("Enter your age: ")
    try:
        user_age_as_int = int(user_age_as_string)
        # Check if the age is between 25-45
        if user_age_as_int >= 25 and user_age_as_int <= 45:
            print("You can date ")
        else:
            print ("You can not date")
    except Exception:
        print("This input is invalid")
    finally:
        print("Thanks for playing")

if __name__ == "__main__":
    main()