import datetime
import requests
import pywhatkit


def get_random_meal():
    MEAL_URL = "http://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(MEAL_URL)
    if response.status_code < 400:
        meal_dict = response.json()
        meal = meal_dict['meals'][0]['strMeal']
        instructions = meal_dict['meals'][0]['strInstructions']

        ingredients = []

        for i in range(1, 20):
            ingredient = meal_dict['meals'][0][f'strIngredient{i}']
            if ingredient:
                ingredients.append(ingredient)
                ingredients = list(filter(None, ingredients))
                return meal, instructions, ingredients
    else:
        raise Exception(f"there is an error: {response.status_code}")


def send_message(ingredients, meal, instructions):
    message = (
        f"Hey sweetie, i was thinking about tonight dinner and i would like to eat {meal}, i would like if you go "
        f"to the store and buy {instructions} ."
        f"if you want to check how to cook here some instructions:\n{ingredients}")
    phone_number = "+972586021864"
    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    current_minute = current_time.minute
    pywhatkit.sendwhatmsg(phone_number, message, current_hour, current_minute + 1)


if __name__ == '__main__':
    try:
        meal, ingredients, instructions = get_random_meal()
        send_message(ingredients, meal, instructions)
    except Exception as e:
        print(e)
