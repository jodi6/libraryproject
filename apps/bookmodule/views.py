from django.shortcuts import render
from django.db.models import Q, Count, Sum, Avg, Max, Min  # استيراد أدوات البحث المتقدم والحساب لـ Lab 8 [cite: 72, 82]
from .models import Book, Student, Address  # استيراد كل الموديلات المطلوبة للابات 7 و 8


# --- وظائف العرض الأساسية ---
def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, 'bookmodule/list_books.html')


def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')


def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


# --- وظائف Lab 5 ---
def lab5_links(request):
    return render(request, 'bookmodule/links.html')


def lab5_formatting(request):
    return render(request, 'bookmodule/formatting.html')


def lab5_listing(request):
    return render(request, 'bookmodule/listing.html')


def lab5_tables(request):
    return render(request, 'bookmodule/tables.html')


# --- وظيفة البحث (Lab 6) ---
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # البحث في قاعدة البيانات مباشرة بدلاً من القائمة اليدوية
        query = Q()
        if isTitle: query |= Q(title__icontains=string)
        if isAuthor: query |= Q(author__icontains=string)

        newBooks = Book.objects.filter(query)
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
    return render(request, 'bookmodule/search.html')


# --- وظائف Lab 7 (Queries) ---
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False) \
                  .filter(title__icontains='and') \
                  .filter(edition__gte=2) \
                  .exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    return render(request, 'bookmodule/index.html')


# --- وظائف Lab 8 (Advanced Models) ---

# Task 1: عرض الكتب التي سعرها أقل من أو يساوي 80 باستخدام Q operator
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))  #
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 2: طبعة > 3 و (العنوان أو الكاتب فيه 'qu') [cite: 79]
def lab8_task2(request):
    # (&) تعني AND، (|) تعني OR [cite: 79]
    query = Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    books = Book.objects.filter(query)
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 3: عكس المهمة الثانية (طبعة <= 3 و لا يوجد 'qu' في العنوان ولا الكاتب) [cite: 80]
def lab8_task3(request):
    # (~) تعني NOT أو النفي [cite: 80]
    query = Q(edition__lte=3) & ~Q(title__icontains='qu') & ~Q(author__icontains='qu')
    books = Book.objects.filter(query)
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 4: ترتيب الكتب حسب العنوان أبجدياً [cite: 81]
def lab8_task4(request):
    books = Book.objects.all().order_by('title') # [cite: 81]
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Task 5: العمليات الحسابية (إحصائيات الأسعار) [cite: 82]
def lab8_task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total=Sum('price'),
        avg=Avg('price'),
        max=Max('price'),
        min=Min('price')
    ) # [cite: 82]
    return render(request, 'bookmodule/lab8_stats.html', {'stats': stats})

# Task 7: عدد الطلاب في كل مدينة [cite: 98]
def lab8_task7(request):
    # annotate تضيف معلومة (عدد الطلاب) لكل مدينة [cite: 98]
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/city_stats.html', {'cities': cities})