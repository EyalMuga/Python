# Ask customer’s First name and Last name
while True:
    name = input("please enter your first name: ")
    if name.isalpha():
        break
    print("please enter valid name using only letters")
    continue
while True:
    last_name = input("please enter your last name: ")
    if last_name.isalpha():
        break
    else:
        print("please enter valid name using only letters")
        continue

    # Suggest class menu to the customer
print(f"""Hello {name.title()} {last_name.title()} we have 3 options for the flight today:
    1)    first class        *        price: 4000$
    2)    business class     *        price: 2300$ - 3000$
    3)    economy class      *        price: 1200$ - 1700$ """)


# *********************************************  FUNCTIONS  ***********************************************

# function to pick class type
def class_pick():
    class_list = ['1', '2', '3']
    while True:
        class_number = input("please enter class from the options given")
        # validate class is from list
        if class_number not in class_list:
            print("Error: please enter from the options.")
            continue
        else:
            break
    class_number = int(class_number)
    return class_number


# BUSINESS class function
def class_2():
    business_rows = ['5', '6', '7']
    business_rows_2 = ['8', '9', '10']
    total_sum = 0
    print("""Welcome to BUSINESS class, we have 2 options for the flight today:
    1)    rows 5,6,7        *         price: 3000$
    2)    rows 8,9,10       *         price: 2300$  """)
    while True:
        row_number = input("Enter row number you want : ")
        # validate input isn't empty
        if len(row_number) == 0:
            print(f"Error: Input can NOT be empty!")
            continue
            # validate row in the options given
        if row_number in business_rows:
            total_sum = 3000
            break
        elif row_number in business_rows_2:
            total_sum = 2300
            break
        else:
            print("wrong number: please enter from options")
            continue
    row_number = int(row_number)
    print(f"you chose row number {row_number}. now lets choose seat")
    seat_windows = ['a', 'd']
    seat_aisle = ['b', 'c']
    seat_letter = None
    print("""we have 2 options:
A and D next to the windows: EXTRA fee of: 55$
B and C next to the aisle: NO extra fee""")
    while True:
        seat_letter = input(
            "please enter A or D to seat next to the windows or B or C next to the aisle ").lower().strip()
        # validate input isn't empty
        if len(seat_letter) == 0:
            print(f"Error: Input can NOT be empty!")
            continue
        if seat_letter in seat_windows:
            total_sum += 55
            break
        elif seat_letter in seat_aisle:
            total_sum += 0
            break
        else:
            print("wrong number: please enter from options")
            continue
    print(f"your order so far is: "
          f" Business class"
          f" seat: {row_number}{seat_letter}"
          f" total cost of: {total_sum}$")
    while True:
        luggage = int(input("Enter luggage weight please : "))
        if luggage < 51:
            print("luggage weight under 50: no extra fee")
            break
        elif luggage > 50:
            extra_weight = luggage % 50
            extra_to_pay = (extra_weight * 10)
            total_sum += extra_to_pay
            print(f"your total order so far is :"
                  f"Business class     "
                  f"seat: {row_number}{seat_letter}      "
                  f"your luggage weight is: {luggage}    "
                  f"and your total sum to pay is: {total_sum}$ ")
            break
        else:
            continue
    while True:
        menu_business = 0
        menu_1 = 'STARTER - Roast veal sweetbread , MAIN - Cornish turbot,  DESERT  - Hazelnut souffle'
        menu_2 = 'STARTER - Ravioli lobster , MAIN - 100-Day aged Cumbrian Blue Grey,  DESERT  - Pecan praline'
        menu_3 = 'STARTER - Scallops from the Isle of Skye , MAIN - Aynhoe Park fallow deer, DESERT - Caramelised ' \
                 'apple Tarte Tatin '

        print(f"""Today's special Chef is : Gordon Ramsey !!!!
            we can offer you his menu for today's flight for extra fee of: 45$
            you can see the menu here:
            menu #1 - {menu_1}
            menu #2 - {menu_2}
            menu #3 - {menu_3}
            and of course we have our BUSINESS FOOD MENU WITH NO EXTRA FEE""")
        food = int(input("please enter 1- for menu #1, 2- for menu #2, 3 for menu #3 or 0 for business menu"))
        if food == 1:
            print(f"you chose {menu_1}")
            total_sum += 45
            break
        elif food == 2:
            print(f"you chose {menu_2}")
            total_sum += 45
            break
        elif food == 3:
            print(f"you chose {menu_3}")
            total_sum += 45
            break
        elif food == 0:
            print("you chose to eat BUSINESS menu for today")
            total_sum += 0
            break
        else:
            print("please choose from the menu description")
            continue
    print(f"""Your total order for today:
            seat:{row_number}{seat_letter}
            luggage weight:{luggage}
            you chose menu:{food}
            for total cost of:{total_sum}""")
    return row_number, seat_letter, total_sum, luggage, food,


