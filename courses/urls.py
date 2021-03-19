from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('mine/',
         views.ManageCourseListView.as_view(),
         name='manage_course_list'),

    path('create/',
         views.CourseCreateView.as_view(),
         name='course_create'),

    path('<pk>/edit/',
         views.CourseUpdateView.as_view(),
         name='course_edit'),
    path('<pk>/delete/',
         views.CourseDeleteView.as_view(),
         name='course_delete'),
]
