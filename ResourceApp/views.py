from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Resource,Borrowed_Resource
from DarajaApp.models import TransactionDetails
from .forms import ResourceForm


import datetime


def resource(request,id):
    resources = Resource.objects.all()
    form = ResourceForm()
    borrower = User.objects.get(id=id)
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            book_title = form.cleaned_data.get('borrowed')
            expiry_date = form.cleaned_data.get('recorded_returning_date')
            if borrower.borrowed_resource_set.filter(borrowed=book_title).exists():
                messages.info(request,f"The Book {book_title} already Borrowed")
            else:
                borrower.borrowed_resource_set.create(borrowed=book_title,recorded_returning_date=expiry_date)
                
    else:
        form = ResourceForm()


    return render(request,'ResourceApp/resources.html',{"resources":resources, "borrower":borrower, "form":form})

def borrowed(request,id):
    borrower = User.objects.get(id=id)
    if borrower.borrowed_resource_set.all().exists():
        for resource in borrower.borrowed_resource_set.all():
            expiry_date = resource.recorded_returning_date
            current=datetime.datetime.now()
    
            
            if int(current.strftime("%Y%m%d")) > int(expiry_date.strftime("%Y%m%d")):
                # A year late
                if int(expiry_date.strftime("%Y")) != int(current.strftime("%Y")):
                        yearly_charge = (int(current.strftime("%Y")) - int(expiry_date.strftime("%Y")))*365*2
                        monthly_charge = (int(current.strftime("%m")) - int(expiry_date.strftime("%m")))*30*2
                        daily_charge = (int(current.strftime("%d")) - int(expiry_date.strftime("%d")))*2
                        total_charges = yearly_charge+monthly_charge+daily_charge
                        print(total_charges)
                        if total_charges >1:
                            borrower.transactiondetails_set.update(user=borrower,amount=total_charges)

        
                        messages.info(request,f"{borrower.username} is expected to pay Ksh {total_charges} due to by_passing Expiry dates ")

                # A month late
                elif int(expiry_date.strftime("%m")) != int(current.strftime("%m")):
                    monthly_charge = (int(current.strftime("%m")) - int(expiry_date.strftime("%m")))*30*2
                    daily_charge = (int(current.strftime("%d")) - int(expiry_date.strftime("%d")))*2
                    total_charges = monthly_charge+daily_charge
                    print(total_charges)
                    if total_charges >1:
                        borrower.transactiondetails_set.update(user=borrower,amount=total_charges)

        
                    messages.info(request,f"{borrower.username} is expected to pay Ksh {total_charges} due to by_passing Expiry dates ")


                # Not expired
                else:
                    pass
                    
            # Not expired    
            else:
                pass
        
          
        


    return render(request,'ResourceApp/borrowed.html',{"borrower":borrower})

