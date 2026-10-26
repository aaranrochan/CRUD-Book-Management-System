from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')

        Student.objects.create(
            name=name,
            email=email,
            department=department
        )

        return redirect('student_list')

    return render(request, 'students/student_form.html')


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.department = request.POST.get('department')
        student.save()

        return redirect('student_list')

    return render(request, 'students/student_form.html', {'student': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {'student': student})