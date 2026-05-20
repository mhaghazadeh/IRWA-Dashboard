from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):

#     # Page from the theme 
#     return render(request, 'pages/dashboard.html')
from django.shortcuts import render, redirect
from .models import Inventory,FieldRule
from .forms import InventoryForm
from django.contrib.auth.decorators import login_required, permission_required

import json

@login_required
@permission_required('yourapp.add_inventory', raise_exception=True)
def index(request):

    form = InventoryForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user
        obj.save()
        form.save_m2m()
        return redirect('index')

    items = Inventory.objects.select_related(
        'waste_type', 'waste_state', 'waste_class', 'site', 'facility'
    ).all().order_by('-created_at')

    rules = list(FieldRule.objects.values())

    return render(request, 'pages/dashboard.html', {
        'form': form,
        'items': items,
        'rules_json': json.dumps(rules)
    })
