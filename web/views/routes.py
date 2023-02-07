from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from web.models import Student, Score, Record_1, Record_2, Record_3_1, Record_3_2, Record_4_1, Record_4_2, Record_4_3, Record_4_4, Record_4_5, Record_4_6, Record_4_7, Record_5, Record_6, Record_7
from web import db, admin
from flask_login import login_required, current_user
from flask_admin.base import BaseView, expose, AdminIndexView, Admin

views = Blueprint('views', __name__)

@views.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('views.dashboard'))
    return render_template('home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/dashboard')
@login_required
def dashboard():
    record_1 = Record_1.query.filter_by(student_id=current_user.id).count()
    record_2 = Record_2.query.filter_by(student_id=current_user.id).count()
    record_3_1 = Record_3_1.query.filter_by(student_id=current_user.id).count()
    record_3_2 = Record_3_2.query.filter_by(student_id=current_user.id).count()
    record_4_1 = Record_4_1.query.filter_by(student_id=current_user.id).count()
    record_4_2 = Record_4_2.query.filter_by(student_id=current_user.id).count()
    record_4_3 = Record_4_3.query.filter_by(student_id=current_user.id).count()
    record_4_4 = Record_4_4.query.filter_by(student_id=current_user.id).count()
    record_4_5 = Record_4_5.query.filter_by(student_id=current_user.id).count()
    record_4_6 = Record_4_6.query.filter_by(student_id=current_user.id).count()
    record_4_7 = Record_4_7.query.filter_by(student_id=current_user.id).count()
    record_5 = Record_5.query.filter_by(student_id=current_user.id).count()
    record_6 = Record_6.query.filter_by(student_id=current_user.id).count()
    record_7 = Record_7.query.filter_by(student_id=current_user.id).count()
    total = record_1+record_2+record_3_1+record_3_2+record_4_1+record_4_2+record_4_3+record_4_4+record_4_5+record_4_6+record_4_7+record_5+record_6+record_7

    signed_1 = Record_1.query.filter_by(sign=True).count()
    signed_2 = Record_2.query.filter_by(sign=True).count()
    signed_3_1 = Record_3_1.query.filter_by(full=True).count()
    signed_3_2 = Record_3_2.query.filter_by(full=True).count()
    signed_4_1 = Record_4_1.query.filter_by(sign=True).count()
    signed_4_2 = Record_4_2.query.filter_by(sign=True).count()
    signed_4_3 = Record_4_3.query.filter_by(sign=True).count()
    signed_4_4 = Record_4_4.query.filter_by(sign=True).count()
    signed_4_5 = Record_4_5.query.filter_by(sign=True).count()
    signed_4_6 = Record_4_6.query.filter_by(sign=True).count()
    signed_4_7 = Record_4_7.query.filter_by(sign=True).count()
    total_sign = signed_1+signed_2+signed_3_1+signed_3_2+signed_4_1+signed_4_2+signed_4_3+signed_4_4+signed_4_5+signed_4_6+signed_4_7

    try:
        progress = (total_sign/total)*100
    except ZeroDivisionError:
        progress = 0

    return render_template('dashboard.html', record_1=record_1, record_2=record_2, record_3_1=record_3_1, record_3_2=record_3_2, record_4_1=record_4_1, record_4_2=record_4_2, record_4_3=record_4_3, record_4_4=record_4_4, record_4_5=record_4_5, record_4_6=record_4_6, record_4_7=record_4_7, record_5=record_5, record_6=record_6, record_7=record_7, total=total, progress=progress)

