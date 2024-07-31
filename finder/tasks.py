# -*- coding: utf-8 -*-
from celery import shared_task
from django.http import HttpResponse
from .funcs import sel,trends,exchange,set_dark_theme,set_light_theme,amazons_deals
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
    
    mailing_task_for_x.apply_async(args=[subject, to_email], queue = 'high_priority',countdown=10)


@shared_task
def forex():

    everybody = "the mail to everybody" #Burada veritabanınızdaki veya sabit mail almasını beklediğiniz mailleri veriniz
    exchange_rates = exchange()
    date = datetime.now()
    body = "Güncel EUR/USD Kurları\n"
    
    for currency, rate in exchange_rates.items():
        body += f"{currency} = {rate} ₺\n"
    
    body += f"Tarih: {date.strftime('%Y-%m-%d %H:%M:%S')}"
    subject = "Güncel Kurlar"
    
    send_email(subject=subject, body=body, to_email=everybody)

@shared_task
def mailing_task_for_x(to_email):
    print("Mail Görevi Çalıştı")
    
    today = datetime.now().date()   
    trends = Agenda.objects.filter(checkedDate__date = today)
    subject = "TRENDS İN X"
    body = "GUNDEMI YAKINDAN TAKIP ET   Iste günün trendleri"
    
    for a in trends:
        body += f"{a.title}\n"
    
    body += ("En yeni haberleri en yakindan takip etmeye devam et...")
    
    
    send_email(subject=subject, body=body, to_email=to_email)
    
    
@shared_task
def light_theme():
    set_light_theme()
    
@shared_task
def dark_theme():
    print("Çalıştı")
    set_dark_theme()


@shared_task
def deals_for_amazon():
    print("firsatlar")
    products = amazons_deals()
    
    to_email = "Lütfen alıcı maili giriniz..."
    
    date = datetime.now
    
    
    subject = "AMAZONDA GÜNÜN FIRSATLARINI KAÇIRMA"
    body = "İşte günün fırsatlarından bazıları\n"
    
    for p in products:
        
        body += f"-{p} \n"
        
    body += "(Fırsat ürünlerdeki indirim saat 23.00'a kadar geçerlidir..)\nHemen Alışverişe Başla.."
    
    send_email(subject=subject, body=body, to_email=to_email)