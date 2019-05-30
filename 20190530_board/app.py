from flask import Flask, render_template, request
from iexfinance.stocks import Stock
import pprint

app = Flask(__name__)
pp = pprint.PrettyPrinter()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_stock')
def stock():
    return render_template(
        'search_stock.html',
        is_first_search=True,
    )


@app.route('/search_result')
def result():
    # print('request.args:', request.args)
    input_keyword = request.args.get('keyword')
    print('input keyword:', input_keyword)

    TOKEN = 'pk_87301e7c4b334621abd8a06136d1178e'

    try:
        stock = Stock(input_keyword, token=TOKEN)
        data = stock.get_quote()
        # print(data)
    except Exception as e:
        print('ㅠㅠ 에러남....')
        print(e)

        return render_template(
            'search_stock.html',
            errFlag=True,
        )

    pp.pprint(data)
    print(data['companyName'], data['latestPrice'])

    return render_template(
        'search_stock.html',
        errFlag=False,
        companyName=data['companyName'],
        latestPrice=data['latestPrice'],
        is_first_search=False,
    )


if __name__ == '__main__':
    app.run(debug=True)
