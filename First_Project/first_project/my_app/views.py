from django.shortcuts import render,get_object_or_404,redirect
from .models import Table,About,Sing_up
from .forms import ContactForm


# Create your views here.
def home(request):
    table=Table.objects.all()
    return render(request,'my_app/index.html',{'table':table})


def detail(request,m_id):
    detail=get_object_or_404(Table,pk=m_id)
    print(detail)
    return render(request,'my_app/detail.html',{'detail':detail})


def about(request):
    
    form = ContactForm()   # ফাঁকা form

    if request.method == "POST":
        form = ContactForm(request.POST)  # ডাটা নেওয়া হলো
        if form.is_valid():
            # এখানে valid হলে কাজ করা যাবে
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, email, message)  # test করার জন্য
    
    
    
    info=About.objects.all()
    return render(request,'my_app/about.html',{'info':info,'form':form})



def login(request):
    if request.method == "POST":
        name=request.POST.get("name")
        try:
            user = Sing_up.objects.get(name=name)  # ডাটাবেজ থেকে ইউজার খুঁজবে
            return redirect('profile', user_id=user.id)  # profile view এ পাঠিয়ে দেবে
        except Sing_up.DoesNotExist:
            return render(request, 'my_app/login.html', {'error': 'Email not found!'})
    
    
    return render(request,'my_app/login.html')





def profile(request,user_id):
    data=get_object_or_404(Sing_up,pk=user_id)
    return render(request,'my_app/profile.html',{'data':data})












def sing(request):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        msg=request.POST.get("msg")
        image=request.FILES.get("image")
        passw=request.POST.get("pass")
        
        
        Sing_up.objects.create(
            name=name,
            email=email,
            message=msg,
            image=image,
            passw=passw
            
        )
        
    
    
    
    return render(request,'my_app/sing.html')
