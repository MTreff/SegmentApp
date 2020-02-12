from django.shortcuts import render, redirect
from .forms import AddNewImage
from .models import NewImage
from django.conf import settings
from .scripts import semantic_segmentation, remove_background, grayscale_background, blur_background
import matplotlib.pyplot as plt
import cv2

def index(request):
    return render(request, 'segmentation/index.html', {'MEDIA_URL': settings.MEDIA_URL})


def add_image(request):
    if request.method == 'POST':
        form = AddNewImage(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return redirect('result')
    else:
        form = AddNewImage()
    return render(request, 'segmentation/semantic_segmentation.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL},)


def show_result(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        image = NewImage.objects.last()

        processed_image = grayscale_background(settings.BASE_DIR + image.image.url)

        path = '{}images/result/1.jpg'.format(settings.MEDIA_ROOT)
        url = '{}images/result/1.jpg'.format(settings.MEDIA_URL)
        plt.imsave(path, processed_image)
        return render(request, 'segmentation/result.html', {'image': image, 'url': url})

"""
def semseg_add_image(request):
    if request.method == 'POST':
        form = AddNewImage(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return redirect('semantic_segmentation_result')
    else:
        form = AddNewImage()
    return render(request, 'segmentation/semantic_segmentation.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL},)


def semgeg_show_result(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        image = NewImage.objects.last()

        processed_image = semantic_segmentation(settings.BASE_DIR + image.image.url)
        path = '{}images/result/1.jpg'.format(settings.MEDIA_ROOT)
        url = '{}images/result/1.jpg'.format(settings.MEDIA_URL)
        plt.imsave(path, processed_image)
        return render(request, 'segmentation/semantic_segmentation_result.html', {'image': image, 'url': url})
"""
def semseg_add_image(request):
    if request.method == 'POST':
        form = AddNewImage(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            image = NewImage.objects.last()
            processed_image = semantic_segmentation(settings.BASE_DIR + image.image.url)
            img_name = image.image.url[image.image.url.rfind('/',) + 1: image.image.url.rfind('.',)] + '_ss'
            path = '{}images/result/{}.jpg'.format(settings.MEDIA_ROOT, img_name)
            url = '{}images/result/{}.jpg'.format(settings.MEDIA_URL, img_name)
            plt.imsave(path, processed_image)
            return render(request, 'segmentation/semantic_segmentation_result.html', {'image': image, 'url': url})
    else:
        form = AddNewImage()
    return render(request, 'segmentation/semantic_segmentation.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL},)


def remback_add_image(request):
    if request.method == 'POST':
        form = AddNewImage(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            image = NewImage.objects.last()
            processed_image = remove_background(settings.BASE_DIR + image.image.url)
            img_name = image.image.url[image.image.url.rfind('/', ) + 1: image.image.url.rfind('.', )] + '_rb'
            path = '{}images/result/{}.jpg'.format(settings.MEDIA_ROOT, img_name)
            url = '{}images/result/{}.jpg'.format(settings.MEDIA_URL, img_name)
            plt.imsave(path, processed_image)
            return render(request, 'segmentation/remove_background_result.html', {'image': image, 'url': url})
    else:
        form = AddNewImage()
    return render(request, 'segmentation/remove_background.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL},)


def graysc_add_image(request):
    if request.method == 'POST':
        form = AddNewImage(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            image = NewImage.objects.last()

            processed_image = grayscale_background(settings.BASE_DIR + image.image.url)
            img_name = image.image.url[image.image.url.rfind('/', ) + 1: image.image.url.rfind('.', )] + '_gb'
            path = '{}images/result/{}.jpg'.format(settings.MEDIA_ROOT, img_name)
            url = '{}images/result/{}.jpg'.format(settings.MEDIA_URL, img_name)
            plt.imsave(path, processed_image)
            return render(request, 'segmentation/grayscale_background_result.html', {'image': image, 'url': url})

    else:
        form = AddNewImage()
    return render(request, 'segmentation/grayscale_background.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL},)


def blur_add_image(request):
    if request.method == 'POST':
        form = AddNewImage(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            image = NewImage.objects.last()
            processed_image = blur_background(settings.BASE_DIR + image.image.url)
            img_name = image.image.url[image.image.url.rfind('/', ) + 1: image.image.url.rfind('.', )] + '_bb'
            path = '{}images/result/{}.jpg'.format(settings.MEDIA_ROOT, img_name)
            url = '{}images/result/{}.jpg'.format(settings.MEDIA_URL, img_name)
            plt.imsave(path, processed_image)
            return render(request, 'segmentation/blur_background_result.html', {'image': image, 'url': url})
    else:
        form = AddNewImage()
    return render(request, 'segmentation/blur_background.html', {'form': form, 'MEDIA_URL': settings.MEDIA_URL},)

