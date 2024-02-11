from django.http import HttpResponse


from . import tasks


def home(request):
    tasks.download_an_img.delay()
    return HttpResponse('<h1>Upload img</h1>')
