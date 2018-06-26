from django.shortcuts import render,redirect,HttpResponse
from contacts.forms import ContactForm
from django.contrib.auth.decorators import login_required
# def sendMessage(request):
#     return  HttpResponse("Hi")

# Create your views here.
@login_required(login_url='/login')
def sendMessage(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #save to the database
            instance= form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('contacts:sendMessage')
    else:
        form=ContactForm()
    return render(request,'contacts/contact.html',{ 'form':form })