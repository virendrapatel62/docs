from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Course
from .serializers import CourseSerializer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(
            courses, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = request.POST.copy()
        author = get_object_or_404(User, pk=request.user.pk)
        data['author'] = author.id
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class CourseDetailView(View):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        data = request.POST.copy()
        author = get_object_or_404(User, pk=request.user.pk)
        data['author'] = author.id
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        course = get_object_or_404(course, pk=pk)
        course.delete()
        return HttpResponse(status=204)
