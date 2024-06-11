from flask import Flask,Blueprint,redirect,url_for,render_template,request,session
from database import*
import uuid

admin=Blueprint('admin',__name__)

@admin.route('admin_home',methods=['get','post'])
def admin_home():

	return render_template('admin_home.html')

@admin.route('admin_register_employee',methods=['get','post'])
def admin_register_employee():
	data={}

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)

	if action=='delete':
		q="delete from login where login_id=(select login_id from gym_instructor where instructor_id='%s')"%(id)
		delete(q)

		q="delete from gym_instructor where instructor_id='%s'"%(id)
		delete(q)

		return redirect(url_for('admin.admin_register_employee'))

	if action=='update':
		q="select * from gym_instructor where instructor_id='%s'"%(id)
		res=select(q)
		data['update_employee']=res


	if 'uemployee' in request.form:
		first_name=request.form['ufname']
		last_name=request.form['ulname']
		phone=request.form['uphone']
		email=request.form['uemail']

		q="update gym_instructor set gfirst_name='%s',glast_name='%s',phone='%s',email='%s' where instructor_id='%s'"%(first_name,last_name,phone,email,id)
		update(q)
		return redirect(url_for('admin.admin_register_employee'))

	if 'employee' in request.form:
		first_name=request.form['fname']
		last_name=request.form['lname']
		age=request.form['age']
		gender=request.form['gender']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['user']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		# if len(res):
		# 	flash("username and password is already exist")
		# else:

		q="insert into login values(null,'%s','%s','employee')"%(username,password)
		ids=insert(q)

		q="insert into gym_instructor values(null,'%s','%s','%s','%s','%s','%s','%s')"%(ids,first_name,last_name,age,gender,phone,email)
		insert(q)

		return redirect(url_for('admin.admin_register_employee'))

	q="select * from gym_instructor"
	res=select(q)
	data['employee_details']=res
	return render_template('admin_register_employee.html',data=data)


@admin.route('admin_register_physician',methods=['get','post'])
def admin_register_physician():
	data={}

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)

	if action=='delete':
		q="delete from login where login_id=(select login_id from physician where physician_id='%s')"%(id)
		delete(q)

		q="delete from physician where physician_id='%s'"%(id)
		delete(q)

		return redirect(url_for('admin.admin_register_physician'))

	if action=='update':
		q="select * from physician where physician_id='%s'"%(id)
		res=select(q)
		data['update_physician']=res


	if 'uphysician' in request.form:
		first_name=request.form['ufname']
		last_name=request.form['ulname']
		phone=request.form['uphone']
		email=request.form['uemail']

		q="update physician set first_name='%s',last_name='%s',phone='%s',email='%s' where physician_id='%s'"%(first_name,last_name,phone,email,id)
		update(q)
		return redirect(url_for('admin.admin_register_physician'))

	if 'physician' in request.form:
		first_name=request.form['fname']
		last_name=request.form['lname']
		age=request.form['qualification']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['user']
		password=request.form['pass']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		# if len(res):
		# 	flash("username and password is already exist")
		# else:

		q="insert into login values(null,'%s','%s','physician')"%(username,password)
		ids=insert(q)

		q="insert into physician values(null,'%s','%s','%s','%s','%s','%s')"%(ids,first_name,last_name,age,phone,email)
		insert(q)

		return redirect(url_for('admin.admin_register_physician'))

	q="select * from physician"
	res=select(q)
	data['physician_details']=res

	return render_template('admin_register_physician.html',data=data)

@admin.route('admin_verify_user',methods=['get','post'])
def admin_verify_user():

	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)
	if action=="verify":
		q="update users set payment_status='Payment Confirm' where user_id='%s'"%(id)
		update(q)
		q="update login set user_type='user' where login_id=(select login_id from users where user_id='%s')"%(id)
		print(q)
		update(q)

	if 'allot' in request.form:
		instructor_id=request.form['instructor_id']
		user_id=request.form['user_id']
		q="update users set instructor_id='%s' where user_id='%s'"%(instructor_id,user_id)
		update(q)
	q="select * from gym_instructor"
	res=select(q)
	data['view_instructor']=res
	q="SELECT * FROM users where payment_status !='pending' "
	# q="SELECT * FROM users INNER JOIN `batches` USING(`batch_id`)"
	res=select(q)
	data['view_user']=res

	return render_template('admin_verify_user.html',data=data)



