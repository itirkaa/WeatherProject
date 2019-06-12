# -*- coding: utf-8 -*-

# Contains app urls which are later included to Project urls (Mocking_Weather/urls.py)

from django.urls import path

from .views import index,info_page, feedback, feedbacklist, add_message

urlpatterns = [
        path('', index, name='home'),
        path('info/', info_page, name='info'),
        path('all-feedbacks/', feedbacklist),
        path('add-message/', add_message, name='message'),
        path('feedback/', feedback, name='feedback'),
]