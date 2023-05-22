from flask import render_template
from flask_login import login_required, current_user

from ..bp_home.consts import *
from .model_task import Task
from flask import Blueprint

bp_tasks = Blueprint('bp_tasks', __name__)


@bp_tasks.route('/task-list', methods=['GET'])
@login_required
#list of all added tasks
def do_task_list():
    tasks = Task.query.all()
    return render_template('task/task_list.html', tasks=tasks , user=current_user)