# first class function
def class_1():
    first_rows = ['1', '2', '3', '4']
    row_number = None
    total_sum = 0
    print("""            Welcome to FIRST class:
            rows 1, 2, 3, 4        *         price $4000
            """)
    while True:
        row_number = input("Enter row number you want : ")
        # validate input isn't empty
        if len(row_number) == 0:
            print(f"Error: Input can NOT be empty!")
            continue
            # validate row in the options given
        if row_number in first_rows:
            total_sum = 4000
            break
        else:
            print("wrong number: please enter from options")
            continue
    row_number = int(row_number)
    print(f"you chose row number {row_number}. now lets choose seat")
    seat_windows = ['a', 'd']
    seat_aisle = ['b', 'c']
    seat_letter = None
    print("""we have 2 options:
        A and D next to the windows, B and C next to the aisle""")
    while True:
        seat_letter = input(
            "please enter A or D to seat next to the windows or B or C next to the aisle ").lower().strip()
        # validate input isn't empty
        if len(seat_letter) == 0:
            print(f"Error: Input can NOT be empty!")
            continue
        if seat_letter in seat_windows:
            break
        elif seat_letter in seat_aisle:
            break
        else:
            print("wrong option: please enter from options")
            continue
    print(f"your order so far is: "
          f" First class"
          f" seat: {row_number}{seat_letter}"
          f" total cost of: {total_sum}$")
    luggage = int(input("Enter luggage weight please : "))
    print(f"""your total order so far is :
        First class
        seat: {row_number}{seat_letter}
        your luggage weight is: {luggage}
        and your total sum to pay is: {total_sum}$ """)
    while True:
        menu_1 = 'STARTER - Roast veal sweetbread , MAIN - Cornish turbot,  DESERT  - Hazelnut souffle'
        menu_2 = 'STARTER - Ravioli lobster , MAIN - 100-Day aged Cumbrian Blue Grey,  DESERT  - Pecan praline'
        menu_3 = 'STARTER - Scallops from the Isle of Skye , MAIN - Aynhoe Park fallow deer, DESERT - Caramelised ' \
                 'apple Tarte Tatin '

        print(f"""Today's special Chef is : Gordon Ramsey !!!!
                you can see the menu here:
                menu #1 - {menu_1}
                menu #2 - {menu_2}
                menu #3 - {menu_3}""")
        food = input(int("please enter 1- for menu #1, 2- for menu #2, 3 for menu #3")
        # what the fuck did you tried to do ? hahaha
        while True:
            if food == 1:
                print(f"you chose {menu_1}")
                break
            elif food == 2:
                print(f"you chose {menu_2}")
                break
            elif food == 3:
                print(f"you chose {menu_3}")
                break
            else:
                print("please choose from the menu description")
                continue
        print(f"""your order sum:
                        First class, seat:{row_number}{seat_letter}
                        your luggage weights {luggage}
                        and your menu for today is: {food} for total sum of: {total_sum}$""")
        return row_number, seat_letter, total_sum, luggage, food


def class_economy():
    # reformat this lines - put range instead of strings as list of numbers
    economy_rows = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    economy_rows_2 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
                      '35', '36', '37', '38', '39', '40']
    economy_rows_3 = 40 <= economy_rows_3 >= 60
    economy_extra = ['12', '22', '42']
    row_number = None
    total_sum = 0
    print("""Welcome to economy class, we have 3 options for the flight today:
        1)    rows 11-20        *         price: 1700$
        2)    rows 21-40        *         price: 1500$
        3)    rows 41-60        *         price: 1200$  """)
    while True:
        row_number = input("Enter row number you want : ")
        # validate input isn't empty
        if len(row_number) == 0:
            print(f"Error: Input can NOT be empty!")
        # validate row in the options given
        if row_number in economy_rows:
            total_sum = 1700
            if row_number in economy_extra:
                total_sum += 15
            break
        elif row_number in economy_rows_2:
            total_sum = 1500
            if row_number in economy_extra:
                total_sum += 15
            break
        elif row_number in economy_rows_3:
            total_sum = 1200
            if row_number in economy_extra:
                total_sum += 15
            break
        else:
            print("wrong number: please enter from options")
            continue
    print(f"you chose row number {row_number}. now lets choose seat")
    seat_windows = ['a', 'f']
    seat_aisle = ['d', 'c']
    middle_seats = ['b', 'e']
    seat_letter = None
    print("""       we have 3 options:
                    A and f next to the windows: EXTRA fee of: 10$
                    d and C next to the aisle: NO extra fee
                    B and E in the middle of 2 seats: NO extra fee""")
    while True:
        seat_letter = input(""" please enter A and F next to the windows or
                                d and C next to the aisle or B and E in the middle of 2 seats""").lower().strip()
        # validate input isn't empty
        if len(seat_letter) == 0:
            print(f"Error: Input can NOT be empty!")
            continue
        if seat_letter in seat_windows:
            total_sum += 15
            break
        elif seat_letter in seat_aisle:
            total_sum += 0
            break
        elif seat_letter in middle_seats:
            total_sum += 0
            break
        else:
            print("wrong number: please enter from options")
            continue
    print(f"your order so far is: "
          f" economy class "
          f" seat: {row_number}{seat_letter}"
          f" total cost of: {total_sum}$")
    while True:

        luggage = int(input("Enter luggage weight please : "))
        if luggage < 21:
            print("luggage weight under 20: no extra fee")
            break
        elif luggage > 20:
            extra_weight = luggage % 20
            extra_to_pay = (extra_weight * 10)
            total_sum += extra_to_pay
            print(f"""your total order so far is :
                  economy class
                  seat: {row_number}{seat_letter}
                  your luggage weight is: {luggage}
                  extra fee : {extra_to_pay}
                  and your total sum to pay is: {total_sum}$ """)
            break
        else:
            continue
    while True:
        print("""for today's food we have 3 options:
                 1) gordon ramsey's menu for additional 42$
                 2) business class menu for additional 22$
                 3) economy class menu for only 7 $ addition.""")
        food = int(input("""please enter 1- for FIRST CLASS
                            2- for BUSINESS CLASS
                            3- for ECONOMY CLASS """))
        if food == 1:
            print(f"you chose to eat Gordon's menu")
            total_sum += 42
            break
        elif food == 2:
            print(f"you chose the business class menu")
            total_sum += 22
            break
        elif food == 3:
            print(f"you chose economy menu")
            total_sum += 7
            break
        else:
            print("please choose from the menu description")
            continue
    print(f"""your total order is:
    Economy class
    seat: {row_number}{seat_letter}
    luggage weight: {luggage}
    extra fee of: {extra_to_pay}
    and you chose menu: {food}
    for total sum of: {total_sum}""")
    return row_number, seat_letter, total_sum, luggage, food


