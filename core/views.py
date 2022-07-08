from django.shortcuts import render, HttpResponse
import json
import datetime
# Create your views here.


def greeting(request):
    context_dict = {
        'users': [
            {
                'name': 'Mher',
                'surname': 'Petrosyan',
                'is_verified': True,
                'age': 17,
            },
            {
                'name': 'John',
                'surname': 'Dohn',
                'is_verified': False,
                'age': 15,
            }
        ]
    }
    return render(request, 'core/greeting.html', context=context_dict)


def hello(request):
    return render(request, 'core/hello.html')


def present(request):
    intro = HttpResponse("""<h2> We are going to learn django framework.</h2>
            \n<h2>It seems a little difficult, but hope that you will make it and soon will get an internship.</h2>""")
    return intro


def curr_time(request):
    current_time = datetime.date.today()
    response = f'Today is {current_time}, the weather is fine and the sun is shining.'
    return HttpResponse(response)


def dict_num_square(request):
    dict_ = {i: i**2 for i in range(1, 16)}
    # for i in range(1, 16):
    #     dict_[i] = i ** 2
    return HttpResponse(json.dumps(dict_))


def intro_patterns(request):
    pattern_intro = """<h1> Here are the paths. </h1>
    \n <h2>Type http://127.0.0.1:8000/admin - to get to the admin page.</h2> 
    \n <h2>Type http://127.0.0.1:8000/greeting - to say Hi to our lovely Django.</h2>
    \n <h2>Type http://127.0.0.1:8000/intro - to get the introduction.</h2>
    \n <h2>Type http://127.0.0.1:8000/date - to get the current date.</h2>
    \n <h2>Type http://127.0.0.1:8000/dictionary - to get the square of numbers between 1-15.</h2> 
    """
    return HttpResponse(pattern_intro)