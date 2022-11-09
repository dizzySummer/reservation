
## Reservation



This app-Reservation offers workforce leasing company a convienent tool to provide short-time work opportunities (Gag work) in healthcare sectors. There is no signup function available, only allowed users are able to use the app.  At the moment there are four user groups:

A. Employer

An employer could publish, update shifts via user interface. An employer can also delete a shift if it's not been reserved (by nurses, agency staff, admin) yet. Otherwise only job agency staff can delete it. 

With the pre-approval of the employee, an employer can assign certain shift to that employee. (Reserve a shift). 

An employer could view all its own shifts (open,reserved,unpublished, unfilled, done). The employer could not view other employers published shifts. 


B. Nurse 

There are three types of nurses: registered nurse (RN), pratical nurse (PN) and assistant (ASST). RN has the right to access and reserve all avaible shifts (RN, PN and ASST). Practical nurse could only view shifts that opens to PN and ASST. Then an assistant is restricted to work on ASST shifts. A nurse could view and reserve all **OPEN** shifts offered by all employers. 

Employer and Nurse are treated as customers.  A customer user can update own profile and reset password. 

C. Agency staff

An agency staff could access all open shifts offered by different employers. Agency staff can assign a shift to a nurse under mutual agreement. Agency staff can publish, update and delete shifts. 

D. Admin (Superuser)

An admin has all rights mentioned above. Admin also creates, updates and deletes users. Admin issues initial password to a user. 


### Build on top of 

1. [django framework](https://www.djangoproject.com/)
2. [bootstrap](https://getbootstrap.com/)
3. [crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
4. [bootstrap_datepicker_plus](https://aerabi.medium.com/](https://pypi.org/project/django-bootstrap-datepicker-plus/))



## Quick start (rewrite)

$ mkdir reservation
$ cd reservation
$ python3 -m venv myvenv
$ source myvenv/bin/activate

##install django before that make sure pip is update

~$ python3 -m pip install --upgrade pip

(myvenv) ~$ pip3 install -r requirements.txt

~$ git init

~$ django-admin startproject reservation .

~$ pip3 install python-decouple

~$ pip3 install python_extensions

~$ python3 manage.py runserver

~$ python3 manage.py migrate

~$ pip3 freeze > requirements.txt

~$ python manage.py startapp core

~$ deactivate

# restart 

$ source myvenv/bin/activate

//how store django secret keys in development and production
//or how to setup a django 4.0 proejct with Heroku and AWS S3



python3 manage.py runserver --settings=reservation.settings.prod

python3 manage.py runserver --settings=reservation.settings.dev


>python3 manage.py shell

>>> from django.contrib.auth import get_user_model
>>> User=get_user_model()
>>> User.objects.all()
<QuerySet [<CustomUser: admin@gmail.com>, <CustomUser: nurse1@gmail.com>, <CustomUser: hospital1@gmail.com>]>
>>> 

##### for allowing password reset email notifications, add authentication_backend part in settings. 
### add also auth_authentication.py in app 
### add email settings in base.py


--revert migartions


	#delete anywanted migrations
	then run command
    showmigrations to see where I am
    migrate 0003 (to go one step back)
    showmigrations to verify that it worked and I am one version behind
    migrate 0004 to migrate correctly



---shifts view

1) if user is employer, employer could view,edit, remove his/her own shifts both published and unpublished. This employer could not view the other employers offered shifts

2) if user is a nurse but not RN, then no RN shifts is visible. All employers published job vacancies could be reserved based on role permissions. RN, PN or Assistant

3) Admin and Staff could access all published shifts, update and remove shifts


#insert to base.html under line 6 when has favicon


    <!-- Link to page favicon.ico to display in location Bar-->
    <!-- <link rel="icon" href="{% static 'images/favicon.png' %}"> -->

https://stackoverflow.com/questions/73564800/django-query-to-filter-date-range

query from core.models.blabala
>> from core.models import Shift
>>> Shift.objects.all()



#render html based on user role 


example https://stackoverflow.com/questions/54158999/django-show-different-content-based-on-user
 from django.shortcuts import render

def my_view(request):
    #you can check user here with request.user
    #example
    if request.user.is_superuser:
        return render('your_template_for_admin.html', {})
    return render('your_template_for_basic_user.html', {})


shifts html


            <li>organization name: {{shift.employer}}</li>
          
            <li>shift id is: {{shift.id}}</li>
            <li> shift_employer_id:{{shift.employer_id}}</li>
            <li> employer phone:{{shift.employer.phone}}</li>
            <li> employer email:{{shift.employer.email}}</li>
            <li>shift status: {{shift.status}}</li>
            <li>shift date: {{shift.shift_date}}</li>
            <li>shift role: {{shift.role}}</li>
            <li>shift start time: {{shift.start_time}}</li>
            <li>shift finish time:{{shift.finish_time}}</li>
            <li>shift details: {{shift.details}}</li>
            <li>organiztion address: {{shift.address}}</li>



 {% for role in shift.role.all%}
              <option value="{{ role }}">{{ role }}</option>
              {{ person.get_gender_display }}
              {% endfor %}


view 

def index(request):
    latest_person_list2 = Person.objects.filter(to_be_listed=True)
    return object_list(request, template_name='polls/schol.html',
                       queryset=latest_person_list, paginate_by=5)

 paginate_by=5
