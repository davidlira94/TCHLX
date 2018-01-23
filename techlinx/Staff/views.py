from django.shortcuts import render, get_object_or_404
from .models import Staff
# Create your views here.


def autor(request,slug):
    autor = get_object_or_404(Staff,slug=slug)
    image = "/static/img/sidebar.jpg"
    return render(request,'blog/autores/perfil.html',{'autor':autor,'image':image})
