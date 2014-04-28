from django.shortcuts import render, redirect, get_object_or_404

def everything(request):
    return render(request, 'everything.html', {})