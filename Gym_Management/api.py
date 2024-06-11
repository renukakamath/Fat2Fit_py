from flask import Blueprint,render_template,redirect,url_for,session,request
from database import*
import uuid
# import demjson

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
import random


api=Blueprint('api',__name__)
@api.route('/login/',methods=['get','post'])
def login():
	data={}
	data.update(request.args)
	username = request.args['username']
	password = request.args['password']
	q="SELECT * FROM `login` WHERE `username`='%s' AND `password` ='%s'"%(username,password)
	res = select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return  str(data)
@api.route('/register/',methods=['get','post'])
def register():
	data={}
	fname=request.args['fname']
	lname=request.args['lname']

	gender=request.args['gender']
	age=request.args['age']
	weight=request.args['weight']
	height=request.args['height']
	phone=request.args['phone']
	email=request.args['email']
	username=request.args['username']
	password=request.args['password']

	q="select * from login where username='%s'"%(username)
	res=select(q)

	if res:
		data['status'] = "failed"

	else:
		
		q="Insert into login values (null,'%s','%s','pending')"%(username,password)
		ids=insert(q)
		print(q)
		q="INSERT INTO `users` VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','0','pending')"%(ids,fname,lname,age,gender,weight,height,phone,email)
		uid=insert(q)
		print(q)
		if uid:

			email = email
			loginid = ids

			otp = random.randint(1000, 9999)
			# email=email
			# print(email)
			pwd = "YOUR OTP : " + str(otp)
			print(pwd)
			try:
				gmail = smtplib.SMTP('smtp.gmail.com', 587)
				gmail.ehlo()
				gmail.starttls()
				gmail.login('handoutfoodcommunity@gmail.com', 'xkyokbuzwopremsz')
			except Exception as e:
				print("Couldn't setup email!!" + str(e))

			pwd = MIMEText(pwd)

			pwd['Subject'] = 'One Time Password'

			pwd['To'] = email

			pwd['From'] = 'handoutfoodcommunity@gmail.com.com'

			try:
				gmail.send_message(pwd)
				print(pwd)
				data['status'] = "success"

			except Exception as e:
				print("COULDN'T SEND EMAIL", str(e))
			else:
				data['status'] = "failed"

			data['status'] = "success"
			data['data_o'] = otp
			data['data1'] = ids

			data['status']="Success"
			data['user_id']=uid
		return str(data)

	@api.route('/viewpayment/',methods=['get','post'])
	def viewpayment():
		data={}
		q="SELECT * FROM `batches`"
		res=select(q)
		if(len(res) > 0):
			data['status']  = 'success'
			data['data'] = res
		else:
			data['status']	= 'failed'
		data['method']='batch'


	return str(data)
@api.route('/payment/',methods=['get','post'])
def payment():
	data={}
	batch_id=request.args['batch_id']
	user_id=request.args['user_id']
	amount=request.args['amount']

	q="INSERT INTO `payments` VALUES(NULL,'%s','%s','Fee',CURDATE())"%(user_id,amount)
	insert(q)
	q="UPDATE `users` SET `batch_id`='%s',`payment_status`='Paid' WHERE `user_id`='%s'"%(batch_id,user_id)
	update(q)
	q="UPDATE `login` SET `user_type`='user' WHERE `login_id`=(SELECT `login_id` FROM `users` WHERE `user_id`='%s')"%(user_id)
	update(q)
	print(q)
	data['status']="success"
	data['method']='paid'
	

	return str(data)
	
@api.route('/equipments/',methods=['get','post'])
def equipments():
	data={}

	q="SELECT * FROM `equipments`"
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return str(data)


	
@api.route('/vequipments/',methods=['get','post'])
def vequipments():
	data={}
	equipment_id=request.args['equipment_id']
	q="SELECT * FROM `workouts` WHERE `equipment_id`='%s'"%(equipment_id)
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return str(data)
@api.route('/payments/',methods=['get','post'])
def payments():
	data={}
	log_id=request.args['log_id']
	amount=request.args['amount']
	q="INSERT INTO `payments` VALUES(NULL,'%s','%s','Subscription',CURDATE())"%(log_id,amount)
	insert(q)
	q="update users set payment_status='Paid' where user_id='%s'"%(log_id)
	update(q)
	data['status']  = 'success'

	return str(data)
@api.route('/viewdiet/',methods=['get','post'])
def viewdiet():
	data={}
	log_id=request.args['log_id']
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS physician_name FROM `user_diets` INNER JOIN `physician` USING(`physician_id`) WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s')"%(log_id)
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	return str(data)
@api.route('/vmessage/',methods=['get','post'])
def vmessage():
	data={}
	log_id=request.args['log_id']
	q="SELECT * FROM `message` WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s')"%(log_id)
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'

	data['method']='vmessage'
	return str(data)
