from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all().order_by('roll_number')
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(name__icontains=search_query)
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def add_student(request):
    if not request.user.is_staff:
        return redirect('student_list')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

@login_required
def edit_student(request, pk):
    if not request.user.is_staff:
        return redirect('student_list')
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/edit_student.html', {'form': form, 'student': student})

@login_required
def delete_student(request, pk):
    if not request.user.is_staff:
        return redirect('student_list')
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')

def view_result(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})
