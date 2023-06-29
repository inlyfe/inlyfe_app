from django.urls import path, include
from .views import( 
    ListVisitorView, Kyc,
    visitorToolKIt,
    addCitizenView,
    office_visitted_purpose_save,
    save_visitor,
    citizenFormView,
    console,
    )
urlpatterns = [
    path('',  console, name="visitor_console"),
    path('visitors/',  ListVisitorView, name="visitor_list"),
    path('visitors/toolkit',  visitorToolKIt, name="visitor_toolkit"),
    path('visitor_register/',  addCitizenView, name="visitor_register"),
    path('add/',  citizenFormView, name="add"),
    path('next_screen/',  office_visitted_purpose_save, name="office_visited_screen"),
    path('save_visitor/',  save_visitor, name="save_visitor"),

    path('check_visitor/',  Kyc, name="visitor_check"),
]