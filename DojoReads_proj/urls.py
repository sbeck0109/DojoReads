from django.urls import path, include

urlpatterns = [
    path('books', include('DojoReads_app.urls')),
    path('', include('loginReg_app.urls'))
]
