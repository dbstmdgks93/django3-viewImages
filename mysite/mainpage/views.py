from django.shortcuts import render
import os
# Create your views here.

def main(request):
    # "./" is mysite folder
    viewDir = "./static/stitch/"
    
    # make file list
    dirList = os.listdir(viewDir)
    dirList2 = []
    for dir in dirList:
        dirList2.append(viewDir+dir)

    return render(request, 'mainpage/main.html', {'dirList':dirList2})

def viewInsideImages(request):
    # "./" is mysite folder
    viewDir = "./static/infolder/"
    viewUrl = "/static/infolder/"
    
    # make file list
    dirList = os.listdir(viewDir)
    dirList2 = []
    for dir in dirList:
        dirList2.append(viewUrl+dir)

    return render(request, 'mainpage/viewInsideImages.html', {'dirList':dirList2})

def viewOutsideImages(request):
    # "./" is mysite folder
    viewDir = "../media/outfolder/"
    viewUrl = "/static/outfolder/"
    
    # make file list
    dirList = os.listdir(viewDir)
    dirList2 = []
    for dir in dirList:
        dirList2.append(viewUrl+dir)

    return render(request, 'mainpage/viewOutsideImages.html', {'dirList':dirList2})
