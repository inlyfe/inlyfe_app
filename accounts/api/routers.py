from django.urls import path 
from django.views.decorators.csrf import csrf_exempt
from accounts.api.views import (
    VendorSignupView,
    ReceptionSignupView,
    OfficeSignupView,
    CustomAuthToken,
    # OfficeOnlyView,
    ReceptionOnlyView,
    VendorOnlyView,
    Logout,
)

urlpatterns = [
    path('vendor-signup/', csrf_exempt(VendorSignupView.as_view()), name="vendor_signup"),
    path('reception-signup/', ReceptionSignupView.as_view(), name="reception_signup"),
    path('office-signup/', OfficeSignupView.as_view(), name="office_signup"),
    path('login/', csrf_exempt(CustomAuthToken.as_view()), name="auth-token"),
    path('logout/', Logout.as_view(), name="auth-token"),

    path('reception/', ReceptionOnlyView.as_view(), name="reception"),
    path('vendor/', VendorOnlyView.as_view(), name="vendor"),
    # path('office/', OfficeOnlyView.as_view(), name="office"),
]
