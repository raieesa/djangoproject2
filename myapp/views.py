from django.shortcuts import render,redirect
from .models import Register,Gallery
from .forms import RegisterForm,LoginForm,UpdatePassword,UpdateGallery
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return render(request,'index.html')
def register(request):
	if request.method=='POST':
		form=RegisterForm(request.POST or None,request.FILES)
		if form.is_valid():
			name=form.cleaned_data['Name']
			email=form.cleaned_data['Email']
			place=form.cleaned_data['Place']
			photo=form.cleaned_data['Photo']
			password=form.cleaned_data['Password']
			cpassword=form.cleaned_data['CPassword']

			ur=Register.objects.filter(Email=email).exists()
			if ur:
				msg='Email already exist'
				return render(request,'register.html',{'error':msg})
			elif password!=cpassword:
				msg='Password does not match'
				return render(request,'register.html',{'error':msg})
			else:
				reg=Register(Name=name,Email=email,Place=place,Photo=photo,Password=password)
				reg.save()
				return redirect('/')
	else:
		form=RegisterForm()
	return render(request,'register.html',{'form':form})

def login(request):
	if request.method=='POST':
		form=LoginForm(request.POST or None)
		if form.is_valid():
			email=form.cleaned_data['Email']
			password=form.cleaned_data['Password']

			ur=Register.objects.get(Email=email)
			if not ur:
				msg='Email does not exist'
				return render(request,'login.html',{'error':msg})
			elif ur.Password!=password:
				msg='Incorrect password'
				return render(request,'login.html',{'error':msg})
			else:
				request.session['sid']=ur.id
				return redirect('/home/%s' % ur.id)
	else:
		form=LoginForm()
	return render(request,'login.html',{'form':form})

def home(request,id):
	uid=request.session['sid']
	user=Register.objects.get(id=id)
	return render(request,'home.html',{'user':user})

def logout(request):
	try:
		del request.session['sid']
		return redirect('/')
	except:
		pass

def passwordchange(request,id):
	uid=request.session['sid']
	user=Register.objects.get(id=id)
	if request.method=='POST':
		form=UpdatePassword(request.POST)
		if form.is_valid():
			password=form.cleaned_data['CurrentPassword']
			newpass=form.cleaned_data['NewPassword']
			cpass=form.cleaned_data['CPassword']

			if user.Password!=password:
				msg='Incorrect Password'
				return render(request,'passwordchange.html',{'error':msg})
			elif newpass!=cpass:
				msg='Password Mismatch'
				return render(request,'passwordchange.html',{'error':msg})
			else:
				user.Password=newpass
				user.save()
				return redirect('/home/%s' % user.id)

	else:
		form=UpdatePassword()
	return render(request,'passwordchange.html',{'form':form})

def viewprofile(request,id):
	uid=request.session['sid']
	user=Register.objects.get(id=id)
	return render(request,'viewprofile.html',{'user':user})

def gallery(request):
	if request.method=='POST':
		form=UpdateGallery(request.POST,request.FILES)
		if form.is_valid():
			form.save()
		return redirect('/')

	else:
		form=UpdateGallery()
	return render(request,'gallery.html',{'form':form})

def viewgallery(request):
	data=Gallery.objects.all()
	return render(request,'viewgallery.html',{'data':data})


	