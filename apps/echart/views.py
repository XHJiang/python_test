from django.shortcuts import render, HttpResponse

# Create your views here.

def echart(request):
    return render(request, 'echart.html')
    # return HttpResponse("echart")

def baidu(request):
    return render(request, 'test.html')