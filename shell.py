"""
https://www.youtube.com/watch?v=Eythq9848Fg&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD
"""

import basic

while True:
    text = input("basic > ")
    result, error = basic.run("<stdin>", text)

    if error:
        print(error.as_string())
    else:
        print(result)
