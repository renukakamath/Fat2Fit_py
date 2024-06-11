/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.27-MariaDB : Database - gym_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gym_management` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci */;

USE `gym_management`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `date` varchar(40) DEFAULT NULL,
  `starting_hour` varchar(50) DEFAULT NULL,
  `ending_hour` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`user_id`,`date`,`starting_hour`,`ending_hour`) values 
(2,1,'2020-01-05','5 pm','8 pm');

/*Table structure for table `batches` */

DROP TABLE IF EXISTS `batches`;

CREATE TABLE `batches` (
  `batch_id` int(11) NOT NULL AUTO_INCREMENT,
  `batch_name` varchar(50) DEFAULT NULL,
  `start_time` varchar(50) DEFAULT NULL,
  `end_time` varchar(50) DEFAULT NULL,
  `instructor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`batch_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `batches` */

insert  into `batches`(`batch_id`,`batch_name`,`start_time`,`end_time`,`instructor_id`) values 
(1,'Morning','00:00:05','00:00:11',1),
(2,'Evening','00:00:03','00:00:09',5);

/*Table structure for table `bookingchild` */

DROP TABLE IF EXISTS `bookingchild`;

CREATE TABLE `bookingchild` (
  `bchild_id` int(11) NOT NULL AUTO_INCREMENT,
  `bmaster_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`bchild_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `bookingchild` */

insert  into `bookingchild`(`bchild_id`,`bmaster_id`,`product_id`,`quantity`,`amount`) values 
(3,2,4,'2','1040.0'),
(4,3,4,'2','1040.0'),
(5,4,4,'02','1040.0');

/*Table structure for table `bookingmaster` */

DROP TABLE IF EXISTS `bookingmaster`;

CREATE TABLE `bookingmaster` (
  `bmaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `total` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`bmaster_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `bookingmaster` */

insert  into `bookingmaster`(`bmaster_id`,`user_id`,`total`,`date`,`status`) values 
(3,2,'1040.0','2023-03-21 21:10:43','Pending'),
(4,3,'1040.0','2023-03-27 20:46:39','Paid');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category`) values 
(4,'fser');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT 'pending',
  `complaint_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`description`,`reply`,`complaint_date`) values 
(1,'1','qwerty11','jgjh','2020-01-17'),
(2,'1','qwerty','qwertyui','2020-01-04'),
(3,'1','weqwsdfgvbn','asdfghj','2020-01-02'),
(4,'2','hello','jsjsjsbdbd','2020-03-20'),
(5,'3','gzuhh','pending','2023-03-27'),
(6,'3','ghbn','pending','2023-03-27');

/*Table structure for table `equipments` */

DROP TABLE IF EXISTS `equipments`;

CREATE TABLE `equipments` (
  `equipment_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `qnty` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`equipment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `equipments` */

insert  into `equipments`(`equipment_id`,`name`,`description`,`image`,`qnty`) values 
(2,'sample1234567','asdfghj','static/img/b9031597-3d3a-4ea1-af72-b7fec3940274Screenshot (1).png',NULL),
(3,'sample','ssss','static/img/127b9e6d-fe09-486c-898f-34c19603c71dcricket-1-700x400.jpg',NULL),
(4,'testing','ddddddd','static/img/f7b83521-46cb-4974-94fb-d6d6113e72de50.jpeg',NULL),
(5,'dudu','shsudu','static/uploads/1afe38a8-48b1-420f-b97f-72292ccfad42abc.jpg','shsusus');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback_description` varchar(200) DEFAULT NULL,
  `feedback_reply` varchar(200) DEFAULT 'pending',
  `feedback_date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback_description`,`feedback_reply`,`feedback_date`) values 
(1,1,'werty','ertgyhj','2020-01-04');

/*Table structure for table `gym_instructor` */

DROP TABLE IF EXISTS `gym_instructor`;

