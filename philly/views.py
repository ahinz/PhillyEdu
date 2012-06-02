import datetime
import json

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.template import RequestContext
from django.shortcuts import render_to_response


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
             "sports": s.sports }

@api_call()
def list_schools(request):
    n = School.objects.filter(school_type=0).order_by('name')
    c = School.objects.filter(school_type=1).order_by('name')
    s = School.objects.filter(school_type=2).order_by('name')

    return {"neighborhood": [school2dict(z) for z in n],
            "citywide": [school2dict(z) for z in c],
            "selective": [school2dict(z) for z in s] }

def index(request):
    return render_to_response('search.html',
                          {},
                          context_instance=RequestContext(request))
