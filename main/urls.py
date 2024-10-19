from rest_framework.routers import SimpleRouter
from .views import ItemsPage, OrderAdd, ItemEdit
from django.urls import path


router = SimpleRouter()
router.register('api/items', ItemsPage)


urlpatterns = [
    path('api/order-add/', OrderAdd.as_view()),
    path('api/edit-item/<slug:slug>', ItemEdit.as_view())
]
urlpatterns += router.urls