CREATE TABLE `gym_instructor` (
  `instructor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `gfirst_name` varchar(50) DEFAULT NULL,
  `glast_name` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`instructor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `gym_instructor` */

insert  into `gym_instructor`(`instructor_id`,`login_id`,`gfirst_name`,`glast_name`,`age`,`gender`,`phone`,`email`) values 
(1,3,'QWERTY','asdfghj','23','male','0876543','asdfg@sd.com'),
(3,7,'qwerty','wertyu','12','male','1234567','wertyu@dfg.g'),
(4,8,'Francis','Davis','20','male','9447155453','francis@yahoo.com'),
(5,9,'employee','employee','26','male','7594869862','employee@gmail.com'),
(6,11,'wertyu','werty','12','male','12345677777777777777777777','asdfg@df.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin123','admin'),
(2,'s','s','employee'),
(7,'3erty','3456yu','employee'),
(6,'z','qqqqqqqq','physician'),
(8,'frank','1234','employee'),
(9,'emp','emp','employee'),
(10,'sam','sam','user'),
(11,'sdfgh','1234567890','employee'),
(12,'dd','dd','physician'),
(13,'ggg','ggg','user');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `physician_id` int(11) DEFAULT NULL,
  `message_description` varchar(200) DEFAULT NULL,
  `message_reply` varchar(200) DEFAULT 'pending',
  `message_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `message` */

insert  into `message`(`message_id`,`user_id`,`physician_id`,`message_description`,`message_reply`,`message_date`) values 
(1,1,2,'sample','hiiii','2020-01-06'),
(2,3,3,'hiii','pending','2020-03-20'),
(3,3,3,'good','','2023-03-27'),
(4,1,2,'bhahw','pending','2023-04-06'),
(5,1,2,'bhahw','pending','2023-04-06'),
(6,1,2,'mmskd','pending','2023-04-06'),
(7,2,2,'nzndn','pending','2023-04-06');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `bmaster_id` int(11) DEFAULT NULL,
  `total` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`bmaster_id`,`total`,`date`) values 
(2,4,'1040.0','2023-03-27');

/*Table structure for table `payments` */

DROP TABLE IF EXISTS `payments`;

CREATE TABLE `payments` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `payment_for` varchar(50) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `payments` */

insert  into `payments`(`payment_id`,`user_id`,`amount`,`payment_for`,`payment_date`) values 
(1,1,'500','fee','2020-01-03'),
(2,3,'500','Fee','2020-03-20'),
(3,3,'500','Subscription','2020-03-20');

/*Table structure for table `physician` */

DROP TABLE IF EXISTS `physician`;

CREATE TABLE `physician` (
  `physician_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`physician_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `physician` */

insert  into `physician`(`physician_id`,`login_id`,`first_name`,`last_name`,`qualification`,`phone`,`email`) values 
(2,6,'q','a','w','1','q@q.q'),
(3,12,'physician','physician','qwerty','1234567890','physician@gmail.com');

/*Table structure for table `products` */

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `product` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `rate` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `products` */

insert  into `products`(`product_id`,`category_id`,`product`,`quantity`,`rate`,`status`) values 
(4,4,'pp','498','520','Available');

/*Table structure for table `subscription` */

DROP TABLE IF EXISTS `subscription`;

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `physician_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`subscription_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `subscription` */

insert  into `subscription`(`subscription_id`,`user_id`,`physician_id`) values 
(1,1,2),
(2,2,2),
(4,3,3);

/*Table structure for table `tournament` */

DROP TABLE IF EXISTS `tournament`;

CREATE TABLE `tournament` (
  `tournament_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) DEFAULT NULL,
  `place` varchar(500) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`tournament_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `tournament` */

insert  into `tournament`(`tournament_id`,`name`,`place`,`date`,`time`) values 
(1,'Scott Hudson','Repellendus Amet q','27-Sep-2007','Impedit velit error'),
(2,'Scott Hudson','Repellendus Amet q','27-Sep-2007','Impedit velit error');

/*Table structure for table `user_diets` */

DROP TABLE IF EXISTS `user_diets`;

CREATE TABLE `user_diets` (
  `user_diet_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `physician_id` int(11) DEFAULT NULL,
  `diet_details` varchar(100) DEFAULT NULL,
  `diet_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_diet_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `user_diets` */

insert  into `user_diets`(`user_diet_id`,`user_id`,`physician_id`,`diet_details`,`diet_date`) values 
(1,1,6,' sample','1234 days'),
(2,10,6,'sdfghj','10 days'),
(5,3,3,' saaaaaaaaaaaaammmmmmmmmmm','112 days'),
(6,1,2,'ccc','120');

/*Table structure for table `user_workouts` */

DROP TABLE IF EXISTS `user_workouts`;

CREATE TABLE `user_workouts` (
  `user_workout_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `workout_id` int(11) DEFAULT NULL,
  `day` varchar(50) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_workout_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `user_workouts` */

insert  into `user_workouts`(`user_workout_id`,`user_id`,`workout_id`,`day`,`duration`) values 
(1,1,4,'1','2');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `height` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `batch_id` int(11) DEFAULT NULL,
  `payment_status` varchar(50) DEFAULT 'Not Paid',
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`first_name`,`last_name`,`age`,`gender`,`weight`,`height`,`phone`,`email`,`batch_id`,`payment_status`) values 
(1,1,'qwertyu','wertyu','wertyu','Male','12','2','3456','sdf@sd.j',1,'Payment Confirm'),
(2,10,'sam','s','23','Male','57','178','12345678','sdfgh@zxc.com',1,'Payment Confirm'),
(3,13,'ggg','ggg','35','Male','85','189','1236985470','gg@gg.com',1,'Payment Confirm');

/*Table structure for table `workouts` */

DROP TABLE IF EXISTS `workouts`;

CREATE TABLE `workouts` (
  `workout_id` int(11) NOT NULL AUTO_INCREMENT,
  `equipment_id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `benefits` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`workout_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table `workouts` */

insert  into `workouts`(`workout_id`,`equipment_id`,`title`,`description`,`benefits`) values 
(2,2,'sample11111111','eeeeeeeeeeeeee','dddddddddddddd'),
(4,2,'sample123456789','qqqqqqqqqqqqqqqqqqq','wwwwwwwwwwwwww'),
(5,0,'njnjj','bbbcc','jhfgg'),
(6,0,'dddd','dddd','ddddd'),
(7,0,'jjjj','jjjj','jjjj'),
(8,2,'ddd','ddd','dddd');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