@api.route('/smessage/',methods=['get','post'])
def smessages():
	data={}
	log_id=request.args['log_id']
	physician_id=request.args['physician_id']
	
	message=request.args['message']

	q="INSERT INTO `message` VALUES(NULL,(SELECT `user_id` FROM `users` WHERE `login_id`='%s'),'%s','%s','pending',CURDATE())"%(log_id,physician_id,message)
	insert(q)
	data['status']  = 'success'
	data['method']='smessage'


	
	return str(data)
@api.route('/vcomplaint/',methods=['get','post'])
def vcomplaint():
	data={}
	log_id=request.args['log_id']
	q="SELECT * FROM `complaints`  WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s')"%(log_id)
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'

	data['method']='view'
	return str(data)
@api.route('/scomplaint/',methods=['get','post'])
def scomplaint():
	data={}
	log_id=request.args['log_id']
	message=request.args['message']

	q="INSERT INTO `complaints` VALUES (NULL,(SELECT `user_id` FROM `users` WHERE `login_id`='%s'),'%s','pending',CURDATE())"%(log_id,message)
	insert(q)
	data['status']  = 'success'
	data['method']='send'


	
	return str(data)
@api.route('/vfeedback/',methods=['get','post'])
def vfeedback():
	data={}
	log_id=request.args['log_id']
	q="SELECT * FROM `feedback`  WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s')"%(log_id)
	res=select(q)
	if(len(res) > 0):
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'

	data['method']='view'
	return str(data)
@api.route('/sfeedback/',methods=['get','post'])
def sfeedback():
	data={}
	log_id=request.args['log_id']
	
	
	message=request.args['message']

	q="INSERT INTO `feedback` VALUES (NULL,(SELECT `user_id` FROM `users` WHERE `login_id`='%s'),'%s','pending',CURDATE())"%(log_id,message)
	insert(q)
	data['status']  = 'success'
	data['method']='send'


	
	return str(data)




@api.route('/View_products',methods=['get','post'])
def View_products():
	data={}
	data['method']='View_products'
	q="SELECT * FROM `products` INNER JOIN `category` USING(`category_id`)"
	print(q)
	res=select(q)
	if res:
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	return str(data)


@api.route('/Add_to_cart',methods=['get','post'])
def Add_to_cart():
    data={}

    loginid=request.args['loginid']
    product_id=request.args['product_id']
    qnty=request.args['qnty']
    amount=request.args['amount']

    flag=0
    q="Select * from bookingmaster  WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s') and status='Pending'"%(loginid)
    result = select(q)
    if not result:
        q="INSERT INTO `bookingmaster` VALUES(null,(select user_id from users where login_id='%s'),'%s',now(),'Pending')"%(loginid,amount)
        id=insert(q)

    else:
        id=result[0]['bmaster_id']
        flag=1
	
    q1="Select * from bookingmaster inner join bookingchild using(bmaster_id)  WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s') and status='Pending' and product_id='%s'"%(loginid,product_id)
    res1=select(q1)

    if res1:
        qw="UPDATE `bookingchild` SET `quantity`=`quantity`+'%s',amount=amount+'%s' WHERE `bmaster_id`='%s'"%(qnty,amount,result[0]['bmaster_id'])
        update(qw)
    else:
        qs="INSERT INTO `bookingchild`(`bmaster_id`,`product_id`,`quantity`,`amount`) VALUES('%s','%s','%s','%s')"%(id,product_id,qnty,amount)
        insert(qs)
    if flag==1:
        qf="UPDATE `bookingmaster` SET `total`=`total`+'%s' WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s') and status='Pending'"%(amount,loginid)
        update(qf)
  
    data['status']  = 'success'
    data['method']='Add_to_cart'
    return  str(data)


@api.route('/View_cart_items',methods=['get','post'])
def View_cart_items():
	data={}
	
	login_id = request.args['login_id']
 
	q="SELECT *,`bookingchild`.`quantity` AS bqnty,`bookingmaster`.`status` AS bstatus FROM `bookingmaster` INNER JOIN `bookingchild` USING(`bmaster_id`) INNER JOIN `products` USING(`product_id`) INNER JOIN `category` USING(`category_id`) WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s') AND `bookingmaster`.`status` ='Pending'"%(login_id)
	print(q)
	res = select(q)
	print(res)
	if res :
		# q="select total from bookingmaster WHERE `user_id`=(SELECT `user_id` FROM `user` WHERE `login_id`='%s')"%(login_id)
		# select(q)
		data['status']  = 'success'
		data['bid']=res[0]['bmaster_id']
		data['data'] = res
		
	else:
		data['status']  = 'failed'
	data['method']='View_cart_items'
	return  str(data)



