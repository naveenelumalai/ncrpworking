from django.shortcuts import render
from managedata.models import CrimeReport

# Create your views here.

def index(request):
    ncrp_details_list = CrimeReport.objects.order_by('acknowledgement_no')
    ncrp_details = {'access_records':ncrp_details_list}
    return render(request,'index.html',context=ncrp_details)
    