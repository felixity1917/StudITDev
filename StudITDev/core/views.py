from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ToDoItem
from .forms import ToDoItemForm

# Create your views here.
# def home(request):
    # return HttpResponse("Test...")
    # return render(request, "home.html")
# def todos(request):
    # items = TodoItem.objects.all()
    # return render(request, "todos.html", {"todos": items})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def todo_list(request):
    items = ToDoItem.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            print(f"Saved ToDoItem: {todo.id}")
            return redirect('todo_list')
    else:
        form = ToDoItemForm()
    return render(request, 'todo_list.html', {'items': items, 'form': form})

@login_required
def delete_todo(request, pk):
    # Get the todo item by its primary key (pk)
    todo = get_object_or_404(ToDoItem, pk=pk)

    # Ensure the current user is the one who created the todo item
    if todo.user == request.user:
        todo.delete()

    # Redirect back to the todo list page after deletion
    return redirect('todo_list')
