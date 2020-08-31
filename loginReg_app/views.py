from django.shortcuts import render, redirect
from django.contrib import messages
from loginReg_app.models import User
import bcrypt

# Create your views here.
def loginReg(request):
  return render(request, "loginReg.html")

def process_reg(request):
  errors = User.objects.register_validator(request.POST)
  if len(errors) > 0:
    for key, error_msg in errors.items():
      messages.error(request, error_msg)
    return redirect('/')

  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  email = request.POST['email']
  password = request.POST['password']
  pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
  print(f"pw hash: {pw_hash}")

  new_user = User.objects.create(first_name=first_name, last_name=last_name,email=email, password=pw_hash)
  request.session['user_id'] = new_user.id
  messages.success(request, "Successfully registered!")
  return redirect("/")

def process_login(request):
  errors = User.objects.login_validator(request.POST)
  if len(errors) > 0:
    for key, error_msg in errors.items():
      messages.error(request, error_msg)
    return redirect('/')
  login_user_list = User.objects.filter(email=request.POST['email'])
  if login_user_list:
    this_user = login_user_list[0]
    if bcrypt.checkpw(request.POST['password'].encode(), this_user.password.encode()):
      request.session['user_id'] = this_user.id
      messages.success(request, "successfully logged in!")
      return redirect('/books')
  else:
    messages.error(request, "Password did not match")
  return redirect('/')

def logout(request):
  request.session.flush()
  return redirect('/')
