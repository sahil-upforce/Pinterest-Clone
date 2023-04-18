from django.urls import path

from pinterest.views import (
    PinCreateView, PinDetailView, SaveUnsavePin, SearchPinByCategoryListView, PinAddToBoard
)

app_name = 'pins'
urlpatterns = [
    path('pin/create/<str:input_value>', PinCreateView.as_view(), name='create_pin'),
    path('pin/details/<int:id>', PinDetailView.as_view(), name='detail_pin'),

    path('pin/save-unsave-pin/<int:pin_id>', SaveUnsavePin.as_view(), name='save_unsave_pin'),

    path('pin/search-category', SearchPinByCategoryListView.as_view(), name='search_pin_by_category'),

    path('pin/<int:board_id>/<int:pin_id>', PinAddToBoard.as_view(), name='pin_add_to_board')
]
