from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, "singleapp/index.html")

text = ["sec1: Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae nihil quasi","sec2: impedit praesentium labore illum quibusdam quo aliquid. Eveniet quo quae mollitia ","sec3: corrupti, dolores architecto obcaecati deserunt eos odio. Impedit!"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(text[num-1])
    else:
        return Http404("Section not found!")