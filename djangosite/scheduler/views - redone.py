# Create your views here.
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

from scheduler.models import Student, Course, Teacher, CourseRegister

def index( request ):
	"""
	Renders the view for the index page
	"""
	
    template = loader.get_template( 'scheduler/index.html' )
    context = Context()
	
    return HttpResponse( template.render( context ) )

	
def student( request ):
	"""
	Renders the view to the initial student page
	"""
	
    student_list = Student.objects.all()
    template = loader.get_template( 'scheduler/students.html' )
    context = Context( { 'student_list' : student_list } )
		
    return HttpResponse( template.render( context ) )

	
def student_detail( request, student_id ):
    student = get_object_or_404( Student, pk=student_id )
    registered_list = CourseRegister.objects.filter( student_id = student_id )
    registered_courses = []
    
	for entry in registered_list:
        registered_courses.append( Course.objects.get( pk = entry.course_id.id ) )
    
	return render_to_response( 'scheduler/students_detail.html', 
							   { 'student' : student, 'registered_courses' : registered_courses },
                               context_instance = RequestContext( request ) )


def teacher( request ):
    teacher_list = Teacher.objects.all()
    template = loader.get_template( 'scheduler/teachers.html' )
    context = Context( { 'teacher_list' : teacher_list } )
	
    return HttpResponse( template.render( context ) )

	
def teacher_detail( request, teacher_id ):
    teacher = get_object_or_404( Teacher, pk = teacher_id )
    courses_taught = Course.objects.filter( teacher_id = teacher_id )
	
    return render_to_response( 'scheduler/teachers_detail.html', 
							   { 'teacher' : teacher, 'courses_taught' : courses_taught },
                               context_instance = RequestContext( request ) )


def course( request ):
    course_list = Course.objects.all()
    template = loader.get_template( 'scheduler/courses.html' )
    context = Context( { 'course_list' : course_list } )
    
	return HttpResponse( template.render( context ) )

	
def course_detail( request, course_id ):
    course = get_object_or_404( Course, pk = course_id )
    teacher = get_object_or_404( Teacher, pk = course.teacher_id.id )
    
	register_count = len( CourseRegister.objects.filter( course_id = course_id ) )
    
	return render_to_response( 'scheduler/courses_detail.html', 
	                           {'course' : course, 'teacher' : teacher, 'register_count' : register_count},
                               context_instance = RequestContext( request ) )
    
