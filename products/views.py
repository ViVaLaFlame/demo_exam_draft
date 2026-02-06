from django.shortcuts import render
from pathlib import Path
from demo1_django.settings import BASE_DIR
from django.http import HttpResponse

# Create your views here.
def login_page(request):
  html_file = Path(BASE_DIR) / "templates" / "login.html"
  content = html_file.read_text()
  return HttpResponse(content)
