from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from web.models import Student
from web import db, login_manager
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(id):
    return Student.query.get(int(id))

# ================== AUTH Part ================

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))
    if request.method == 'POST':
        password = request.form['password']
        username = request.form['username']
        
        user = Student.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            flash("Logged in successfully!", 'success')
            login_user(user)
            return redirect(url_for('views.dashboard'))
        elif user is None:
            flash(f"No one account with username {username} found. Please register first!",'warning')
        else:
            flash("Incorect password, try again.", 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html', page='student')

@auth.route('/sign_up', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        student_id = request.form['student_id']
        grade = request.form['grade']
        address = request.form['address']
        region_group = request.form['region_group']
        subdistrict = request.form['subdistrict']
        district = request.form['district']
        province = request.form['province']
        zipcode = request.form['zipcode']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if len(full_name) < 4:
            flash('Full Name must be greater than 4 characters', category='danger')
        elif len(password) < 8:
            flash('Passowrd must be greater than 8 characters', category='danger')
        elif confirm_password != password:
            flash('Passowrd don\'t match.', category='danger')
        else:
            add_student = Student(full_name=full_name, username=username, student_id=student_id, grade=grade, address=address, region_group=region_group, subdistrict=subdistrict, district=district, province=province, zipcode=zipcode, parents='', phone='', best_friend='', ambition='', motto='', disease='', password=generate_password_hash(password, method='sha256'))
            db.session.add(add_student)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template('register.html', page='student')

@auth.route('/logout')
@login_required
def logout():
    flash('You have logged out!', 'warning')
    logout_user()
    session.clear()
    return redirect(url_for('auth.login'))

# @auth.route('/admin_login', methods=['GET', 'POST'])
# def login_admin():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         user = AdminData.query.filter_by(username=username).first()

#         if user and password:
#             flash("Logged in successfully!", 'success')
#             login_user(user)
#             return redirect(url_for('views.dashboard'))
#         elif user is None:
#             flash(f"No one account with username {username} found. Please register first!",'warning')
#         else:
#             flash("Incorect password, try again.", 'error')
#             return redirect(url_for('auth.login_admin'))
#     return render_template('admin/login.html')

# @auth.route('/admin_login')
# def admin_login():
#     # session['logged_in'] = True
#     # return redirect('/admin')
#     if request.method == 'POST':
#         if request.form.get('username') == 'admin' and request.form.get('password') == 'thongkum.app':
#             return redirect(url_for('views.admin_dashboard'))
#     return render_template('/admin/login.html')

# @auth.route('/admin_logout')
# def admin_logout():
#     session.clear()
#     return redirect(url_for('admin/login.html'))