@admin.route('admin_add_new_batches',methods=['get','post'])
def admin_add_new_batches():
	data={}
	if 'batches' in request.form:
		batch=request.form['batch']
		stime=request.form['stime']
		etime=request.form['etime']
		instructor_id=request.form['instructor_id']
		q="insert INTO `batches` value(NULL,'%s','%s','%s','%s')"%(batch,stime,etime,instructor_id)
		insert(q)

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)
	if action=="delete":
		q="DELETE FROM `batches` WHERE `batch_id`='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_add_new_batches'))


	if action=="update":
		q="select * from batches where batch_id='%s'"%(id)
		res=select(q)
		data['batchsss']=res


	if 'update' in request.form:
		batch=request.form['batch']
		stime=request.form['stime']
		etime=request.form['etime']
		
		q="update batches set batch_name='%s',start_time='%s',end_time='%s' where batch_id='%s'"%(batch,stime,etime,id)
		update(q)
		return redirect(url_for('admin.admin_add_new_batches'))


 
	q="select * from gym_instructor"
	res=select(q)
	data['view_instructor']=res
	
	q="select * from batches inner join gym_instructor using(instructor_id)"
	res=select(q)
	data['batch_details']=res


	return render_template('admin_add_new_batches.html',data=data)

@admin.route('admin_view_complaint',methods=['get','post'])
def admin_view_complaint():
	data={}

	q="select * from complaints inner join users using(user_id)"
	res=select(q)
	data['complaints']=res
	j=0
	for i in range(1,len(res)+1):
		if 'replys'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(res[j]['complaint_id'])
			q="update complaints set reply='%s' where complaint_id='%s'"%(reply,res[j]['complaint_id'])
			print(q)
			update(q)
			return redirect(url_for('admin.admin_view_complaint'))
		j=j+1
	

	return render_template('admin_view_complaint.html',data=data)

@admin.route('admin_view_feedback',methods=['get','post'])
def admin_view_feedback():
	data={}

	q="select * from feedback inner join users using(user_id)"
	res=select(q)
	data['feedback']=res
	j=0
	for i in range(1,len(res)+1):
		if 'replys'+str(i) in request.form:
			feedback_reply=request.form['feedback_reply'+str(i)]
			print(res[j]['feedback_id'])
			q="update feedback set feedback_reply='%s' where feedback_id='%s'"%(feedback_reply,res[j]['feedback_id'])
			print(q)
			update(q)
			return redirect(url_for('admin.admin_view_feedback'))
		j=j+1

	return render_template('admin_view_feedback.html',data=data)

@admin.route('admin_view_attendance_user',methods=['get','post'])
def admin_view_attendance_user():
	data={}

	q="select * from attendance inner join users using(user_id)"
	res=select(q)
	data['attendance']=res

	return render_template('admin_view_attendance_user.html',data=data)

@admin.route('admin_view_payment',methods=['get','post'])
def admin_view_payment():
	data={}

	q="select * from payments inner join users using(user_id)"
	res=select(q)
	data['payment']=res

	return render_template('admin_view_payment.html',data=data)

@admin.route('admin_allot_user_gym_instructor',methods=['get','post'])
def admin_allot_user_gym_instructor():
	data={}

	user_id=request.args['user_id']
	q="select * from batches  inner join gym_instructor using (instructor_id)"
	res=select(q)
	data['batches']=res





	qq="select * from users inner join batches using(batch_id)   inner join gym_instructor using (instructor_id) where user_id='%s'"%(user_id)
	rr=select(qq)
	if rr:
		data['rr']=rr

	if 'allot' in request.form:
		batches_id=request.form['batches_id']
		
		q="update users set batch_id='%s' where user_id='%s'"%(batches_id,user_id)
		update(q)
		return redirect(url_for('admin.admin_allot_user_gym_instructor',user_id=user_id))

	return render_template('admin_allot_user_gym_instructor.html',data=data)



@admin.route('/admin_manage_category',methods=['get','post'])
def admin_manage_category():
	data={}
	if 'submit' in request.form:
		cat=request.form['cat']
		q="select * from category where category='%s'"%(cat)
		res=select(q)
		if res:
			flash('THIS CATEGORY IS ALREADY ADDED')
			return redirect(url_for('admin.admin_manage_category'))
		else:
			q="insert into category values(NULL,'%s')"%(cat)
			lid=insert(q)
			return redirect(url_for('admin.admin_manage_category'))

	q="select * from category"
	res=select(q)
	if res:
		data['category']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from category where category_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_category'))
	if action=='update':
		q="select * from category where category_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		cat=request.form['cat']
		q="update category set category='%s' where category_id='%s'"%(cat,id)
		update(q)
		return redirect(url_for('admin.admin_manage_category'))
	return render_template('admin_manage_category.html',data=data)