# function to calculate the total discount
def bonus(total_sum):
    import random
    name_length = len(name + last_name)
    rand_number = random.randint(0, 9)
    lucky_number = random.randint(0, 5)
    reminder = (name_length * lucky_number) / rand_number
    if reminder <= 5:
        discount = ((100 - reminder) / 100)
        new_total = (total_sum * discount)
        print(f"""you won!!!  you got {reminder} % discount
              your total sum now is: {round(new_total)}""")
    else:
        print("you did not win..... maybe next time!")
    return


# function that asks the customer if he wants to participate
def yes_no_bonus():
    lottery = None
    while lottery != "yes" and lottery != 'no':
        lottery = str(input(
            "would you like to participate in our lottery contest and win discount?(yes) or (no)")).lower().strip()
    if lottery == 'yes':
        bonus(total_sum)
    else:
        print("thank you, see you next flight!!")


# **************************************************************
#                       MAIN START
# **************************************************************


if __name__ == "__main__":

    print("""𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 Muga 𝒂𝒊𝒓𝒍𝒊𝒏𝒆𝒔
    𝗯𝗲𝗳𝗼𝗿𝗲 𝘆𝗼𝘂𝗿 𝗳𝗹𝗶𝗴𝗵𝘁 𝘄𝗲𝗹𝗹 𝗻𝗲𝗲𝗱 𝘁𝗼 𝘁𝗮𝗸𝗲 𝘀𝗼𝗺𝗲 𝗱𝗲𝘁𝗮𝗶𝗹𝘀 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝗳𝗹𝘆𝗶𝗻𝗴 𝘁𝗶𝗰𝗸𝗲𝘁.
    𝗵𝗮𝘃𝗲 𝗻𝗶𝗰𝗲 𝗳𝗹𝗶𝗴𝗵𝘁 𝗮𝗻𝗱 𝘀𝘁𝗮𝘆 𝘀𝗮𝗳𝗲 ❗
        """)

    pick = class_pick()

    if pick == 2:
        row_number, seat_letter, total_sum, luggage, food = class_2()
        yes_no_bonus()

    elif pick == 1:
        row_number, seat_letter, total_sum, luggage, food = class_1()
        yes_no_bonus()

    elif pick == 3:
        row_number, seat_letter, total_sum, luggage, food = class_economy()
        yes_no_bonus()

# **************************************************************
#                       MAIN END
# **************************************************************
