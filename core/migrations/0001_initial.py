# Generated by Django 3.2 on 2022-12-29 11:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, null=True, region=None, unique=True)),
                ('bios', models.CharField(max_length=250, null=True)),
                ('is_nurse', models.BooleanField(default=False)),
                ('is_rn', models.BooleanField(default=False, null=True)),
                ('is_employer', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=64)),
                ('alt_line', models.CharField(blank=True, max_length=64)),
                ('postcode', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[0-9]{5}$', 'Invalid postal code')])),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(blank=True, default='Uusimaa', max_length=64)),
                ('country', models.CharField(default='Suomi', max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AddressBook',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.customuser')),
                ('org_name', models.CharField(max_length=64)),
                ('bank_account_name', models.CharField(blank=True, max_length=30, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Employer',
            },
            bases=('core.customuser',),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.customuser')),
                ('bank_account_name', models.CharField(blank=True, max_length=30, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=20, null=True)),
                ('role', models.CharField(choices=[('RN', 'RN'), ('PN', 'PN'), ('ASST', 'ASST')], max_length=4)),
                ('experience', models.IntegerField(choices=[(0, '<5'), (1, '<10'), (2, '>=10')])),
            ],
            options={
                'verbose_name': 'Nurse',
            },
            bases=('core.customuser',),
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date published')),
                ('updated_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('role', models.CharField(choices=[('RN', 'RN'), ('PN', 'PN'), ('ASST', 'ASST')], max_length=4)),
                ('start_time', models.DateTimeField()),
                ('finish_time', models.DateTimeField()),
                ('published', models.BooleanField(default=False)),
                ('details', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Reserved', 'Reserved'), ('Done', 'Done'), ('Unfilled', 'Unfilled'), ('Cancelled', 'Cancelled')], max_length=200, null=True)),
                ('time_reserved', models.DateTimeField(auto_now_add=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_street', to='core.addressbook')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_employer', to='core.employer')),
                ('nurse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Shift_nurse', to='core.nurse')),
            ],
        ),
    ]
