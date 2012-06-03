import datetime
import json

from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings


from philly.models import School

from functools import wraps

def api_call(content_type="application/json"):
    """ Wrap an API call that returns an object that
        is convertable from json
    """
    def decorate(req_function):
        @wraps(req_function)
        def newreq(request, *args, **kwargs):
            outp = req_function(request, *args, **kwargs)
            if issubclass(outp.__class__, HttpResponse):
                response = outp
            else:
                response = HttpResponse()
                response.write('%s' % json.dumps(outp))
                response['Content-length'] = str(len(response.content))
                response['Content-Type'] = content_type


            return response
            
        return newreq
    return decorate

def school2dict(s):
    return { "id" : s.pk,
             "name" : s.name,
             "locationnumber": s.locationnumber,
             "grading_style_c": s.grading_style_c,
             "grading_style_c_num": s.grading_style_c_num,
             "grading_style_c_time": s.grading_style_c_time,
             "pssa_reading": s.pssa_reading,
             "pssa_math": s.pssa_math,
             "national_norm": s.national_norm,
             "allowed_absences": s.allowed_absences,
             "allowed_tardy": s.allowed_tardy, 
             "attendance_time": s.attendance_time, 
             "behavior_time": s.behavior_time,
             "essay": s.essay,
             "essay_topic": s.essay_topic,
             "invite_only": s.invite_only,
             "other": s.other,
             "mission": s.mission,
             "pride": s.pride,
             "highlights": s.highlights,
             "partnerships": s.partnerships,
             "extracurriculars": s.extracurriculars,
             "sports": s.sports,
             "grades": s.grade_descr(),
             "grad_rate": s.grad_rate}

@api_call()
def list_schools(request):
    n = School.objects.filter(school_type=0).order_by('name')
    c = School.objects.filter(school_type=1).order_by('name')
    s = School.objects.filter(school_type=2).order_by('name')

    return {"neighborhood": [school2dict(z) for z in n],
            "citywide": [school2dict(z) for z in c],
            "selective": [school2dict(z) for z in s] }

def str2bool(s):
    return s == "true"

@api_call()
def school_detail(request,school_id):
    school = School.objects.get(pk=school_id)
    
    return school2dict(school)
    

@api_call()
def search_schools(request):
    req = request.REQUEST
    
    missing = req["absences"]    # Max
    late = req["tardies"]        # Max
    behavior = req["discipline"] # 0=> None, 1 => Recent, 2 => 'Past'
    
    pssa_math = req["pssa_math"] # 2=> Advanced 1=> Proficient, 3=> Near Proficient, 4=> Not Proficient, -1=> None
    pssa_reading = req["pssa_reading"] # 2=> Advanced 1=> Proficient, 3=> Near Proficient, 4=> Not Proficient, -1=> None

    national_rank = int(req["national_rank"]) #0=> Ignore, otherwise percentile

    grades = req["grades"] #0=> As & Bs,  1=> 1 c in minor subj, 2=> 1 c in major subj, 3=> 2+ c's, 4=> Failed

    schools = School.objects.all()

    schools = schools.filter(allowed_absences__gte=missing)
    schools = schools.filter(allowed_tardy__gte=late)

    if behavior == "1": # Got a recent dicipline, only neighborhood schools
        schools = schools.filter(school_type=0) # Only neighborhood schools
    elif behavior == "2":
        schools = schools.filter(Q(behavior_time=0) | Q(behavior_time=-1))

    if pssa_math == "1":
        schools = schools.filter(Q(pssa_math=1)|Q(pssa_math=0)|Q(pssa_math=3))
    elif pssa_math == "3":
        schools = schools.filter(Q(pssa_math=0)|Q(pssa_math=3))
    elif pssa_math == "4":
        schools = schools.filter(school_type=0) # Only neighborhood schools

    if pssa_reading == "1":
        schools = schools.filter(Q(pssa_reading=1)|Q(pssa_reading=0)|Q(pssa_reading=3))
    elif pssa_reading == "3":
        schools = schools.filter(Q(pssa_reading=0)|Q(pssa_reading=3))
    elif pssa_reading == "4":
        schools = schools.filter(school_type=0) # Only neighborhood schools

    if national_rank > 0:
        schools = schools.filter(Q(national_norm__lte=national_rank)|Q(national_norm=0))

    if grades == "0":
        #TODO: But we do need to filter on time
        pass # If As & Bs then we don't have to filter on anything
    elif grades == "1":
        # Filter where (# of c's allowed is >= 1 and minor is allowed) OR
        #              (# of c's allowed is >= 0 and major is allowed)
        schools = schools.filter(Q(grading_style_c=0) |
                                 Q(grading_style_c_num__gte=1,grading_style_c=1) | 
                                 Q(grading_style_c_num__gte=0,grading_style_c=2))
    elif grades == "2":
        # Filter where number of c's allowed is greater than or equal to 1 and C's are allowed in major
        # subjects OR Cs allowed
        schools = schools.filter(Q(grading_style_c=0) | 
                                 Q(grading_style_c_num__gte=1,grading_style_c=2))
    elif grades == "3": # 2+c's, so, 
        # TODO: We are ignoring time in this
        # TODO: We should probably split this into major/minor
        schools = schools.filter(Q(grading_style_c=0) |
                                 Q(grading_style_c_num__gte=2))
    elif grades == "4":
        schools = schools.filter(school_type=0) # Only neighborhood schools

    # Explicitly exclude neighborhood schools (this will interact with above 
    # to filter to zero if we picked neighborhood only)

    n = School.objects.filter(school_type=0).order_by('name')
    c = schools.filter(school_type=1).order_by('name')
    s = schools.filter(school_type=2).order_by('name')


    return {"neighborhood": [school2dict(z) for z in n],
            "citywide": [school2dict(z) for z in c],
            "selective": [school2dict(z) for z in s] }

def search_js(request):
    return js('search.js',request)

def school_js(request):
    return js('school.js',request)


def js(file_name,request):
    return render_to_response(file_name,
                              {"API_URL": settings.API_URL, "title": "Search"},
                              context_instance=RequestContext(request),
                              mimetype="application/javascript")

def school_info(request, school_id):
    school = School.objects.get(pk=school_id)

    return render_to_response('school.html',
                              {"API_URL": settings.API_URL,
                               "school": school },
                              context_instance=RequestContext(request))

def index(request):
    return render_to_response('search.html',
                          {"API_URL": settings.API_URL, "title": "Search"},
                          context_instance=RequestContext(request))

def getSchoolsByType(t):
    return School.objects.filter(school_type=t).order_by('name')

def schools(request):
    n = getSchoolsByType(0)
    c = getSchoolsByType(1)
    s = getSchoolsByType(2)

    return render_to_response('schools.html',
                            { "title": "Schools",
                              "neighborhood": n,
                              "citywide": c,
                              "selective": s},
                            context_instance=RequestContext(request))