@api.route('/userremoveproduct',methods=['get','post'])
def userremoveproduct():
	data={}
	
	bchild_ids = request.args['bchild_ids']
	amounts = request.args['amounts']
	bmaster_ids = request.args['bmaster_ids']
 
	q="delete from bookingchild WHERE `bchild_id`='%s'"%(bchild_ids)
	print(q)
	delete(q)
	q="UPDATE `bookingmaster` SET `total`=`total`-'%s' WHERE `bmaster_id`='%s'"%(amounts,bmaster_ids)
	update(q)
	
	data['status']  = 'success'
	data['method']='userremoveproduct'
	return  str(data)



@api.route('/userremoveallproduct',methods=['get','post'])
def userremoveallproduct():
	data={}
	
	login_id = request.args['login_id']
	bmaster_ids = request.args['bmaster_ids']
 
	q="DELETE FROM `bookingmaster` WHERE `user_id`=(SELECT `user_id` FROM users WHERE login_id='%s') AND `status`='Pending'"%(login_id)
	print(q)
	delete(q)
	q="DELETE FROM `bookingchild` WHERE `bmaster_id`='%s'"%(bmaster_ids)
	delete(q)
	
	data['status']  = 'success'
	data['method']='userremoveallproduct'
	return  str(data)


@api.route('/User_payment',methods=['get','post'])
def User_payment():

	data={}
	bmaster_ids=request.args['bmaster_ids']
	amount=request.args['amount']
	

	q="UPDATE `bookingmaster` SET `status`='Paid' WHERE `bmaster_id`='%s'"%(bmaster_ids)
	update(q)
	q="SELECT * FROM `bookingmaster` INNER JOIN `bookingchild` USING(`bmaster_id`) WHERE `bmaster_id`='%s'"%(bmaster_ids)
	res=select(q)
	for row in res:
		q="UPDATE `products` SET `quantity`=`quantity`-'%s' WHERE `product_id`='%s'"%(row['quantity'],row['product_id'])
		update(q)
	q= "INSERT INTO `payment` VALUES(NULL,'%s','%s',CURDATE())"%(bmaster_ids,amount)
	print(q)	
	id=insert(q)
	
	if id>0:
		data['status'] = 'success'
		
	else:
		data['status'] = 'failed'
	data['method'] = 'User_payment'
	return str(data)


@api.route('/View_my_orders',methods=['get','post'])
def View_my_orders():
	data={}

	login_id=request.args['login_id']
	
	q="SELECT *,`payment`.`total` AS ptotal,`payment`.`date` AS pdate,`bookingmaster`.`status` AS pstatus FROM `bookingmaster`  INNER JOIN `payment` on bookingmaster.bmaster_id=payment.bmaster_id WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s') "%(login_id)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='View_my_orders'
	return  str(data)


@api.route('/View_order_products',methods=['get','post'])
def View_order_products():
	data={}
	bmaster_id=request.args['bmaster_id']

	q="SELECT *,`bookingchild`.`quantity` AS bquantity FROM `bookingmaster` INNER JOIN `bookingchild` USING(`bmaster_id`) INNER JOIN `products` USING(`product_id`) INNER JOIN `category` USING(`category_id`) WHERE `bmaster_id`='%s'"%(bmaster_id)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='View_order_products'
	return  str(data)



@api.route('/View_tournament',methods=['get','post'])
def View_tournament():
	data={}

	q="select * from tournament"
	res=select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='View_tournament'
	return  str(data)





@api.route('/User_view_employee',methods=['get','post'])
def User_view_employee():
	data={}

	q="select * from gym_instructor"
	res=select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='User_view_employee'
	return  str(data)



@api.route('/View_users',methods=['get','post'])
def View_users():
	data={}

	q="select * from users"
	res=select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
	else:
		data['status']	= 'failed'
	data['method']='View_users'
	return  str(data)


@api.route('/manageequipments',methods=['get','post'])
def manageequipments():
    data={}
    image=request.files['image'];
    name=request.form['amount'];
    desc=request.form['quantity'];
    quantity=request.form['total'];
    path="static/uploads/"+str(uuid.uuid4())+image.filename
    image.save(path)
    
    q="insert into equipments values(null,'%s','%s','%s','%s')"%(name,desc,path,quantity)
    insert(q)
    
    data['status']='success'
    return str(data)
    

@api.route('/viewspinner')
def viewspinner():
    data={}
    q="select * from equipments"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewspinner'    
    return str(data)


@api.route('/addworkouts')
def addworkouts():
    data={}
    workout=request.args['workout']
    login_id=request.args['login_id']
    tit=request.args['tit']
    desc=request.args['desc']
    ben=request.args['ben']
    eqid=request.args['eq_id']
    
    q="insert into workouts values(null,'%s','%s','%s','%s')"%(eqid,tit,desc,ben)
    insert(q)
    data['status']='success'
    data['method']='workout'
    return str(data)



