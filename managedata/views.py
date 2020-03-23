from django.shortcuts import render
from managedata.models import CrimeReport
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.db.models import Q

# Create your views here.

def index(request):
    ncrp_details_list = CrimeReport.objects.order_by('acknowledgement_no')
    ncrp_details = {'access_records':ncrp_details_list}
    return render(request,'index.html',context=ncrp_details)
    

from django.views import generic


class ComplaintsListView(generic.ListView):
    """Generic class-based view for a list of Complaints."""
    model = CrimeReport
    paginate_by = 10


class ComplaintsDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = CrimeReport

class ComplaintCreate(CreateView):
    model = CrimeReport
    fields = '__all__'

class ComplaintUpdate(UpdateView):
    model = CrimeReport
    fields = '__all__'

class SearchResultsView(generic.ListView):
    model = CrimeReport

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = CrimeReport.objects.filter(
            Q(acknowledgement_no=query) | Q (suspect_name=query)
        )
        return object_list
