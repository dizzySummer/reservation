## Reservation

The app-Reservation offers a convenient tool for a workforce leasing company to provide short-time work opportunities (gig work) for healthcare professionals. Currently, only approved users can use the app, and there are four user groups:

A. Employer:

- An employer can use the user interface to publish and update shifts.
- An employer can delete a shift if it has not been reserved by nurses, agency staff, or admins. Otherwise, only agency staff can delete it.
- With an employee's pre-approval, an employer can assign a specific shift to that employee (reserve a shift). A reserved nurse cannot be reserved on the same day by another employer.
- An employer can view all of their own shifts (open, reserved, unpublished, unfilled, done), but cannot view other employers' published shifts.

B. Nurse:

- Nurses are divided into three categories: registered nurses (RNs), practical nurses (PNs), and assistants (ASSTs).
- RNs can access and reserve all available shifts (RN, PN, and ASST).
- PNs can only view shifts that are open to PNs and ASSTs.
- Assistants are restricted to working on ASST shifts only.
- A nurse can view and reserve his or her role permitted shifts offered by all employers.

Employers and nurses are treated as customers. As a customer, a user can update their own profile and reset their password.

C. Agency staff:

- Agency staff can access all open shifts offered by different employers.
- Agency staff can assign a shift to a nurse with mutual agreement.
- Agency staff can publish, update, and delete shifts.

D. Admin (Superuser):

- Admins have all the rights mentioned above.
- Admins can also create, update, and delete users.
- Admins issue initial passwords to users.


### Built on top of:

1. [django framework](https://www.djangoproject.com/)
2. [bootstrap](https://getbootstrap.com/)
3. [crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/)
4. [bootstrap_datepicker_plus](https://pypi.org/project/django-bootstrap-datepicker-plus/)


## Features

1. Admins, staff, and employers can import or export shifts using CSV, XLSX, JSON, YAML, Pandas, and HTML formats. The imported data can then be updated in the database.
2. The search and multiple filter options allow users to easily find what they're looking for without violating privacy by accessing other users' data or reserved shifts.
3. Admins/staff can view live shift data on the admin panel by checking the data or viewing visualized charts.
4. A charbot can make the user interface more user-friendly and accessible for accessing the service.-todo


## Quick start

For Mac users:

```
$ mkdir reservation
$ cd reservation
$ python3 -m venv myvenv
$ source myvenv/bin/activate
```

## install django before that make sure pip is update
```
~$ python3 -m pip install --upgrade pip
(myvenv) ~$ pip install Django
~$ git init
~$ django-admin startproject reservation .
~$ pip3 install python-decouple
~$ pip3 install python_extensions
~$ python3 manage.py runserver
~$ python3 manage.py migrate
~$ pip3 freeze > requirements.txt
~$ deactivate 
```
# restart 

```
$ source myvenv/bin/activate
````

## add data to database on admin panel

1. To add admin or staff users, click the "Custom Users" button on the left. Then, select the "is_staff" button to give them staff permissions.

2. To add a nurse, click the "Nurses" button, enter the required details in the form, and select the "is_ nurse" button to grant them nurse status. If the user is a registered nurse, select "Yes" in the "is_rn" drop-down field. Registered nurses have the permission to reserve all shifts, including those for practical nurses and assistants.

3. It's recommended to add the user first, before adding their address in the "Address Book" form.
4. To add shifts, complete steps 1-4 first. It's not necessary to include nurse or user information when creating a shift, as it may not be known at that time who will do the shift or who will reserve it (e.g. a nurse, admin, or employer). The nurse and user details can be updated when reserving the shift.

In the authentication and authorization part: Groups have not yet been created.
