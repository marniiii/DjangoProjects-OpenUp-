from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = form.save()    #changed this from account = authenticate(email=email, password=raw_password) 
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
            
    else:
        form = AccountAuthenticationForm()
        
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    subjects = ["AFST", "AMST", "ANTH", "APSC", "ARAB", "ART", "ARTH", "AMES", "APIA", "BIOL", "BUAD", "CHEM", "CHIN", "CLCV",
                "COLL", "CAMS", "CSCI", "CONS", "CRWR", "CRIN", "DANC", "DATA", "ECON", "EPPL", "EDUC", "ELEM", "ENGL", "ENSP",
                "EURS", "FMST", "FREN", "GSWS", "GIS", "GEOL", "GRMN", "GOVT", "GRAD", "GREK", "HBRW", "HISP", "HIST", "INTR",
                "INRL", "ITAL", "JAPN", "KINE", "LATN", "LAS", "LAW", "LING", "MSCI", "MATH", "MLSC", "MDLL", "MUSC", "NSCI",
                "PHIL", "PHYS", "PSYC", "PBHL", "PUBP", "RELG", "RUSN", "RPSS", "SOCL", "SPCH", "THEA", "WRIT"]
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                    "subject": request.POST['subject'],
                    "term": request.POST['term'],
                    "crn": request.POST['crn'],
            }
            form.save()
            context['success_msg'] = "Changes Saved"
    else:
        form = AccountUpdateForm(
            initial = {
                "subject": request.user.subject,
                "term": request.user.term,
                "crn": request.user.crn,
            }
        )
    context.update({
        'account_form': form,
        'subjects': subjects,
    })
    return render(request, 'account/account.html', context)





