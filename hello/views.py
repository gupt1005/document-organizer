'''
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction, connection
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_date
from .models import Document, Category


def hello_world(request):
    return HttpResponse("Hello World")


def health_check(request):
    """
    Used by Google Cloud to verify app is running.
    """
    return HttpResponse("OK", status=200)

def sanitize_date(value):
    """Parse and validate date input. Returns None if invalid."""
    if not value:
        return None
    #returns None if format is wrong
    parsed = parse_date(value)  
    return parsed


def sanitize_category_id(value):
    """Ensure category ID is a positive integer. Returns None if invalid."""
    if not value:
        return None
    try:
        cid = int(value)
        if cid <= 0:
            return None
        return cid
    except (ValueError, TypeError):
        return None


@login_required
def document_list(request):
    raw_category   = request.GET.get('category')
    raw_start_date = request.GET.get('start_date')
    raw_end_date   = request.GET.get('end_date')

    category   = sanitize_category_id(raw_category)
    start_date = sanitize_date(raw_start_date)
    end_date   = sanitize_date(raw_end_date)

    with transaction.atomic():
        documents = Document.objects.filter(user=request.user)

        if category:
            documents = documents.filter(category__id=category)
        if start_date:
            documents = documents.filter(renewal_date__gte=start_date)
        if end_date:
            documents = documents.filter(renewal_date__lte=end_date)

        categories = list(Category.objects.all())
        documents  = list(documents.select_related('category'))

    return render(request, 'hello/document_list.html', {
        'documents':         documents,
        'categories':        categories,
        'selected_category': raw_category,
        'selected_start':    raw_start_date,
        'selected_end':      raw_end_date,
    })


@login_required
@transaction.atomic
def document_create(request):
    """
    Transaction: wraps the full create in one atomic block.
    If anything fails (validation, DB error), nothing is saved.
    """
    if request.method == 'POST':
        name         = request.POST.get('name', '').strip()
        location     = request.POST.get('location', '').strip()
        notes        = request.POST.get('notes', '').strip()
        category_id  = sanitize_category_id(request.POST.get('category'))
        renewal_date = sanitize_date(request.POST.get('renewal_date'))

        if not name or not category_id:
            return render(request, 'hello/document_form.html', {
                'error': 'Name and category are required.',
                'categories': Category.objects.all(),
            })

        category = get_object_or_404(Category, id=category_id)

        Document.objects.create(
            user=request.user,
            name=name,
            location=location,
            notes=notes,
            category=category,
            renewal_date=renewal_date,
        )
        return redirect('document_list')

    return render(request, 'hello/document_form.html', {
        'categories': Category.objects.all(),
    })


@login_required
@transaction.atomic
def document_update(request, pk):
    """
    select_for_update() locks the row so concurrent edits don't overwrite
    each other (lost update prevention).
    Isolation: defaults to READ COMMITTED — sufficient for single-row updates.
    """
    doc = get_object_or_404(
        Document.objects.select_for_update(),
        pk=pk,
        #prevents users editing each other's documents
        user=request.user   
    )

    if request.method == 'POST':
        name         = request.POST.get('name', '').strip()
        location     = request.POST.get('location', '').strip()
        notes        = request.POST.get('notes', '').strip()
        category_id  = sanitize_category_id(request.POST.get('category'))
        renewal_date = sanitize_date(request.POST.get('renewal_date'))

        if not name or not category_id:
            return render(request, 'hello/document_form.html', {
                'doc': doc,
                'error': 'Name and category are required.',
                'categories': Category.objects.all(),
            })

        doc.name         = name
        doc.location     = location
        doc.notes        = notes
        doc.category     = get_object_or_404(Category, id=category_id)
        doc.renewal_date = renewal_date
        doc.save()
        return redirect('document_list')

    return render(request, 'hello/document_form.html', {
        'doc': doc,
        'categories': Category.objects.all(),
    })


@login_required
@transaction.atomic
def document_delete(request, pk):
    """
    Atomic delete — safe for future cascade scenarios (e.g. if you add
    related attachments that also need deleting in the same transaction).
    """
    doc = get_object_or_404(Document, pk=pk, user=request.user)
    if request.method == 'POST':
        doc.delete()
        return redirect('document_list')
    return render(request, 'hello/document_confirm_delete.html', {'doc': doc})

'''
def hello_world(request):
    return render(request, 'hello/hello.html')  



def document_list(request):
    category = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    documents = Document.objects.all()
    
    # Filter by category
    if category:
        documents = documents.filter(category__id=category)

    # Filter by start date
    if start_date:
        documents = documents.filter(renewal_date__gte=start_date)

    # Filter by end date
    if end_date:
        documents = documents.filter(renewal_date__lte=end_date)

    return render(request, 'hello/document_list.html', {
        'documents': documents,
        'categories': Category.objects.all()
    })
'''