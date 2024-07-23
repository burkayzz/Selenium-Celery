# -*- coding: utf-8 -*-
from celery import shared_task
from django.http import HttpResponse
from .funcs import sel,trends
from finder.celery_conf import app
import time
from selenium import webdriver
from .models import Keyword, SearchResult,Agenda
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from .mailing import send_email


@shared_task
def sell():
    sel()


@shared_task
def trends_task():
    print("X Görevi Çalıştı")
    trends()
    
    subject = "X - TOP TWEETS"
    to_email = "" # Alıcı mail hesabını giriniz..
    
    mailing_task.apply_async(args=[subject, to_email], queue = 'high_priority',countdown=10)

@shared_task
def mailing_task(subject,  to_email):
    print("Mail Görevi Çalıştı")
    
    today = datetime.now().date()   
    trends = Agenda.objects.filter(checkedDate__date = today)
    
    body = "GUNDEMI YAKINDAN TAKIP ET   Iste gunun gundemleri"
    
    for a in trends:
        body += f"{a.title}\n"
    
    body += ("En yeni haberleri en yakindan takip etmeye devam et...")
    
    
    send_email(subject=subject, body=body, to_email=to_email)
    
    
