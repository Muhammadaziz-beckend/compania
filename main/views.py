from django.shortcuts import render, get_object_or_404, redirect
from main.models import Sotrudnic, Catigori_woork, Task
from django.core.paginator import Paginator
from .forms import SotrudnicForm, TaskForm, UpdateForm


def index(req):
    form = SotrudnicForm()
    if req.method == "POST":
        create(req)
        # form = SotrudnicForm(req.POST, req.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect("home")
    work = Sotrudnic.objects.all()

    deliteOk = req.GET.get("deliteOk", None)

    if deliteOk:
        id_del = Sotrudnic.objects.get(pk=deliteOk)
        id_del.delete()
        return redirect("home")

    sorch_work = req.GET.get("sorch", 0)

    if sorch_work:
        work = Sotrudnic.objects.filter(name__icontains=sorch_work)

    catigori_work = req.GET.get("catigori", 0)

    if catigori_work:
        work = Sotrudnic.objects.filter(jod_id__name__icontains=catigori_work)

    page = int(req.GET.get("page", 1))
    page_size = int(req.GET.get("page_size", 8))

    pagin = Paginator(work, page_size)
    work = pagin.get_page(page)

    if not catigori_work:
        catigori_work = 0

    return render(
        req,
        "components/workers.html",
        {
            "h1": "Сатрудники",
            "activ": False,
            "img_user": work,
            "catigori": Catigori_woork.objects.all(),
            "catigori_peng": catigori_work,
            "form": form,
        },
    )

def create(req):
    form = SotrudnicForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
        return redirect("home")
    pass


def order(req):
    sorch_work = req.GET.get("sorch", 0)
    work = Task.objects.all()
    work_sotrudnik = Sotrudnic.objects.all()
    if sorch_work:
        work = Task.objects.filter(name__icontains=sorch_work)

    page = int(req.GET.get("page", 1))
    page_size = int(req.GET.get("page_size", 8))

    pagin = Paginator(work, page_size)
    work = pagin.get_page(page)

    deliteOK = req.GET.get("deliteOk", None)

    if deliteOK:
        del_order = Task.objects.get(pk=deliteOK)
        del_order.delete()
        redirect("order")
    form = TaskForm()
    if req.method == "POST":
        form = TaskForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect("order")

    return render(
        req,
        "components/order.html",
        {
            "h1": "Задачи",
            "activ": True,
            "img_user": work,
            "work": work_sotrudnik,
            "form": form,
        },
    )


def order_main(req, id):
    work = Task.objects.get(id=id)
    dev = get_object_or_404(Task, id=id)

    return render(
        req,
        "components/order_main.html",
        {
            "h1": "Задача",
            "activ": True,
            "order": work,
            "dev": dev,
        },
    )


def update(req, id):
    work = get_object_or_404(Task, id=id)

    form = UpdateForm(instance=work)
    if req.method == 'POST':
        form = UpdateForm(req.POST,req.FILES,instance=work)
        if form.is_valid():
            form.save()
            return redirect('order')

    return render(
        req,
        "components/udate.html",
        {
            "order_q": work,
            "forms": form,
            "catigori": Sotrudnic.objects.all()
        },
    )
