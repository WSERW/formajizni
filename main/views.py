from .forms import LeadForm
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import FAQ, Category, Work
# Create your views here.


def index(request):
    faqs = FAQ.objects.all()
    categories = Category.objects.all()
    works = Work.objects.all()

    return render(request, 'main/index.html', {'faqs': faqs, 'categories': categories, 'works': works})


def lead_form_view(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Ваша заявка успешно отправлена!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'message': 'Неверный запрос'}, status=400)
