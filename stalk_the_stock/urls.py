from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("stockdata/", views.stockdata, name="stockdata"),
    path("stockdata/<str:ticker>/", views.graphs, name="graphs"),
    path("stockdata/<str:ticker>/analysis1", views.analysis1, name="analysis1"),
    path("stockdata/analysis2/<str:sec>", views.analysis2, name="analysis2"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
