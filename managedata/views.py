from django.shortcuts import render
from managedata.models import CrimeReport

# Create your views here.

def index(request):
    ncrp_details_list = CrimeReport.objects.order_by('acknowledgement_no')
    ncrp_details = {'access_records':ncrp_details_list}
    return render(request,'index.html',context=ncrp_details)
    

from django.views import generic


class ComplaintsListView(generic.ListView):
    """Generic class-based view for a list of Complaints."""
    model = CrimeReport


class ComplaintsDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = CrimeReport