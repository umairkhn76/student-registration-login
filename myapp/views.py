from django.shortcuts import render,redirect
from .models import Product, Student
# Create your views here.

def register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')

        Student.objects.create(name=name,email=email,phone=phone,password=password)
        return redirect("login")

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        student=Student.objects.filter(email=email,password=password).first()
        if student:
            request.session['student_id'] = student.id
            return redirect('add_product')
        else:
            return render(request, 'login.html',{
                'error' : 'invalid email or password'
            })

    return render(request,'login.html')

def add_product(request):

    if request.method == "POST":

        name = request.POST.get("name")
        price = request.POST.get("price")
        product_id = request.POST.get("product_id")

        student_id = request.session.get("student_id")

        student = Student.objects.get(id=student_id)

        Product.objects.create(
            student=student,
            name=name,
            price=price,
            product_id=product_id
        )

        return redirect("add_product")

    return render(request, "add_product.html")

def my_products(request):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("login")

    products = Product.objects.filter(student_id=student_id)

    return render(request, "my_products.html", {
        "products": products
    })

def delete_product(request, id):

    student_id = request.session.get("student_id")

    if not student_id:
        return redirect("login")

    product = Product.objects.filter(
        id=id,
        student_id=student_id
    ).first()

    if not product:
        return redirect("my_products")

    if request.method == "POST":

        product.delete()

        return redirect("my_products")

    return redirect("my_products")

def logout(request):
    request.session.flush()
    return redirect("login")
    