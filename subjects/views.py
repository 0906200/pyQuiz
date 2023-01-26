from django.shortcuts import render, redirect
from . import models
from django.db import connection
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import get_plot


def signup(resquest):
    if resquest.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if resquest.method == 'POST':
            form = CreateUserForm(resquest.POST)
            if form.is_valid():
                form.save()
                t = models.User.objects.get(username=resquest.POST["username"])
                t.resultmaths_set.create(user=resquest.POST["username"])
                t.save()
                t.resultphysics_set.create(user=resquest.POST["username"])
                t.save()
                t.resultchemistry_set.create(user=resquest.POST["username"])
                t.save()

                return redirect('home')

        context = {'form': form}
        return render(resquest, 'acct/signup.html', context)


def login_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or password is incorrect")

        return render(request, 'acct/login.html', {})


def log_out(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(response):
    return render(response, 'home.html', {})


@login_required(login_url='login')
def chemistry_hard(response, id):
    t = models.Chemistry.objects.get(id=id)
    chem = t.chemistryhard_set
    l = response.user
    l = l.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in chem.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultchemistry SET chemistry_hard = %s WHERE user_id = %s ", [x, l])
                cursor.fetchone()
            return redirect('chemistry_hard_result')
    return render(response, 'subjects/chemistry/chemistry_hard.html', {'chem': chem})


@login_required(login_url='login')
def chemistry_medium(response, id):
    t = models.Chemistry.objects.get(id=id)
    chem = t.chemistrymedium_set
    l = response.user
    l = l.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in chem.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultchemistry SET chemistry_medium = %s WHERE user_id = %s ", [x, l])
                cursor.fetchone()
            return redirect('chemistry_medium_result')
    return render(response, 'subjects/chemistry/chemistry_medium.html', {'chem': chem})


@login_required(login_url='login')
def chemistry_easy(response, id):
    t = models.Chemistry.objects.get(id=id)
    chem = t.chemistryeasy_set
    l = response.user
    l = l.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in chem.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultchemistry SET chemistry_easy = %s WHERE user_id = %s ", [x, l])
                cursor.fetchone()
            return redirect('chemistry_easy_result')
            print(x)
    return render(response, 'subjects/chemistry/chemistry_easy.html', {'chem': chem})


@login_required(login_url='login')
def mathematics_hard(response, id):
    t = models.Maths.objects.get(id=id)
    maths = t.mathshard_set
    l = response.user
    l = l.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in maths.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultmaths SET maths_hard = %s WHERE user_id = %s ", [x, l])
                cursor.fetchone()
            return redirect('maths_hard_result')
            print(x)
    return render(response, 'subjects/maths/level/maths_hard.html', {'maths': maths})


@login_required(login_url='login')
def mathematics_medium(response, id):
    t = models.Maths.objects.get(id=id)
    maths = t.mathsmedium_set
    l = response.user
    l = l.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in maths.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultmaths SET maths_medium = %s WHERE user_id = %s ", [x, l])
                cursor.fetchone()
            return redirect('maths_medium_result')
            print(x)
    return render(response, 'subjects/maths/level/maths_medium.html', {'maths': maths})


@login_required(login_url='login')
def mathematics_easy(response, id):
    t = models.Maths.objects.get(id=id)
    maths = t.mathseasy_set
    l = response.user
    l = l.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in maths.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultmaths SET maths_easy = %s WHERE user_id = %s ", [x, l])
                cursor.fetchone()
            return redirect('maths_easy_result')
            print(x)
    return render(response, 'subjects/maths/level/maths_easy.html', {'maths': maths})


@login_required(login_url='login')
def physics_hard(response, id):
    t = models.Physics.objects.get(id=id)
    physics = t.physicshard_set
    r = response.user
    p = r.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in physics.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultphysics SET physics_hard = %s WHERE user_id = %s ", [x, p])
                cursor.fetchone()
            return redirect('physics_hard_result')
            print(x)
    return render(response, 'subjects/physics/level/physics_hard.html', {'physics': physics})


@login_required(login_url='login')
def physics_medium(response, id):
    t = models.Physics.objects.get(id=id)
    physics = t.physicsmedium_set
    k = response.user
    p = k.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in physics.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultphysics SET physics_medium = %s WHERE user_id = %s ", [x, p])
                cursor.fetchone()
            return redirect('physics_medium_result')
            print(x)
    return render(response, 'subjects/physics/level/physics_medium.html', {'physics': physics})


@login_required(login_url='login')
def physics_easy(response,id):
    t = models.Physics.objects.get(id=id)
    physics = t.physicseasy_set
    k = response.user
    p = k.id
    x = 0
    if response.method == 'POST':
        if response.POST.get("submit"):
            for i in physics.all():
                if response.POST.get("fav_language" + str(i.id)) == 'Q':
                    x += 1

                else:
                    x -= 0
            with connection.cursor() as cursor:
                cursor.execute("UPDATE subjects_resultphysics SET physics_easy = %s WHERE user_id = %s ", [x, p])
                cursor.fetchone()
            return redirect('physics_easy_result')
    return render(response, 'subjects/physics/level/physics_easy.html', {'physics': physics})


@login_required(login_url='login')
def chemistry_chapters(response):
    t = models.Chemistry.objects.all()
    context = {'chem':t}
    return render(response, 'subjects/chemistry/chemistry.html',context)


@login_required(login_url='login')
def chemistry_level(response,id):
    t = id
    context = {'ch':t}
    return render(response, 'subjects/chemistry/chemistry_level.html',context)


@login_required(login_url='login')
def maths_chapters(response):
    t = models.Maths.objects.all()
    context = {'maths':t}
    return render(response, 'subjects/maths/mathematics.html',context)


@login_required(login_url='login')
def maths_level(response,id):
    t = id
    context = {'ch':t}
    return render(response, 'subjects/maths/maths_level.html',context)


@login_required(login_url='login')
def physics_chapters(response):
    t = models.Physics.objects.all()
    context = {'physics':t}
    return render(response, 'subjects/physics/physics.html',context)


@login_required(login_url='login')
def physics_level(response,id):
    t = id
    context = {'ch':t}
    return render(response, 'subjects/physics/physics_level.html',context)


@login_required(login_url='login')
def chemistry_easy_result(response):
    l = response.user
    mark = models.ResultChemistry.objects
    number = mark.filter(user=l).values_list('chemistry_easy', flat=True)[0]
    return render(response, 'subjects/chemistry/chemistryeasyresult.html', {'result': number})


@login_required(login_url='login')
def chemistry_medium_result(response):
    l = response.user
    mark = models.ResultChemistry.objects
    number = mark.filter(user=l).values_list('chemistry_medium', flat=True)[0]
    return render(response, 'subjects/chemistry/chemistrymediumresult.html', {'result': number})


@login_required(login_url='login')
def chemistry_hard_result(response):
    l = response.user
    mark = models.ResultChemistry.objects
    number = mark.filter(user=l).values_list('chemistry_hard', flat=True)[0]
    return render(response, 'subjects/chemistry/chemistryhardresult.html', {'result': number})


@login_required(login_url='login')
def maths_hard_result(response):
    l = response.user
    mark = models.ResultMaths.objects
    number = mark.filter(user=l).values_list('maths_hard', flat=True)[0]
    return render(response, 'subjects/maths/level/mathshardresult.html', {'result': number})


@login_required(login_url='login')
def maths_easy_result(response):
    l = response.user
    mark = models.ResultMaths.objects
    number = mark.filter(user=l).values_list('maths_easy', flat=True)[0]
    return render(response, 'subjects/maths/level/mathseasyresult.html', {'result': number})


@login_required(login_url='login')
def maths_medium_result(response):
    l = response.user
    mark = models.ResultMaths.objects
    number = mark.filter(user=l).values_list('maths_medium', flat=True)[0]
    return render(response, 'subjects/maths/level/mathsmediumresult.html', {'result': number})


@login_required(login_url='login')
def physics_medium_result(response):
    l = response.user
    mark = models.ResultPhysics.objects
    number = mark.filter(user=l).values_list('physics_medium', flat=True)[0]
    return render(response, 'subjects/physics/level/physicsmediumresult.html', {'result': number})


@login_required(login_url='login')
def physics_hard_result(response):
    l = response.user
    mark = models.ResultPhysics.objects
    number = mark.filter(user=l).values_list('physics_hard', flat=True)[0]
    return render(response, 'subjects/physics/level/physicshardresult.html', {'result': number})


@login_required(login_url='login')
def physics_easy_result(response):
    l = response.user
    mark = models.ResultPhysics.objects
    number = mark.filter(user=l).values_list('physics_easy', flat=True)[0]
    return render(response, 'subjects/physics/level/physicseasyresult.html', {'result': number})


@login_required(login_url='login')
def progress(response):
    l = response.user
    mark1 = models.ResultPhysics.objects
    mark2 = models.ResultMaths.objects
    mark3 = models.ResultChemistry.objects
    number = mark3.filter(user=l).values_list('chemistry_easy', flat=True)[0]
    number1 = mark3.filter(user=l).values_list('chemistry_medium', flat=True)[0]
    number2 = mark3.filter(user=l).values_list('chemistry_hard', flat=True)[0]
    physics1 = mark1.filter(user=l).values_list('physics_easy', flat=True)[0]
    physics2 = mark1.filter(user=l).values_list('physics_medium', flat=True)[0]
    physics3 = mark1.filter(user=l).values_list('physics_hard', flat=True)[0]
    maths1 = mark2.filter(user=l).values_list('maths_easy', flat=True)[0]
    maths2 = mark2.filter(user=l).values_list('maths_medium', flat=True)[0]
    maths3 = mark2.filter(user=l).values_list('maths_hard', flat=True)[0]
    phy_chart = get_plot(physics1,physics2,physics3,'physics')
    chemistry_chart = get_plot(number, number1, number2, 'chemistry')
    maths_chart = get_plot(maths1, maths2, maths3, 'maths')
    return render(response,'progress/progress.html',{'physics':phy_chart ,'chemistry':chemistry_chart ,'maths': maths_chart})