@api.route('/viewworkouts')
def viewworkouts():
    data={}
    q="select * from workouts inner join equipments using(equipment_id)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewworkouts'    
    return str(data)

@api.route('/viewspinner1')
def viewspinner1():
    data={}
    q="select * from workouts inner join equipments using(equipment_id)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewworkout'    
    return str(data)


@api.route('/viewsusersss')
def viewsusersss():
    data={}
    q="select * from users "
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewsusersss'    
    return str(data)



@api.route('/viewuser_workouts')
def viewuser_workouts():
    data={}
    q="SELECT * FROM user_workouts INNER JOIN users USING(user_id) INNER JOIN workouts USING(workout_id) INNER JOIN `equipments` USING(`equipment_id`)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='viewuser_workouts'    
    return str(data)



@api.route('/user_workouts')
def user_workouts():
    data={}
    days=request.args['days']
    durations=request.args['durations']
    wid=request.args['wid']
    uid=request.args['uid']
    
    
    q="insert into user_workouts values(null,'%s','%s','%s','%s')"%(uid,wid,days,durations)
    insert(q)
    data['status']='success'
    data['method']='user_workouts'
    return str(data)
    
@api.route('/Attendance')
def Attendance():
    data={}
    
    date=request.args['date']
    stime=request.args['stime']
    etime=request.args['date']
    uid=request.args['uid']
    q="insert into attendance values(null,'%s','%s','%s','%s')"%(uid,date,stime,etime)
    insert(q)
    data['status']='success'
    data['method']='addattendence'
    return str(data)


@api.route('/viewatten')
def viewatten():
    data={}
    q="select * from attendance inner join users using(user_id)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
        
    data['method']='viewattendence'
    return str(data)


@api.route('/viewcomplaints')
def viewcomplaints():
    data={}
    q="select * from complaints inner join users using(user_id)"
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
        
    
    return str(data)
    
    
@api.route('/sendreply')
def sendreply():
    data={}
    reply=request.args['reply']
    compid=request.args['compid']
    q="update complaints set reply='%s' where complaint_id='%s'"%(reply,compid)
    update(q)
    data['status']='success'
    return str(data)
    
    

# @api.route('/View_users')
# def View_users():
#     data={}
#     q="select * from users "
#     res=select(q)
#     if res:
#         data['ststus']='success'
#         data['data']=res
#     else:
#         data['status']='failed'
        
    
#     return str(data)


@api.route('/usmessages')
def usmessages():
    data={}
    message=request.args['message']
    uid=request.args['uid']
    log_id=request.args['log_id']
    q="insert into message values(null,'%s',(select physician_id from physician where login_id='%s'),'%s','pending',curdate())"%(uid,log_id,message)
    insert(q)
    data['status']='success'
    data['method']='usmessage'
    return str(data)
    
    
@api.route('/uvmessage/')
def uvmessage():
    data={}
    lid=request.args['log_id']
    uid=request.args['userid']
    q="select * from message where physician_id=(select physician_id from physician where login_id='%s') and user_id='%s'"%(lid,uid)
    print(q)
    res=select(q)
    if res:
        data['status']='success'
        data['data']=res
    else:
        data['status']='failed'
    data['method']='uvmessage'
    return str(data)	



@api.route('/adddiet/')
def adddiet():
    data={}
    diet=request.args['diet']
    days=request.args['days']
    logid=request.args['logid']
    uid=request.args['uid']
    
    q="insert into user_diets values(null,'%s',(select physician_id from physician where login_id='%s'),'%s','%s')"%(uid,logid,diet,days)
    id=insert(q)
    if id:
        data['status']='success'
    else:
        data['status']='failed'
        
    return str(data)





def calculate_bmis(gender, age, height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi




# print(res)


@api.route('/calculate_bmi')
def calculate_bmi():
	data={}
	res=""
	gender=request.args['gender']
	age=int(request.args['age'])
	height=float(request.args['height'])
	weight=float(request.args['weight'])
	bmi = calculate_bmis(gender, age, height, weight)
	try:
		if gender.upper() == "M":
			bmi_range = [(20, 25), (25, 30), (30, 100)]
		else:
			bmi_range = [(19, 24), (24, 29), (29, 100)]

		for i, label in enumerate(['Underweight', 'Normal weight', 'Overweight', 'Obesity']):
			if i == 0:
				if bmi < bmi_range[i][0]:
					res="Your BMI is {:.1f} and you are {}.".format(bmi, label)
					break
			else:
				if bmi >= bmi_range[i-1][1] and bmi < bmi_range[i][1]:
					res="Your BMI is {:.1f} and you are {}.".format(bmi, label)
					break
	except IndexError:
		res="Entered Values are Not Valid"


	data['status']="success"
	data['res']=res
	# data['method']="calculate_bmi"
	return str(data)