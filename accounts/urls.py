from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from jobsapp.views import EditProfileView
from .views import RegisterPatientView, RegisterDoctorView, LogoutView, LoginView

app_name = "accounts"

urlpatterns = [
    path('patient/register', RegisterPatientView.as_view(), name='patient-register'),
    path('doctor/register', RegisterDoctorView.as_view(), name='doctor-register'),
    path('patient/profile/update', EditProfileView.as_view(), name='patient-profile-update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