@views.route('/dashboard/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_profile(id):
    user = Student.query.filter_by(id=id).first()

    if request.method == 'POST':
        if user:
            db.session.delete(user)
            db.session.commit()
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
            parents = request.form['parents']
            phone = request.form['phone']
            best_friend = request.form['best_friend']
            ambition = request.form['ambition']
            motto = request.form['motto']
            disease = request.form['disease']
            # password = request.form['password']   
            
            user = Student(full_name=full_name, username=username, student_id=student_id, grade=grade, address=address, region_group=region_group, subdistrict=subdistrict, district=district, province=province, zipcode=zipcode, parents=parents, phone=phone, best_friend=best_friend, ambition=ambition, motto=motto, disease=disease, password=user.password)
            
            db.session.add(user)
            db.session.commit()
            flash('Profile Updated!', category='success')
            return redirect(url_for('views.dashboard'))
        
        return f"Student with id = {id} Does not exist"

    return render_template('update_profile.html', user=user)

# @views.route('/dashboard/<int:id>/change_password', methods=['GET', 'POST'])
# def change_pass():
#     passd = Student.query.filter_by(password=current_user.password).first()
#     if request.method == 'POST':
#         if 
        

@views.route('/dashboard/<int:id>/record_1', methods=['GET', 'POST'])
@login_required
def rec_1(id):
    user = Student.query.filter_by(id=id).first()
    data = Record_1.query.order_by(Record_1.student_id).all()
    return render_template('record_1.html', data=data, user=user)

@views.route('/dashboard/<int:id>/record_2', methods=['GET', 'POST'])
@login_required
def rec_2(id):
    user = Student.query.filter_by(id=id).first()
    data = Record_2.query.order_by(Record_2.student_id).all()
    return render_template('record_2.html', data=data, user=user)

@views.route('/dashboard/<int:id>/record_3', methods=['GET', 'POST'])
@login_required
def rec_3(id):
    user = Student.query.filter_by(id=id).first()
    data = Record_3_1.query.order_by(Record_3_1.student_id).all()
    data2 = Record_3_1.query.order_by(Record_3_1.student_id).all()
    return render_template('record_3.html', data=data, data2=data2, user=user)

@views.route('/dashboard/<int:id>/record_4', methods=['GET', 'POST'])
@login_required
def rec_4(id):
    user = Student.query.filter_by(id=id).first()
    data = Record_4_1.query.order_by(Record_4_1.student_id).all()
    data2 = Record_4_2.query.order_by(Record_4_2.student_id).all()
    data3 = Record_4_3.query.order_by(Record_4_3.student_id).all()
    data4 = Record_4_4.query.order_by(Record_4_4.student_id).all()
    data5 = Record_4_5.query.order_by(Record_4_5.student_id).all()
    data6 = Record_4_6.query.order_by(Record_4_6.student_id).all()
    data7 = Record_4_7.query.order_by(Record_4_7.student_id).all()
    return render_template('record_4.html', data=data, data2=data2, data3=data3, data4=data4, data5=data5, data6=data6, data7=data7, user=user)

@views.route('/dashboard/<int:id>/record_5', methods=['GET', 'POST'])
@login_required
def rec_5(id):
    user = Student.query.filter_by(id=id).first()
    data = Record_5.query.order_by(Record_5.student_id).all()
    return render_template('record_5.html', data=data, user=user)

@views.route('/dashboard/<int:id>/record_6', methods=['GET', 'POST'])
@login_required
def rec_6(id):
    user = Student.query.filter_by(id=id).first()
    data = Record_6.query.order_by(Record_6.student_id).all()

    pray1 = Record_6.query.filter_by(id=1).first()
    pray2 = Record_6.query.filter_by(id=2).first()
    pray3 = Record_6.query.filter_by(id=3).first()
    pray4 = Record_6.query.filter_by(id=4).first()
    pray5 = Record_6.query.filter_by(id=5).first()
    pray6 = Record_6.query.filter_by(id=6).first()
    pray7 = Record_6.query.filter_by(id=7).first()
    pray8 = Record_6.query.filter_by(id=8).first()
    pray9 = Record_6.query.filter_by(id=9).first()
    pray10 = Record_6.query.filter_by(id=10).first()

    qty = int(pray1.subh+pray1.dzuhr+pray1.ashr+pray1.maghrib+pray1.isya)
    qty2 = int(pray2.subh+pray2.dzuhr+pray2.ashr+pray2.maghrib+pray2.isya)
    qty3 = int(pray3.subh+pray3.dzuhr+pray3.ashr+pray3.maghrib+pray3.isya)
    qty4 = int(pray4.subh+pray4.dzuhr+pray4.ashr+pray4.maghrib+pray4.isya)
    qty5 = int(pray5.subh+pray5.dzuhr+pray5.ashr+pray5.maghrib+pray5.isya)
    qty6 = int(pray6.subh+pray6.dzuhr+pray6.ashr+pray6.maghrib+pray6.isya)
    qty7 = int(pray7.subh+pray7.dzuhr+pray7.ashr+pray7.maghrib+pray7.isya)
    qty8 = int(pray8.subh+pray8.dzuhr+pray8.ashr+pray8.maghrib+pray8.isya)
    qty9 = int(pray9.subh+pray9.dzuhr+pray9.ashr+pray9.maghrib+pray9.isya)
    qty10 = int(pray10.subh+pray10.dzuhr+pray10.ashr+pray10.maghrib+pray10.isya)
    return render_template('record_6.html', data=data, user=user, qty=qty, qty2=qty2, qty3=qty3, qty4=qty4, qty5=qty5, qty6=qty6, qty7=qty7, qty8=qty8, qty9=qty9, qty10=qty10)

@views.route('/dashboard/<int:id>/record_7', methods=['GET', 'POST'])
@login_required
def rec_7(id):
    user = Student.query.filter_by(id=id).first()
    data = Record_7.query.order_by(Record_7.student_id).all()
    return render_template('record_7.html', data=data, user=user)

class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        student = Student.query.all()
        return self.render('admin/index.html', student=student)

admin = Admin(index_view=MyHomeView())