#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:36:11 2019

@author: richasdy
@source: https://medium.com/@rahulvaish/speech-to-text-python-77b510f06de 
"""

import speech_recoginition as sr
r = sr.Recognizer()
with sr.Mirophone() as source:
    print("Say Something")
    audio = r.listen(source)
    print("Time over, Thanks")
try:
    print("Text: "+r.recognize_google(audio));
except:
    pass;