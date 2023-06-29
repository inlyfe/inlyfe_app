from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from visitors.models import Visitor 
from visitors_data_strg.models import Citizen
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from nida import load_user
import json





def console(request):
    visitors = Visitor.objects.all().order_by('in_time')
    visitor_total = Visitor.objects.all().count()
    visitor_by_total = Visitor.objects.all().count()
    print(visitor_total)
    context = {
        'visitors': visitors,
        'total_visitors': visitor_total,
        'visitor_by_total': visitor_by_total,
    }
    return render(request, 'visitors/dashboard/index.html', context)



def ListVisitorView(request):
    visitors = Visitor.objects.all().order_by('in_time')
    visitor_total = Visitor.objects.all().count()
    visitor_by_total = Visitor.objects.all().count()
    print(visitor_total)
    context = {
        'visitors': visitors,
        'total_visitors': visitor_total,
        'visitor_by_total': visitor_by_total,
    }
    return render(request, 'visitors/visitor_list/index.html', context)



def visitorToolKIt(request):
    visitors = Visitor.objects.all().order_by('in_time')
   
    context = {
        'visitors': visitors,
    }
    return render(request, 'visitors/visitor_toolkit/index.html', context)









def addCitizenView(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        lastName = json.load(request)['lastName']
        firstName = json.load(request)['firstName']
        middleName = json.load(request)['middleName']
        gender = json.load(request)['gender']
        phone = json.load(request)['phone']
        res = None
        visitor_registered = Citizen.objects.create(
            firstName=firstName,
            middleName=middleName,
            lastName=lastName,
            gender=gender,
            phone=phone,
        )

        data = Citizen.objects.get(visitor_registered)

        res.append(data)

        context = {}
        return JsonResponse({})
    return JsonResponse({})



def citizenFormView(request):
    return render(request, 'citizen/add.html')


def citizenListView(request):
    return render(request, 'citizen/list.html')






# @csrf_exempt 
# def Kyc(request):
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         id_number = json.load(request)['id_number']
#         visitor_check = Citizen.objects.filter(id_number=id_number).exists()
#         visitor = Citizen.objects.get(id_number=id_number)
#         # user_info = load_user(national_id=id_number)
#         print(visitor)
#         print(visitor_check)

#         print(id_number)
      
#         res = None
#         if visitor_check == True:
#             if visitor == id_number :
#                 ui =  Citizen.objects.get(id_number=id_number)
                
#                 data = []
#                 items = {
#                     'NIN': ui.id_number,
#                     'FisrtName': ui.first_name,
#                     'MiddleName': ui.middle_name,
#                     'LastName': ui.last_name,
#                     'Sex': ui.gender
#                 }
#                 data.append(item)
                
#                 res = data
               
#         else:
#             res = 'No data match!'
#         return JsonResponse({'data': res})
#     return JsonResponse({})



def Kyc(request):
    context = {}
    if request.method == 'POST':
        id_number = request.POST.get('id_number')
        user_info = load_user(national_id=id_number)
        is_true  = Citizen.objects.filter(id_number=id_number).exists()
        res = None
        context = {}
        if is_true == True:
            data = None
            citizen_information = Citizen.objects.get(id_number=id_number)
            item = {
                    'id_number': citizen_information.id_number,
                    'FirstName': citizen_information.firstName,
                    'MiddleName': citizen_information.middleName,
                    'LastName': citizen_information.lastName,
                    'Sex': citizen_information.gender,
                    'image': citizen_information.image,
            }
            data = item
            res = data
        elif user_info is not None:
            if id_number == user_info.get('Nin'):
                ui = load_user(national_id=id_number)
                # print(ui)
                data = []
                item = {
                    'NIN': ui.Nin,
                    'FirstName': ui.Firstname,
                    'MiddleName': ui.Middlename,
                    'LastName': ui.Surname,
                    'Sex': ui.Sex,
                }
                data.append(item)
                res = data
        else:
            res = "we can't find a visitor"
        context = {
            'response': res
        }
        context = context
    return render(request, 'visitors/kyc/index.html', context)





def office_visitted_purpose_save(request):
    context = {}
    if request.method == 'POST':
        id_number = request.POST['id_number']
        visitor = Citizen.objects.get(id_number=id_number)
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        context = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'gender': gender,
            'image': visitor,
        }
        context = context
    return render(request, 'visitors/kyc/verify.html', context)



def save_visitor(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        office_visited = request.POST['office_visited']
        purpose = request.POST['purpose']
        gender = request.POST['gender']
        guest_from = request.POST['guest_from']
        phone = request.POST['phone']
        visitor_image = request.FILES['visitor_image']
        visitor_verified = Visitor(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            office_visited=office_visited,
            purpose=purpose,
            gender=gender,
            guest_from=guest_from,
            phone=phone,
            checked_in=True,
            visitor_image=visitor_image,
        )

        visitor_verified.save()
        return redirect("visitor_toolkit")


