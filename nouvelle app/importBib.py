from wageApp import Employee as emp, Salarie as sal
import matplotlib as plt
from datetime import date, datetime, timedelta as td
import time
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
