from django.conf.urls import url
from bank_information.views import branch_search, bank_details

urlpatterns = [
    url(r'^branches/autocomplete$', branch_search, name='branch_autocomplete'),
    url(r'^branches$', bank_details, name='bank_information'),
]