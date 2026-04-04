from django.shortcuts import render
def lab5_links(request):
    return render(request, 'bookmodule/links.html')

def lab5_formatting(request):
    return render(request, 'bookmodule/formatting.html')

def lab5_listing(request):
    return render(request, 'bookmodule/listing.html')

def lab5_tables(request):
    return render(request, 'bookmodule/tables.html')
