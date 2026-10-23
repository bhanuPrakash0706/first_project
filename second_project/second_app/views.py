from django.http import HttpResponse
from .forms import ReservationsFrom
from django.shortcuts import render

def home(request):
    form = ReservationsFrom()
    
    if request.method=='POST':
        form =ReservationsFrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("SUCCESS")
    return render(request,'index.html',{'form':form})
