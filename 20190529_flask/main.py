from flask import Flask, render_template
import requests
import random
import json
import lotto_package

app = Flask(__name__)

cnt = 0
price = 0
history = ''


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
    global cnt
    global price
    global history

    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    data = requests.get(url).text
    lotto_data = json.loads(data)
    print(lotto_data)

    lotto_numbers = []
    for key, value in lotto_data.items():
        print(key, value)
        if 'drwtNo' in key:
            lotto_numbers.append(value)
        elif 'bnusNo' in key:
            bonus_number = value
    print('가져온 로또번호:', lotto_numbers, '보너스번호:', bonus_number)

    while cnt < 10000:
        my_lotto = lotto_package.get_lotto_numbers(lotto_numbers, bonus_number)
         # {'lotto_numbers': lotto_numbers,
         #        'my_numbers': my_numbers,
         #        'diff_nums': diff_nums,
         #        'result': result,
         #        'output': output
         #        }

        my_numbers = my_lotto['my_numbers']
        diff_nums = my_lotto['diff_nums']
        result = my_lotto['result']
        output = my_lotto['output']

        if output.find('미당첨') < 0:
            history += f'{cnt}회 {output}\n'

        cnt += 1
        price += 1000

    num1 = history.count('1등')
    num2 = history.count('2등')
    num3 = history.count('3등')
    num4 = history.count('4등')
    num5 = history.count('5등')

    return render_template(
        'lotto.html',
        lotto_numbers=lotto_numbers,
        bonus=bonus_number,
        my_numbers=my_numbers,
        result=output,
        ordr=num,
        price=format(price, ','),
        history=history,
        num1=num1,
        num2=num2,
        num3=num3,
        num4=num4,
        num5=num5
    )


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




