import pandas as pd

TOP = '''<!DOCTYPE html>
<html>
    <head>
        <title>Broccoli Questionnaire</title>
    </head>
    <body>
        <form action = "/thankyou" method="POST">
            <table border="1">
'''
INDENT = "            "
BOTTOM = '''            </table>
            <p><label for="name">Your name (optional):</label>
            <input type="text" id="name" value=""></p>
            <p><input type ='submit' value='Submit'/></p>
        </form>
    </body>
</html>
'''

if __name__ == '__main__':
    df = pd.read_csv('data/foods.csv')
    foods = df['Food'].to_list()
    f = open("templates/survey.html", "w")
    f.write(TOP)

    i=1
    for food in foods:
        slug = food.replace(' ', '')
        filename = f'static/images/{slug}.jpg'
        f.write(f'{INDENT}<tr><td>{i}</td><td>{food}</td><td><img src="{filename}" alt="picture of {food}"></td>\n')
        f.write(f'{INDENT}    <td><input type="radio" id="{slug}-like" name="{slug}" value="1"><label for="{slug}-like">like</label><br>\n')
        f.write(f'{INDENT}    <input type="radio" id="{slug}-neutral" name="{slug}" value="0" checked><label for="{slug}-neutral">neutral</label><br>\n')
        f.write(f'{INDENT}    <input type="radio" id="{slug}-dislike" name="{slug}" value="-1"><label for="{slug}-dislike">dislike</label></td></tr>\n')
        i += 1

    f.write(BOTTOM)
    f.close()
