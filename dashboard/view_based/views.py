from django.shortcuts import render, redirect
from visitors_data_strg.models import Citizen




def createCitizen(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        middleName = request.POST.get('middleName')
        lastName = request.POST.get('lastName')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        image = request.FILES['visitor__image']

        citizen = Citizen(
            firstName=firstName, 
            middleName=middleName, 
            lastName=lastName,
            gender=gender,
            phone=phone,
            image=image,
            )

        citizen.save()
        return redirect('create_citizen')
    return render(request, 'citizen/add.html')