from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import JobPosting

# Create your views here.
def index(request):
    jobs = JobPosting.objects.all()
    context = {
        'JobPostings': jobs
    }
    return render(request, 'job_board/index.html', context)

def jobdetail(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    #job = JobPosting.objects.get(pk=pk)
    context = {
        'job' : job
    }
    return render(request, 'job_board/detail.html', context)