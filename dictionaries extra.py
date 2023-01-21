# Write a function that receives 2 lists as parameters - the first list contains strings that represent vehicles
# (manufacturer + model), the second list contains strings of colors.
# Create a dictionary that maps vehicles to a list of colors. You can assume that the length of the lists is equal.
#  For example, for the input:
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     B8     1   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# model = ["Mazda 3", "Toyota Yaris", "Volvo S40", "Mazda 2", "Toyota Yaris", "Volvo S40"]
# colors = ["red", "white", "red", "blue", "black", "red"]
#
#
# def car2color(model, colors):
#     car_color = {}
#     for i in range(len(model)):
#         car_color[model[i]] = colors[i]
#     return car_color
#
#
# print(car2color(["Mazda 3", "Toyota Yaris", "Volvo S40", "Mazda 2", "Toyota Yaris", "Volvo S40"],
#                 ["red", "white", "red", "blue", "black", "red"]))
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     B8     2   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def string_count(list):
#     count = {}
#     for string in list:
#         if string in count:
#             count[string] += 1
#         else:
#             count[string] = 1
#     return count
#
#
# print(string_count(["sun", "water", "air", "water", "water", "apple", "air"]))
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     B8     3   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import pprint

# Implement a function that receives 2 lists of strings - dates and stocks. Date contains various dates
# represented as string in format dd-mm-yy, and stocks list contains tickers of stocks that fell more than 5%
# in the corresponding date. You should return 2 dictionaries - the first one maps dates to list of stocks that
# fell more than 5% in that date, the second one maps stocks to list of dates in which they fell.
# For example, for the input:


dates = ["11-05-22", "12-05-22", "13-05-22", "12-05-22", "11-05-22", "11-05-22"]
stocks = ["TSLA", "TSLA", "AAPL", "MSFT", "AAPL", "IBM"]


def create_date_dict(dates, stocks):
    date_dict = {}
    for date, stock in zip(dates, stocks):
        if date not in date_dict:
            date_dict[date] = [stock]
        else:
            date_dict[date].append(stock)
    return date_dict


def create_stock_dict(dates, stocks):
    stock_dict = {}
    for date, stock in zip(dates, stocks):
        if stock not in stock_dict:
            stock_dict[stock] = [date]
        else:
            stock_dict[stock].append(date)
    return stock_dict


pprint.pprint(create_stock_dict(dates, stocks))
pprint.pprint('===========================')
pprint.pprint(create_date_dict(dates, stocks))
