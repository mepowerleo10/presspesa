from django.urls import path
from management.api.views import (
    CompanyDetails,
    CompanyList,
    CampaignList,
    CampaignDetails,
)

urlpatterns = [
    # Company endpoints
    path(
        "company/", CompanyList.as_view(), name="company_list"
    ),  # Endpoint for listing all company or create a new one
    path(
        "company/<int:pk>/", CompanyDetails.as_view(), name="company_details"
    ),  # Endpoint for retrieving, update or delete a company instance
    path(
        "campaign/", CampaignList.as_view(), name="campaigns"
    ),  # Endpoint for listing all tokens
    path(
        "campaign/<int:pk>/", CampaignDetails.as_view(), name="campaign_details"
    ),  # Endpoint for retrieving , update or delete a token instance
]
