This app was forked from django-swingtime on 8 November 2013 (https://github.com/dakrauth/django-swingtime/tree/b6066f32beab67bf5b02e3f5d9452c439841cf5c)

About Swingtime
===============

`Swingtime` is a [Django](http://www.djangoproject.com/) application similar to a
stripped-down version of iCal for Mac OS X or Google Calendar. `Swingtime` provides  an 
`Event` model that acts as a metadata container for one or more `Occurrence` objects,
which describe specific start and end times.

Swingtime relies heavily upon both the `datetime` standard library package and
the `dateutil` package, featuring direct support for the `dateutil.rrule`
interface to create occurrences.

A fairly simple example:

    >>> from datetime import *
    >>> from swingtime import models as swingtime
    >>> et = swingtime.EventType.objects.create(abbr='work', label='Work Related Events')
    >>> evt = swingtime.Event.objects.create(
    ...     title='New TPS Cover Sheet',
    ...     description='Kiss off, Lumbergh!',
    ...     event_type=et
    ... )
    >>> evt.add_occurrences(datetime(2013,4,1,16), datetime(2013,4,1,16,15), count=5)
    >>> for o in evt.occurrence_set.all():
    ...     print o
    ... 
    New TPS Cover Sheet: 2013-04-01T16:00:00
    New TPS Cover Sheet: 2013-04-02T16:00:00
    New TPS Cover Sheet: 2013-04-03T16:00:00
    New TPS Cover Sheet: 2013-04-04T16:00:00
    New TPS Cover Sheet: 2013-04-05T16:00:00

A bit more elaborate example, using the the convenience function `create_event`:

    >>> from dateutil import rrule
    >>> # pay day is the last Friday of the month at 5pm
    >>> evt = swingtime.create_event(
    ...     'Pay day',
    ...     ('pay', 'Payroll'), # alternate means to add EventType on the fly
    ...     freq=rrule.MONTHLY,
    ...     byweekday=rrule.FR(-1),
    ...     until=datetime(2013,8,1),
    ...     start_time=datetime(2013,4,1,17)
    ... )
    >>> for o in evt.occurrence_set.all():
    ...     print o
    ... 
    Pay day: 2013-04-26T17:00:00
    Pay day: 2013-05-31T17:00:00
    Pay day: 2013-06-28T17:00:00
    Pay day: 2013-07-26T17:00:00

Features
--------

* Support for adding complex event occurrences via `dateutil`
* Ready-made `MultipleOccurrenceForm` for handling complex input
* Daily, monthly, and annual view functions
* Grid-based daily view generator, complete with alternating or sequential 
  `EventType` CSS-class handling
* Slightly better than average documentation, a few test cases, and commented code
* **Built-in demo project / application**

Requirements
------------

* Django 1.4
* Python 2.7 
* [dateutil](http://labix.org/python-dateutil)

