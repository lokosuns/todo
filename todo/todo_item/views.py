from django.shortcuts import render

data = {
    'lists': [
        {'name': 'Хлеб', 'is_done': True},
        {'name': 'Рыба', 'is_done': False},
        {'name': 'Мука', 'is_done': True},
        {'name': 'Колбаса', 'is_done': False},
        {'name': 'Яйца', 'is_done': True}
    ],
    'user_name': 'admin',
}


def todo_item_view(request):
    context = data
    return render(request, 'index.html', context)