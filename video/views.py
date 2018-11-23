
from django.http import HttpResponse
from django.http import QueryDict
import subprocess as sp


def index(request):
    print (request.GET.get("video", ''))
    sp.run(["python",
            "/Users/adrien/Documents/Projet/pytorch-yolo-v3/video_demo.py",
            '--video {}'.format(request.GET.get("video", ''))
            ])
    return HttpResponse("Hello, world. You're at the polls index.")


def videoUrl(request, videoUrl):
    # start over ssh
    sp.run(["python", "/Users/adrien/Documents/Projet/pytorch-yolo-v3/video_demo.py", "--video %s".format(videoUrl)])
    return HttpResponse("hello there!")

def videoStop(request):
    # stop over ssh
    return HttpResponse("video stopped")
