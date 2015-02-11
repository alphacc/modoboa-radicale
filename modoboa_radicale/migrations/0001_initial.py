# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modoboa_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read', models.BooleanField(default=False)),
                ('write', models.BooleanField(default=False)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SharedCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('domain', models.ForeignKey(to='modoboa_admin.Domain')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserCalendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('mailbox', models.ForeignKey(to='modoboa_admin.Mailbox')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='accessrule',
            name='calendar',
            field=models.ForeignKey(related_name='rules', to='radicale.UserCalendar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accessrule',
            name='mailbox',
            field=models.ForeignKey(to='modoboa_admin.Mailbox'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='accessrule',
            unique_together=set([('mailbox', 'calendar')]),
        ),
    ]
