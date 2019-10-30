from django.shortcuts import render

def post_list(request):
    return render(request, 'toptap/post_list.html', {})
