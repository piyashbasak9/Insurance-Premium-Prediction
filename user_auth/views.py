from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserRegisterForm, EmailVerificationForm
from .models import EmailVerification
from django.contrib.auth.models import User

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Check if email already exists
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registered.')
                return render(request, 'registration/register.html', {'form': form})
                
            try:
                # Store registration data in session
                request.session['reg_data'] = {
                    'username': form.cleaned_data.get('username'),
                    'email': email,
                    'password1': form.cleaned_data.get('password1')
                }
                code = EmailVerification.generate_code()
                request.session['verification_code'] = code
                
                # Send verification email
                send_mail(
                    'Verify your email - Insurance Premium Prediction',
                    f'Hello {form.cleaned_data.get("username")},\n\n'
                    f'Your verification code is: {code}\n\n'
                    f'This code will expire in 24 hours.\n\n'
                    f'If you did not request this code, please ignore this email.',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.info(request, 'Please check your email for the verification code.')
                return redirect('verify_email')
            except Exception as e:
                messages.error(request, 'Error sending verification email. Please try again.')
                # Clean up session data in case of error
                request.session.pop('reg_data', None)
                request.session.pop('verification_code', None)
    else:
        form = UserRegisterForm()
    
    return render(request, 'registration/register.html', {'form': form, 'title': 'Register'})

def verify_email(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    reg_data = request.session.get('reg_data')
    sent_code = request.session.get('verification_code')
    
    if not reg_data or not sent_code:
        messages.error(request, 'Registration session expired. Please register again.')
        # Clean up any partial session data
        request.session.pop('reg_data', None)
        request.session.pop('verification_code', None)
        return redirect('register')
    
    if request.method == 'POST':
        form = EmailVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('verification_code')
            if code == sent_code:
                try:
                    # Check again if email is unique before creating user
                    if User.objects.filter(email=reg_data['email']).exists():
                        messages.error(request, 'This email was registered by someone else while you were verifying. Please register with a different email.')
                        request.session.pop('reg_data', None)
                        request.session.pop('verification_code', None)
                        return redirect('register')
                    
                    # Create user
                    user = User.objects.create_user(
                        username=reg_data['username'],
                        email=reg_data['email'],
                        password=reg_data['password1'],
                        is_active=True
                    )
                    
                    # Create verification record
                    EmailVerification.objects.create(
                        user=user,
                        verification_code=code,
                        is_verified=True
                    )
                    
                    # Clean up session
                    request.session.pop('reg_data', None)
                    request.session.pop('verification_code', None)
                    
                    messages.success(request, 'Account created successfully! You can now login.')
                    return redirect('login')
                    
                except Exception as e:
                    messages.error(request, 'Error creating account. Please try registering again.')
                    # Clean up session on error
                    request.session.pop('reg_data', None)
                    request.session.pop('verification_code', None)
                    return redirect('register')
            else:
                messages.error(request, 'Invalid verification code. Please try again.')
    else:
        form = EmailVerificationForm()
    
    return render(request, 'registration/verify_email.html', {
        'form': form,
        'title': 'Verify Email',
        'email': reg_data.get('email')  # Show email being verified in template
    })

def user_login(request):
    if request.user.is_authenticated:
        return redirect('')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    next_url = request.GET.get('next', 'index')
                    messages.success(request, f'Welcome back, {username}!')
                    return redirect(next_url)
                else:
                    messages.error(request, 'Account is not activated. Please verify your email.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please fill in both username and password.')
    
    return render(request, 'registration/login.html', {'title': 'Login'})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('index')

@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')