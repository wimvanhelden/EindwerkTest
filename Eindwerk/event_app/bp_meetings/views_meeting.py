from flask import render_template
from flask_login import login_required, current_user
from datetime import datetime
from flask import render_template
from flask_login import login_required, current_user 
from event_app.bp_home.consts import *
from model_meeting import Meeting
import bp_meetings

@bp_meetings.route('/meeting-list', methods=['GET'])
@login_required
def do_meeting_list():
    meetings = Meeting.query.all()
    return render_template('meeting/meeting_list.html', meetings=meetings, datetime=datetime, user=current_user)