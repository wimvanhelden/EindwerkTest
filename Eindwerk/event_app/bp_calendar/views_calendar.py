from flask import render_template
from flask_login import login_required, current_user
from flask import render_template
from flask_login import login_required, current_user 
from event_app.bp_home.consts import *
from bp_events.controller_event import get_events
from bp_meetings.controller_meeting import get_meetings
from bp_tasks.controller_task import get_tasks
import bp_calendar

@bp_calendar.route('/calendar', methods=['GET'])
@login_required
def do_calendar():
    events = get_events()
    meetings = get_meetings()
    tasks = get_tasks()
    return render_template('calendar/calendar.html', events=events, meetings=meetings, tasks=tasks)
