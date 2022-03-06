from django.urls import path
from .views import index, renderLoadFullUrl

urlpatterns = [
  path('', index, name='index'),
  path('<str:short_url>', renderLoadFullUrl, name='Load Full Url'),
]