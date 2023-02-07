from sqlalchemy.sql import func
from web import db, admin
from flask_login import UserMixin
from datetime import datetime
from flask_admin.contrib.sqla.view import ModelView
from flask_admin.base import BaseView, expose
# from flask_admin.contrib.sqla import ModelView
# from flask_admin.menu import MenuLink
# from flask_login import current_user

now = datetime.now()

# class AdminData(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=True)
#     password = db.Column(db.String, nullable=True)

class Student(db.Model, UserMixin):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    student_id = db.Column(db.String, nullable=False, unique=True)
    grade = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    region_group = db.Column(db.String, nullable=False)
    subdistrict = db.Column(db.String, nullable=False)
    district = db.Column(db.String, nullable=False)
    province = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.String, nullable=False)
    parents = db.Column(db.String, nullable=False, default=None)
    phone = db.Column(db.String, nullable=False, default=None)
    best_friend = db.Column(db.String, nullable=False, default=None)
    ambition = db.Column(db.String, nullable=False, default=None)
    motto = db.Column(db.String, nullable=False, default=None)
    disease = db.Column(db.String, nullable=False, default=None)
    password = db.Column(db.String, nullable=False)
    scores = db.relationship('Score', backref='student', lazy=True)
    rec_1 = db.relationship('Record_1', backref='student', lazy=True)
    rec_2 = db.relationship('Record_2', backref='student', lazy=True)
    rec_3_1 = db.relationship('Record_3_1', backref='student', lazy=True)
    rec_3_2 = db.relationship('Record_3_2', backref='student', lazy=True)
    rec_4_1 = db.relationship('Record_4_1', backref='student', lazy=True)
    rec_4_2 = db.relationship('Record_4_2', backref='student', lazy=True)
    rec_4_3 = db.relationship('Record_4_3', backref='student', lazy=True)
    rec_4_4 = db.relationship('Record_4_4', backref='student', lazy=True)
    rec_4_5 = db.relationship('Record_4_5', backref='student', lazy=True)
    rec_4_6 = db.relationship('Record_4_6', backref='student', lazy=True)
    rec_4_7 = db.relationship('Record_4_7', backref='student', lazy=True)
    rec_5 = db.relationship('Record_5', backref='student', lazy=True)
    rec_6 = db.relationship('Record_6', backref='student', lazy=True)
    rec_7 = db.relationship('Record_7', backref='student', lazy=True)

    def __repr__(self):
        return f"Student('{self.full_name}','{self.username}','{self.student_id}','{self.grade}')"

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

