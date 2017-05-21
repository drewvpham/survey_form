from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if "submit_num" not in request.session:
        request.session["submit_num"] = 0
    return render(request, 'survey_form/index.html')

def survey_process(request):
    request.session["submit_num"] += 1
    request.session['name']=request.POST['name']
    request.session['fave_lang']=request.POST['fave_lang']
    request.session['loc_select']=request.POST['loc_select']
    request.session['comments']=request.POST['comments']
    return redirect("/result")

def result(request):
    return render(request, "survey_form/result.html")
