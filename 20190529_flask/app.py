from flask import Flask, render_template
import numpy as np
import requests
import random
import json

app = Flask(__name__)


# @app.route('/')
# def index():
#     return """
#         <h1>안녕하세요!</h1>
#         <p>This is 4th4deep</p>
#     """

@app.route('/')
def index():
    # render_template 함수가  templates 폴더안의 소스를 가져온다.
    return render_template('index.html')


@app.route('/lotto')
def lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    return f'{lucky_numbers}'


@app.route('/pick_lotto')
def pick_lotto():
    lucky_numbers = random.sample(range(1, 46), 6)
    print( type(lucky_numbers) )
    print('정렬:', sorted(lucky_numbers) )
    print('원본:', lucky_numbers )
    print('lucky_numbers.sort():', lucky_numbers.sort())
    print('원본(바뀜):', lucky_numbers)

    tuples_numbers = random.sample(range(1, 46), 6)
    tuples_numbers = tuple(tuples_numbers)
    print( type(tuples_numbers) )
    print('tuples_numbers.sort():', sorted(tuples_numbers) )
    print('튜플도 바뀌나??:', tuples_numbers)
    return render_template('pick_lotto.html',  numbers=lucky_numbers)


@app.route('/lotto/<num>')
def find_lotto(num):

    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    data = requests.get(url).text
    lotto_data = json.loads(data)

    lotto_numbers = []
    for key, value in lotto_data.items():
        print(key, value)
        if 'drwtNo' in key:
            lotto_numbers.append(value)

    # for i in range(1,7):
    #     lotto_idx = f'drwtNo{i}'
    #     print('json key:', lotto_idx)
    #     lotto_numbers.append(lotto_data.get(lotto_idx))
    print('가져온 로또번호:', lotto_numbers)
    return render_template('pick_lotto.html',  numbers=lotto_numbers, ordr=num)


# @app.route('/square/<num>')
# def square(num):
#     result = int(num) ** 2
#     return f'{result}'


@app.route('/square/<int:num>')
def square(num):
    result = num ** 2
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)




