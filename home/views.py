from django.shortcuts import render
from django.http import HttpResponse

import joblib

model = joblib.load('static/insurance_premium_model.pkl')

# Create your views here.


def index(request):
    # return HttpResponse("This is home page of Insurance Premium Prediction")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("This is about page of Insurance Premium Prediction")
    return render(request, 'about.html')

def contract(request):
    # return HttpResponse("This is contract page of Insurance Premium Prediction")
    return render(request, 'contract.html')

def prediction(request):
    # return HttpResponse("This is prediction page of Insurance Premium Prediction")
    if request.method == "POST":
        age = int(request.POST.get("age"))
        sex = int(request.POST.get("sex"))
        bmi = float(request.POST.get("bmi"))
        children = int(request.POST.get("children"))
        smoker = int(request.POST.get("smoker"))
        region = int(request.POST.get("region"))

        print(age, sex, bmi, children, smoker, region)

        pred = model.predict([[age, sex, bmi, children, smoker, region]])

        print(pred)

        output = {
            'output' : round(pred[0], 2)
        }

        return render(request, 'prediction.html', output)


    else :
        return render(request, 'prediction.html')

