from django.shortcuts import render,redirect
from app24.models import Product
from django.core.paginator import Paginator


def showIndex(request):
    product_data = Product.objects.all()
    p = Paginator(product_data,3)
    page_no = request.GET.get("pno")
    if page_no:
        page = p.page(page_no)
    else:
        page = p.page(1)

    return render(request,"index.html",{"data":page})



def save_product(request):
    no = request.POST.get("t1")
    na = request.POST.get("t2")
    pr = request.POST.get("t3")
    q = request.POST.get("t4")
    img = request.FILES["t5"]
    Product(no = no,name=na,price=pr,quantity=q,image=img).save()
    return redirect('main')