class Record_1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.to_char("%d %B, %Y"))
    rec_list = db.Column(db.String, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    ability = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_3_1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    mid = db.Column(db.Boolean, nullable=False, default=False)
    advance = db.Column(db.Boolean, nullable=False, default=False)
    full = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_3_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    mid = db.Column(db.Boolean, nullable=False, default=False)
    advance = db.Column(db.Boolean, nullable=False, default=False)
    full = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_4_1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_4_2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_4_3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_4_4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_4_5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_4_6(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_4_7(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rec_list = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.to_char("%d %B, %Y"))
    rec_list = db.Column(db.String, nullable=False)
    leave = db.Column(db.DateTime(timezone=True), default=func.to_char("%d %B, %Y"))
    sign_1 = db.Column(db.Boolean, nullable=False, default=False)
    entry = db.Column(db.DateTime(timezone=True), default=func.to_char("%d %B, %Y"))
    sign_2 = db.Column(db.Boolean, nullable=False, default=False)
    note = db.Column(db.String, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    # def time_only(self):
    #     return (self.leave.strftime("%H:%M:%S"),self.entry.strftime("%H:%M:%S"))

class Record_6(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # quantity = db.Column(db.Integer, nullable=False)
    subh = db.Column(db.Integer, nullable=False, default=0)
    dzuhr = db.Column(db.Integer, nullable=False, default=0)
    ashr = db.Column(db.Integer, nullable=False, default=0)
    maghrib = db.Column(db.Integer, nullable=False, default=0)
    isya = db.Column(db.Integer, nullable=False, default=0)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

class Record_7(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String, nullable=False)
    sign = db.Column(db.Boolean, nullable=False, default=False)
    notes = db.Column(db.String, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

# class SecureModelView(ModelView):
#     def is_accessible(self):
#         if "logged_in" in session:
#             return True
#         else:
#             abort(403)

# class MyAdminIndexView(admin.AdminIndexView):
#     @expose('/')
#     def index(self):
#         if not LoginManager.current_user.is_authenticated:
#             return redirect(url_for('.login_view'))
#         return super(MyAdminIndexView, self).index()

#     @expose('/login/', methods=('GET', 'POST'))
#     def login_view(self):
#         # handle user login
#         form = LoginForm(request.form)
#         if helpers.validate_form_on_submit(form):
#             user = form.get_user()
#             login.login_user(user)

#         if login.current_user.is_authenticated:
#             return redirect(url_for('.index'))
#         link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
#         self._template_args['form'] = form
#         self._template_args['link'] = link
#         return super(MyAdminIndexView, self).index()

# class DefaultModelView(ModelView):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#     def is_accessible(self):
#         return current_user.is_authenticated and current_user.is_admin
#     def inaccessible_callback(self, *args, **kwargs):
#         return redirect(url_for('auth.login', next=request.url))

# class MyAdminIndexView(AdminIndexView):
#     def is_accessible(self):
#         return current_user.is_authenticated and current_user.is_admin

#     def inaccessible_callback(self, name, **kwargs):
#         return redirect(url_for('auth.login', next=request.url))

#     @expose('/')
#     def index(self):
#         if not current_user.is_authenticated and current_user.is_admin:
#             return redirect(url_for('auth.login'))
#         return super(MyAdminIndexView, self).index()

# admin.add_view(DefaultModelView(AdminData, db.session))
# admin.add_link(MenuLink(name='Logout', category='', url='/auth/logout?next=/admin'))
admin.add_view(ModelView(Student, db.session, name='Student', menu_icon_type='fa', menu_icon_value='fa-users'))
admin.add_view(ModelView(Score, db.session, name='Scores', menu_icon_type='fa', menu_icon_value='fa-star'))
admin.add_view(ModelView(Record_1, db.session, name='Good Deeds & Volunteer Spirit Record', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_2, db.session, name='Activity Record', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_3_1, db.session, name='General Subjects Record', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_3_2, db.session, name='Course Subjects Record', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_4_1, db.session, name='Practical Exams Record (Religion)', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_4_2, db.session, name='Practical Exams Record (Society)', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_4_3, db.session, name='Practical Exams Record (Computer)', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_4_4, db.session, name='Practical Exams Record (Science)', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_4_5, db.session, name='Practical Exams Record (Math)', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_4_6, db.session, name='Practical Exams Record (Thai Language)', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_4_7, db.session, name='Practical Exams Record (English Language)', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_5, db.session, name='Permission Request Record', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_6, db.session, name='Prayer Summary Record', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
admin.add_view(ModelView(Record_7, db.session, name='Homecoming Record', category='Record Lists', menu_icon_type='fa', menu_icon_value='fa-tasks'))
# admin.add_view(SecureModelView(Student, db.session))
# admin.add_view(SecureModelView(Record_1, db.session))
# admin.add_view(SecureModelView(Record_2, db.session))
# admin.add_view(SecureModelView(Record_3_1, db.session))
# admin.add_view(SecureModelView(Record_3_2, db.session))
# admin.add_view(SecureModelView(Record_4_1, db.session))
# admin.add_view(SecureModelView(Record_4_2, db.session))
# admin.add_view(SecureModelView(Record_4_3, db.session))
# admin.add_view(SecureModelView(Record_4_4, db.session))
# admin.add_view(SecureModelView(Record_4_5, db.session))
# admin.add_view(SecureModelView(Record_4_6, db.session))
# admin.add_view(SecureModelView(Record_4_7, db.session))
# admin.add_view(SecureModelView(Record_5, db.session))
# admin.add_view(SecureModelView(Record_6, db.session))
# admin.add_view(SecureModelView(Record_7, db.session))
