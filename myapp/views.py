from django.shortcuts import render, redirect
from .forms import MessageForms
def index(request):
    if request.method == 'POST':
        form = MessageForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MessageForms()
    return render(request,'index.html',{'form':form})

def main(request):
    return render(request,'main.html')

