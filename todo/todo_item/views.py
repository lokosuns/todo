from django.shortcuts import render

data = {
    'lists': [
        {'name': 'Купить торт', 'is_done': True, 'date': '01.05.2020'},
        {'name': 'Заказать цветы', 'is_done': False},
        {'name': 'Пригласить друзей', 'is_done': True, 'date': '20.04.2020'},
        {'name': 'Сделать фотки', 'is_done': False},
        {'name': 'Купить подарок', 'is_done': True, 'date': '10.03.2020'}
    ],
    'user_name': 'admin',
}


def todo_item_view(request):
    context = data
    return render(request, 'list.html', context)