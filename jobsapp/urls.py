from django.urls import path, include

from .views import HomeView, SearchView, DashboardView, ApplicantsListView, ApplicantPerJobView, filled, ApplyJobView, JobListView, JobDetailsView, JobCreateView

app_name = "jobs"    

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='searh'),
    path('doctor/dashboard', include([
        path('', DashboardView.as_view(), name='doctor-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='doctor-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='doctor-dashboard-applicants'),
        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('doctor/jobs/create', JobCreateView.as_view(), name='doctor-jobs-create'),
]
