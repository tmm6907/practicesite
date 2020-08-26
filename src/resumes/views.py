from django.shortcuts import render

from .models import User, Education, Work

from .forms import ResumeForm

# Create your views here.
def resume_create_view(request):
    form = ResumeForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ResumeForm()

    context = {
        'form': form,
    }
    return render(request, "resumes/resume_create.html", context)

def resume_detail_view(request):
    obj = [
        User.objects.get(id=1),
        Education.objects.get(id=1),
        Work.objects.get(id=1),
        ]


    context = {
        'object': obj,
    }
    return render(request, "resumes/resume_detail.html", context)
