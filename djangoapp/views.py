from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import ModelAuto
from .forms import ModelAutoForm


# Create your views here.
def model_index(request):
    
    return render(request, 'excar/index.html')

def model_catalog(request):
    ModelAutos = ModelAuto.objects.all()
    return render(request, 'excar/catalog.html', {'ModelAutos' : ModelAutos})

def model_show(request, pk):
    modelAuto = get_object_or_404(ModelAuto, pk=pk)
    return render(request, 'excar/show.html', {'modelAuto' : modelAuto})

def model_new(request):    
    if request.method == "POST":
        form = ModelAutoForm(request.POST, request.FILES)
        if form.is_valid():
            modelAuto = form.save(commit=False)
            if request.FILES:
                #Сохранение основного изображения
                with open(f"djangoapp/uploads/{request.FILES['izobrazhenie'].name}", "wb+") as destination:
                    for chunk in request.FILES['izobrazhenie'].chunks():
                        destination.write(chunk)
                #Сохранение изображения особенностей
                        
                with open(f"djangoapp/uploads/{request.FILES['photoosobennosti'].name}", "wb+") as destination:
                    for chunk in request.FILES['photoosobennosti'].chunks():
                        destination.write(chunk)


                #Сохранение изображения ленты №1
                with open(f"djangoapp/uploads/{request.FILES['photo1'].name}", "wb+") as destination:
                    for chunk in request.FILES['photo1'].chunks():
                        destination.write(chunk)                        

                #Сохранение изображения ленты №2
                with open(f"djangoapp/uploads/{request.FILES['photo2'].name}", "wb+") as destination:
                    for chunk in request.FILES['photo2'].chunks():
                        destination.write(chunk)     
                #Сохранение изображения ленты №3
                with open(f"djangoapp/uploads/{request.FILES['photo3'].name}", "wb+") as destination:
                    for chunk in request.FILES['photo3'].chunks():
                        destination.write(chunk)     

            modelAuto.save()
            form.save_m2m()
            return redirect('catalog')
    else:
        form = ModelAutoForm()
    return render(request, 'excar/edit.html', {'form' : form})

def model_edit(request, pk):    

    modelAuto = get_object_or_404(ModelAuto, pk=pk)
    izobr = modelAuto.izobrazhenie
    izobr_os = modelAuto.photoosobennosti
    izobr1 = modelAuto.photo1
    izobr2 = modelAuto.photo2
    izobr3 = modelAuto.photo3
    if request.method == "POST":
        form = ModelAutoForm(request.POST, request.FILES, instance=modelAuto)
        if form.is_valid():
            modelAuto = form.save(commit=False)
            modelAuto.data_izmen = timezone.now()

            #Восстановление фото
            modelAuto.izobrazhenie = izobr
            modelAuto.photoosobennosti = izobr_os
            modelAuto.photo1 = izobr1
            modelAuto.photo2 = izobr2
            modelAuto.photo3 = izobr3

            if request.FILES:
                with open(f"excar/uploads/{request.FILES['izobrazhenie'].name}", "wb+") as destination:
                    for chunk in request.FILES['izobrazhenie'].chunks():
                        destination.write(chunk)
                #Сохранение изображения особенностей
                        
                with open(f"excar/uploads/{request.FILES['photoosobennosti'].name}", "wb+") as destination:
                    for chunk in request.FILES['photoosobennosti'].chunks():
                        destination.write(chunk)


                #Сохранение изображения ленты №1
                with open(f"excar/uploads/{request.FILES['photo1'].name}", "wb+") as destination:
                    for chunk in request.FILES['photo1'].chunks():
                        destination.write(chunk)                        

                #Сохранение изображения ленты №2
                with open(f"excar/uploads/{request.FILES['photo2'].name}", "wb+") as destination:
                    for chunk in request.FILES['photo2'].chunks():
                        destination.write(chunk)     
                #Сохранение изображения ленты №3
                with open(f"excar/uploads/{request.FILES['photo3'].name}", "wb+") as destination:
                    for chunk in request.FILES['photo3'].chunks():
                        destination.write(chunk)   
            
            modelAuto.save()
            form.save_m2m()
            return redirect('catalog')
    else:
        form = ModelAutoForm(instance=modelAuto)
    return render(request, 'excar/edit.html', {'form' : form})


def model_delete(request, pk):    
    modelAuto = get_object_or_404(ModelAuto, pk=pk)
    modelAuto.delete()
    return redirect('catalog')