@admin.route('/admin_manage_products',methods=['get','post'])
def admin_manage_products():
	data={}
	catid=request.args['catid']
	data['catid']=catid
	name=request.args['name']
	data['name']=name


	if 'submit' in request.form:
		product=request.form['product']
		qua=request.form['qua']
		rate=request.form['rate']
		status=request.form['status']
		
		q="insert into products values(NULL,'%s','%s','%s','%s','%s')"%(catid,product,qua,rate,status)
		lid=insert(q)	
		# flash("ADDED SUCESSFULLY")
		return redirect(url_for('admin.admin_manage_products',catid=catid,name=name))
	q="select * from products where category_id='%s'"%(catid)
	res=select(q)
	if res:
		data['product']=res
		print(res)
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	if action=='delete':
		q="delete from products where product_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_products',catid=catid,name=name))
	if action=='update':
		q="select * from products where product_id='%s'"%(id)
		data['updater']=select(q)
	if 'update' in request.form:
		product=request.form['product']
		qua=request.form['qua']
		rate=request.form['rate']
		status=request.form['status']
		q="update products set product='%s',quantity='%s',rate='%s',status='%s' where product_id='%s'"%(product,qua,rate,status,id)
		update(q)
		return redirect(url_for('admin.admin_manage_products',catid=catid,name=name))
	return render_template('admin_manage_products.html',data=data)



@admin.route('/admin_view_bookings',methods=['get','post'])
def admin_view_bookings():
	data={}
	q="SELECT * from bookingmaster INNER JOIN users USING(user_id)  WHERE `bookingmaster`.`status`!='pending'"
	res=select(q)
	print(res)
	data['orders']=res
	return render_template("admin_view_bookings.html",data=data)


@admin.route('/admin_view_oproducts',methods=['get','post'])
def admin_view_oproducts():
	bid=request.args['bid']
	data={}
	q="SELECT *,`bookingchild`.`quantity` AS bquantity FROM `bookingchild`  INNER JOIN products USING(product_id) WHERE `bmaster_id`='%s'"%(bid)
	res=select(q)
	print(res)
	data['product']=res
	return render_template("admin_view_oproducts.html",data=data)





@admin.route('/admin_manage_tournament',methods=['get','post'])
def admin_manage_tournament():


	
	data={}

	q="select * from tournament"
	res=select(q)
	data['tou']=res

	if 'submit' in request.form:
		tname=request.form['name']
		place=request.form['place']
		date=request.form['date']
		time=request.form['time']
		
		q="insert into tournament values(NULL,'%s','%s','%s','%s')"%(tname,place,date,time)
		lid=insert(q)	
		return redirect(url_for('admin.admin_manage_tournament'))
	



	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)
	if action=="delete":
		q="DELETE FROM `tournament` WHERE `tournament_id`='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_manage_tournament'))


	if action=="update":
		q="select * from tournament where tournament_id='%s'"%(id)
		res=select(q)
		data['batchsss']=res


	if 'update' in request.form:
		tname=request.form['name']
		place=request.form['place']
		date=request.form['date']
		time=request.form['time']
		
		q="update tournament set name='%s',place='%s',date='%s',time='%s' where tournament_id='%s'"%(tname,place,date,time,id)
		update(q)
		return redirect(url_for('admin.admin_manage_tournament'))

	
		
	return render_template("admin_manage_tournament.html",data=data)



@admin.route('employee_manage_equipments',methods=['get','post'])
def employee_manage_equipments():
	data={}
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
	print(action)
	if action=="delete":
		q="DELETE FROM `equipments` WHERE `equipment_id`='%s'"%(id)
		delete(q)
	if action=="update":
		q="select * from equipments where equipment_id='%s'"%(id)
		res=select(q)
		data['update_equipments']=res
	if 'uequipment' in request.form:
		ueqname=request.form['ueqname']
		qnty=request.form['qnty']
		udescription=request.form['udescription']
		uimage=request.files['uimage']
		path='static/img/'+str(uuid.uuid4())+uimage.filename
		uimage.save(path)
		q="update equipments set name='%s',description='%s',image='%s',qnty='%s' where equipment_id='%s'"%(ueqname,udescription,path,qnty,id)
		update(q)
		return redirect(url_for('employee.employee_manage_equipments'))

	if 'equipment' in request.form:
		eqname=request.form['eqname']
		description=request.form['description']
		qnty=request.form['qnty']
		image=request.files['image']
		path='static/img/'+str(uuid.uuid4())+image.filename
		image.save(path)
		q="INSERT INTO `equipments` VALUES(NULL,'%s','%s','%s','%s')"%(eqname,description,path,qnty)
		insert(q)

	q="select * from equipments"
	res=select(q)
	data['equipments_details']=res

	return render_template('employee_manage_equipments.html',data=data)

