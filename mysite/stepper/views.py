from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)


def blinker(request):
    if 'on' in request.POST:
        GPIO.output(12,1)
    elif 'off' in request.POST:
        GPIO.output(12,0)
    return render(request,'control_page.html')
    
# Create your views here.
