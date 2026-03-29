from django.shortcuts import render, redirect
from .models import AI_Links
from django.contrib.auth.decorators import login_required

# Create your views here.

def Index(request):
    category = request.GET.get('category')

    if category:
        data = AI_Links.objects.filter(category=category)
    else:
        data = AI_Links.objects.all()

    categories = AI_Links.objects.values_list('category', flat=True).distinct()

    return render(request, 'app/index.html', {
        'data': data,
        'categories': categories
    })

@login_required
def Form(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        website_name = request.POST.get('web-name')
        website_link = request.POST.get('web-link')
        description = request.POST.get('description')

        AI_Links.objects.create(
            category=category,
            website_name=website_name,
            website_link=website_link,
            description=description
        )

        return redirect('home')

    return render(request, 'app/Form.html')