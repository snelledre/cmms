from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, current_user
from . import department
from .. import db
from ..models import Department, Permission
from .forms import DepartmentForm, DepartmentShowForm, DepartmentEditForm
from ..decorators import admin_required, permission_required


@department.route('/', methods=['GET'])
@login_required
@admin_required
def index():
    departments = Department.query.all()
    return render_template('department/index.html', departments=departments)


@department.route('/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create():
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data[0].upper() + form.name.data[1:],
                                description=form.description.data)
        db.session.add(department)
        db.session.commit()
        flash(u'Afdeling is succesvol aangemaakt.', 'success')
        return redirect(url_for('department.index'))
    return render_template('department/create.html', form=form)


@department.route('/<int:id>')
@login_required
@admin_required
def show(id):
    department = Department.query.get_or_404(id)
    return render_template('department/show.html', departments=[department])


@department.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit(id):
    department = Department.query.get_or_404(id)
    form = DepartmentEditForm(department.name)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash(u'Afdeling is bijgewerkt.', 'success')
        return redirect(url_for('department.show', id=department.id))
    elif request.method == 'GET':
        form.name.data = department.name
        form.description.data = department.description
    return render_template('department/edit.html', department=department, form=form)


@department.route("/delete/<int:id>", methods=['POST'])
@login_required
@admin_required
def delete(id):
    department = Department.query.get_or_404(id)

    db.session.delete(department)
    db.session.commit()
    flash(u'Afdeling is verwijderd', 'success')
    return redirect(url_for('department.index'))
