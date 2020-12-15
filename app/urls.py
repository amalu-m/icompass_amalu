from django.urls import path,include
from app.views import inputData

urlpatterns = [
    path('v1/sanitized/input', inputData),
]
