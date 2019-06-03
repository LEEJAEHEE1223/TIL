from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'utils/index.html')


def artii(request, keyword):
    import art
    # result = art.tprint({keyword}, font='block')
    result = art.text2art(keyword, 'alpha')
    context = {
        'keyword': keyword,
        'result': result,
    }
    return render(request, 'utils/art.html', context)


def stock(request):
    pass  # TODO: 완성하기
    # return render(request, 'utils/stock.html')
