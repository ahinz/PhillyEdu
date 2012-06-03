from django.db import models

class School(models.Model):
    # Base Info
    name = models.CharField(max_length=255)
    locationnumber = models.CharField(max_length=20)

    school_type = models.IntegerField(default=0, choices=((0, "Neighborhood"),(1, "Citywide Admission"),(2, "Selective Admission"),(3, "Promise"),(4,"Charter")))

    # Admission requirements
    grading_style_c = models.IntegerField(default=0, choices=((0, "Allowed"),(1, "Minor Subject"),(2, "Any Subject")))
    grading_style_c_num = models.IntegerField(default=0)
    grading_style_c_time = models.IntegerField(default=0, choices=((1, "All Years"),(0, "Most Recent"),(-1,"Unspecified")))

    def grade_descr(self):
        if self.grading_style_c == 0:
            return "Marks of A, B, or C"
        else:
            if self.grading_style_c == 1:
                major = "minor subject"
            else:
                major = "major subject"

            time = ""
            if  self.grading_style_c_time == 1:
                time = "in all classes"
            elif self.grading_style_c_time == 0:
                time = "on the most recent report card"

            if (self.grading_style_c_num == 0):
                return "Only A's and B's"
            else:
                return "At most %s C allowed in a %s %s" % (self.grading_style_c_num,major,time)

    pssa_reading = models.IntegerField(default=0, choices=((2, "Advanced"), (1,"Proficient"), (0, "Not Required"), (3, "Near Proficient")))
    pssa_math = models.IntegerField(default=0, choices=((2, "Advanced"), (1,"Proficient"), (0, "Not Required"), (3, "Near Proficient")))
    national_norm = models.IntegerField(default=0) # percentile

    allowed_absences = models.IntegerField(default=10)
    allowed_tardy = models.IntegerField(default=5)
    attendance_time = models.IntegerField(default=0, choices=((1, "All Years"),(0, "Most Recent"),(-1,"Unspecified")))

    behavior_time = models.IntegerField(default=0, choices=((1, "All Years"),(0, "Most Recent"),(-1,"Unspecified")))

    essay = models.BooleanField(default=False)
    essay_topic = models.CharField(max_length=255,default="",blank=True,null=True)
        
    # Note that these fields combine to form the grading criteria. For instance:
    # grading_style_c = Minor Subject
    # grading_style_c_num = 1
    # grading_style_c_time = Most Recent
    # Would be read as:
    # At most 1 C in a minor subject on the last report card

    invite_only = models.BooleanField(default=False)
    other = models.TextField(default="",blank=True,null=True)
    
    # Base Info
    mission = models.TextField(default="")
    pride = models.TextField(default="")
    highlights = models.TextField(default="")
    partnerships = models.TextField(default="")
    extracurriculars = models.TextField(default="")
    sports = models.TextField(default="")

    grad_rate = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s (%s / %s)' % (self.name, self.locationnumber, self.get_school_type_display().split(" ")[0])

class SchoolAddress(models.Model):

    name = models.CharField(max_length=255)
    locationnumber = models.CharField(max_length=20)

    address_street  = models.CharField(max_length=255)
    address_zip  = models.CharField(max_length=255)

    phone = models.CharField(max_length=200)
    image = models.TextField()
    
