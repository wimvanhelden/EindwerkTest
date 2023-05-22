from flask import render_template
from flask_login import login_required, current_user
import bp_tasks
from event_app.bp_home.consts import *
from model_task import Task



@bp_tasks.route('/task-list', methods=['GET'])
@login_required
#list of all added tasks
def do_task_list():
    tasks = Task.query.all()
    return render_template('task/task_list.html', tasks=tasks , user=current_user)