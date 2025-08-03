from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList

router = DefaultRouter()
router.register(r'books', BookList)

urlpatterns = [
    path('api/', include(router.urls)),
    path('books/', BookList.as_view({'get': 'list'}), name='book-list'),
    path('admin/', admin.site.urls),
    path('', include('api.urls')),  
]

