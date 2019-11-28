-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: shanzhaimusic
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.18.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add user',7,'add_user'),(20,'Can change user',7,'change_user'),(21,'Can delete user',7,'delete_user'),(22,'Can add person_diary',8,'add_person_diary'),(23,'Can change person_diary',8,'change_person_diary'),(24,'Can delete person_diary',8,'delete_person_diary'),(25,'Can add person_photo',9,'add_person_photo'),(26,'Can change person_photo',9,'change_person_photo'),(27,'Can delete person_photo',9,'delete_person_photo'),(28,'Can add music',10,'add_music'),(29,'Can change music',10,'change_music'),(30,'Can delete music',10,'delete_music'),(31,'Can add discuss',11,'add_discuss'),(32,'Can change discuss',11,'change_discuss'),(33,'Can delete discuss',11,'delete_discuss'),(34,'Can add 音乐人',12,'add_musician'),(35,'Can change 音乐人',12,'change_musician'),(36,'Can delete 音乐人',12,'delete_musician');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$iFgfFcsKUP8Q$mJaMbdECR2eRrfSkYufcDwNL/6uS8UMmBL2siCLu7rA=','2019-11-22 07:23:54.513512',1,'zhangda','','','',1,1,'2019-11-21 13:23:59.894064'),(2,'pbkdf2_sha256$36000$PRr6JbZZ3qij$TwaX4dru3AQc91BopEwzEBi/34NzdoJ8tti2H19Gb3k=','2019-11-23 05:51:29.010793',1,'123','','','',1,1,'2019-11-23 05:49:23.695052');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discuss_discuss`
--

DROP TABLE IF EXISTS `discuss_discuss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discuss_discuss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `music_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  `parent_id` int(11) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `discuss_discuss_music_id_id_663a02de` (`music_id_id`),
  KEY `discuss_discuss_user_id_id_94649d6d` (`user_id_id`),
  CONSTRAINT `discuss_discuss_music_id_id_663a02de_fk_music_music_id` FOREIGN KEY (`music_id_id`) REFERENCES `music_music` (`id`),
  CONSTRAINT `discuss_discuss_user_id_id_94649d6d_fk_users_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discuss_discuss`
--

LOCK TABLES `discuss_discuss` WRITE;
/*!40000 ALTER TABLE `discuss_discuss` DISABLE KEYS */;
INSERT INTO `discuss_discuss` VALUES (1,'123',1,1,0,'2019-11-22 07:36:48.403824'),(2,'123',1,1,0,'2019-11-22 07:36:56.120970'),(3,'123',1,1,0,'2019-11-22 07:38:54.016154'),(4,'123',1,1,0,'2019-11-22 07:41:15.616590'),(5,'546',2,1,0,'2019-11-22 08:16:20.889576'),(6,'567',2,1,0,'2019-11-22 08:18:20.934389'),(7,'457',1,1,0,'2019-11-22 08:20:18.524271'),(8,'如啼眼5',3,1,0,'2019-11-22 09:41:17.719637'),(9,'76i78o',3,1,8,'2019-11-22 09:41:23.941862'),(10,'klkllkljk',1,2,0,'2019-11-22 09:45:48.466539'),(11,'yuhjjk',1,2,7,'2019-11-22 09:45:55.852208'),(12,'787',4,1,0,'2019-11-24 00:42:26.384502'),(13,'ukuyil',4,1,12,'2019-11-24 00:42:43.240833'),(14,'546',4,1,0,'2019-11-24 00:45:41.685478'),(15,'9809878',4,1,0,'2019-11-24 00:46:05.518394'),(16,'098',4,1,0,'2019-11-24 00:47:29.731001'),(17,'7',4,1,0,'2019-11-24 00:47:59.712819');
/*!40000 ALTER TABLE `discuss_discuss` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-11-22 07:25:00.324668','1','Music object',1,'[{\"added\": {}}]',10,1),(2,'2019-11-22 07:25:42.518520','2','Music object',1,'[{\"added\": {}}]',10,1),(3,'2019-11-22 07:30:34.630742','2','Music object',2,'[{\"changed\": {\"fields\": [\"music_name\"]}}]',10,1),(4,'2019-11-22 07:30:40.723025','1','Music object',2,'[{\"changed\": {\"fields\": [\"music_name\"]}}]',10,1),(5,'2019-11-22 08:23:39.087582','2','Music object',2,'[{\"changed\": {\"fields\": [\"music_name\"]}}]',10,1),(6,'2019-11-22 08:23:43.688829','1','Music object',2,'[{\"changed\": {\"fields\": [\"music_name\"]}}]',10,1),(7,'2019-11-22 09:23:19.561089','3','Music object',1,'[{\"added\": {}}]',10,1),(8,'2019-11-22 09:24:36.059170','4','Music object',1,'[{\"added\": {}}]',10,1),(9,'2019-11-22 09:25:30.853463','5','Music object',1,'[{\"added\": {}}]',10,1),(10,'2019-11-22 09:26:00.140126','6','Music object',1,'[{\"added\": {}}]',10,1),(11,'2019-11-22 09:26:29.825185','7','Music object',1,'[{\"added\": {}}]',10,1),(12,'2019-11-22 09:26:57.791832','8','Music object',1,'[{\"added\": {}}]',10,1),(13,'2019-11-22 09:27:32.647297','9','Music object',1,'[{\"added\": {}}]',10,1),(14,'2019-11-22 09:27:59.603488','10','Music object',1,'[{\"added\": {}}]',10,1),(15,'2019-11-22 12:48:39.439237','1','<刘德华>',1,'[{\"added\": {}}]',12,1),(16,'2019-11-22 12:49:39.314330','2','<刘若英>',1,'[{\"added\": {}}]',12,1),(17,'2019-11-22 12:51:14.931557','3','<张靓颖>',1,'[{\"added\": {}}]',12,1),(18,'2019-11-22 12:52:38.141128','4','<张杰>',1,'[{\"added\": {}}]',12,1),(19,'2019-11-22 12:54:01.406178','5','<李荣浩>',1,'[{\"added\": {}}]',12,1),(20,'2019-11-22 12:55:06.281164','6','<林俊杰>',1,'[{\"added\": {}}]',12,1),(21,'2019-11-22 12:56:21.133033','7','<王力宏>',1,'[{\"added\": {}}]',12,1),(22,'2019-11-22 12:57:46.506122','8','<谭维维>',1,'[{\"added\": {}}]',12,1),(23,'2019-11-22 12:59:15.974816','9','<韩红>',1,'[{\"added\": {}}]',12,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'discuss','discuss'),(10,'music','music'),(12,'musician','musician'),(8,'person','person_diary'),(9,'person','person_photo'),(6,'sessions','session'),(7,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-11-21 13:16:43.889308'),(2,'auth','0001_initial','2019-11-21 13:16:54.847669'),(3,'admin','0001_initial','2019-11-21 13:16:57.096773'),(4,'admin','0002_logentry_remove_auto_add','2019-11-21 13:16:57.249531'),(5,'contenttypes','0002_remove_content_type_name','2019-11-21 13:16:58.597266'),(6,'auth','0002_alter_permission_name_max_length','2019-11-21 13:16:59.446119'),(7,'auth','0003_alter_user_email_max_length','2019-11-21 13:17:00.433582'),(8,'auth','0004_alter_user_username_opts','2019-11-21 13:17:00.497114'),(9,'auth','0005_alter_user_last_login_null','2019-11-21 13:17:01.159473'),(10,'auth','0006_require_contenttypes_0002','2019-11-21 13:17:01.201668'),(11,'auth','0007_alter_validators_add_error_messages','2019-11-21 13:17:01.294376'),(12,'auth','0008_alter_user_username_max_length','2019-11-21 13:17:03.467369'),(13,'users','0001_initial','2019-11-21 13:17:04.108133'),(14,'music','0001_initial','2019-11-21 13:17:04.530213'),(15,'discuss','0001_initial','2019-11-21 13:17:06.969678'),(16,'discuss','0002_discuss_parent_id','2019-11-21 13:17:07.883090'),(17,'discuss','0003_auto_20191109_1106','2019-11-21 13:17:11.448211'),(18,'discuss','0004_discuss_created_time','2019-11-21 13:17:12.271686'),(19,'music','0002_music_discuss_user','2019-11-21 13:17:15.429142'),(20,'music','0003_auto_20191121_2029','2019-11-21 13:17:15.546754'),(21,'music','0004_auto_20191121_2032','2019-11-21 13:17:15.606335'),(22,'musician','0001_initial','2019-11-21 13:17:16.035837'),(23,'musician','0002_auto_20191114_1858','2019-11-21 13:17:16.085798'),(24,'users','0002_user_info','2019-11-21 13:17:16.917726'),(25,'person','0001_initial','2019-11-21 13:17:19.963941'),(26,'sessions','0001_initial','2019-11-21 13:17:20.664340');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2sin4gvvgkf2xxt3xqwp2ou5oxw3fgq8','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:23.134767'),('5wme9l4x34vxwr4u5mxktr4a1a0b5ffi','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:23.325034'),('638kpn0omgpj077axftigvw80yllvh0d','NzdhZTIyOTNkNzI3MzAyMDMxNmFhYjY5ZjdlZDliYWU5MDExZWZiNTp7fQ==','2019-12-07 04:28:29.592035'),('a9ml3xg77g2re6ulojyb2uwfl8ifrk6v','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:23.508135'),('dkuziup3j62qnt9bqq66s6iqc6hazyi0','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:22.920817'),('hfjxljuxxzf8wm1c6jhorcnlis4truh1','MGVlNjcyMzA1OGExZTI3Zjk4ZDA5YjIxZjE5YzdkZGI0NGZkNTk1Mjp7InVzZXJuYW1lIjoiMTIzIiwiX2F1dGhfdXNlcl9pZCI6IjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjBkM2E3YzRkOTZkMmI0MWE3MWE5YTY3YzdkZWM5NjkyZmYyZmViYTMifQ==','2019-12-07 05:51:29.069897'),('i8f1e7aut2dlwlwsfxmpp4puai8vdtrr','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-08 00:32:07.467895'),('lqfkmtxcnox9p6wzpna95i8fx07pp4v4','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:22.681381'),('mz7cwrtkf98uelp0wymg04r8ua8tyw6u','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-06 12:27:31.144542'),('nmgkxy0xhm2b170oucqu2ciaapnlbpfn','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:18:23.744744'),('p298yl14lbj52pbss3pm4vpqt648as6f','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:23.760025'),('tkgpmpmmksem2lt2l024yy9nast5923a','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:24.120551'),('wuztccugbwoj56y5zlgubxmhst20bu8v','ZWJlMDE5OWJmNjUyMWVjNTc0OGU3Y2MwMWM2YjIxYWQ1ZWE0NDE4Yzp7InVzZXJuYW1lIjoiMTIzIn0=','2019-12-05 13:22:23.917090'),('xqa1wmb3mz5p0ads5w5jc1x7u53ehpuw','ODAyZmJjZWNkNTNkMDEzNTBlODY1YzY5Yzk0ZDdkZGNmZTQyZmJmOTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5NTg2MDBlMjY5ZTgxYTY1MjI5Y2ZjNDRhZDc4M2E3MjYwNmQxYTY0IiwidXNlcm5hbWUiOiI3ODkifQ==','2019-12-06 10:20:28.634111');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `music_music`
--

DROP TABLE IF EXISTS `music_music`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `music_music` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `music_name` varchar(64) NOT NULL,
  `singer` varchar(24) NOT NULL,
  `music_dir` varchar(128) NOT NULL,
  `kind` varchar(8) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `music_music`
--

LOCK TABLES `music_music` WRITE;
/*!40000 ALTER TABLE `music_music` DISABLE KEYS */;
INSERT INTO `music_music` VALUES (1,'爱你一万年','刘德华','music/刘德华-爱你一万年.mp3','流行'),(2,'为爱痴狂','刘若英','music/刘若英-为爱痴狂.mp3','流行'),(3,'寂寞才说爱','刘可','music/刘可-寂寞才说爱.mp3','流行'),(4,'一曲相思','半阳','music/半阳-一曲相思.mp3','电子'),(5,'燕归巢','张靓颖,张杰','music/张靓颖、张杰-燕归巢.mp3','民谣'),(6,'老街','李荣浩','music/李荣浩-老街.mp3','爵士'),(7,'世间美好与你环环相扣','松柏','music/松柏-世间美好与你环环相扣.mp3','民谣'),(8,'曹操','林俊杰','music/曹操-林俊杰.mp3','摇滚'),(9,'缘分一道桥','王力宏,谭维维','music/王力宏,谭维维-缘分一道桥.mp3','电子'),(10,'飞云之下','韩红,林俊杰','music/韩红、林俊杰-飞云之下.mp3','电子');
/*!40000 ALTER TABLE `music_music` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `music_music_discuss_user`
--

DROP TABLE IF EXISTS `music_music_discuss_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `music_music_discuss_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `music_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `music_music_discuss_user_music_id_user_id_5270f69f_uniq` (`music_id`,`user_id`),
  KEY `music_music_discuss_user_user_id_241218a4_fk_users_user_id` (`user_id`),
  CONSTRAINT `music_music_discuss_user_music_id_931009a8_fk_music_music_id` FOREIGN KEY (`music_id`) REFERENCES `music_music` (`id`),
  CONSTRAINT `music_music_discuss_user_user_id_241218a4_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `music_music_discuss_user`
--

LOCK TABLES `music_music_discuss_user` WRITE;
/*!40000 ALTER TABLE `music_music_discuss_user` DISABLE KEYS */;
INSERT INTO `music_music_discuss_user` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,1),(9,9,1),(10,10,1);
/*!40000 ALTER TABLE `music_music_discuss_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `musician`
--

DROP TABLE IF EXISTS `musician`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `musician` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `musician` varchar(10) NOT NULL,
  `music_name` varchar(6) NOT NULL,
  `music` varchar(100) NOT NULL,
  `style` int(11) NOT NULL,
  `picture` varchar(100) NOT NULL,
  `like` int(11) NOT NULL,
  `addtime` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `musician`
--

LOCK TABLES `musician` WRITE;
/*!40000 ALTER TABLE `musician` DISABLE KEYS */;
INSERT INTO `musician` VALUES (1,'刘德华','爱你一万年','static/images/刘德华-爱你一万年.mp3',1,'static/images/刘德华.jpg',1212,'2019-11-22 12:48:39.434773'),(2,'刘若英','为爱痴狂','static/images/刘若英-为爱痴狂.mp3',2,'static/images/刘若英.jpg',1145,'2019-11-22 12:49:39.311498'),(3,'张靓颖','燕归巢','static/images/张靓颖张杰-燕归巢.mp3',3,'static/images/张靓颖.jpg',1148,'2019-11-22 12:51:14.930185'),(4,'张杰','燕归巢','static/images/张靓颖张杰-燕归巢_lozHmBk.mp3',4,'static/images/张杰.jpg',2453,'2019-11-22 12:52:38.140433'),(5,'李荣浩','老街','static/images/李荣浩-老街.mp3',5,'static/images/李荣浩.jpg',2356,'2019-11-22 12:54:01.404613'),(6,'林俊杰','曹操','static/images/林俊杰-曹操.mp3',6,'static/images/林俊杰.jpg',4586,'2019-11-22 12:55:06.279941'),(7,'王力宏','缘分一道桥','static/images/王力宏谭维维-缘分一道桥.mp3',1,'static/images/王力宏.jpg',2586,'2019-11-22 12:56:21.130802'),(8,'谭维维','缘分一道桥','static/images/王力宏谭维维-缘分一道桥_icpy9or.mp3',2,'static/images/谭维维.jpeg',7412,'2019-11-22 12:57:46.498210'),(9,'韩红','飞云之下','static/images/韩红林俊杰-飞云之下.mp3',4,'static/images/韩红.jpg',1234,'2019-11-22 12:59:15.974150');
/*!40000 ALTER TABLE `musician` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person_diary`
--

DROP TABLE IF EXISTS `person_diary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person_diary` (
  `diary_id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`diary_id`),
  KEY `person_diary_user_id_id_de203f8f_fk_users_user_id` (`user_id_id`),
  CONSTRAINT `person_diary_user_id_id_de203f8f_fk_users_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person_diary`
--

LOCK TABLES `person_diary` WRITE;
/*!40000 ALTER TABLE `person_diary` DISABLE KEYS */;
INSERT INTO `person_diary` VALUES (1,'开始日记按到的发挥也亏了的方法很苦;哦;','2019-11-21 13:18:37.176276',1),(2,'开始日记ltkhoth','2019-11-22 10:00:43.159414',2),(3,'123','2019-11-22 10:20:41.765568',3),(4,'开始日记76565454','2019-11-22 10:25:02.123905',3),(5,'324','2019-11-22 10:25:13.150100',3),(6,'开始日记oigfhiojrhoihhgk','2019-11-22 13:18:13.577507',1);
/*!40000 ALTER TABLE `person_diary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person_photo`
--

DROP TABLE IF EXISTS `person_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person_photo` (
  `photo_id` int(11) NOT NULL AUTO_INCREMENT,
  `avatar` varchar(100) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`photo_id`),
  KEY `person_photo_user_id_id_bbf45ffe_fk_users_user_id` (`user_id_id`),
  CONSTRAINT `person_photo_user_id_id_bbf45ffe_fk_users_user_id` FOREIGN KEY (`user_id_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person_photo`
--

LOCK TABLES `person_photo` WRITE;
/*!40000 ALTER TABLE `person_photo` DISABLE KEYS */;
INSERT INTO `person_photo` VALUES (1,'avatar/timg.jpeg',1),(2,'avatar/358a4fb6041b3e9612da6a8b04011d9c.jpg',3);
/*!40000 ALTER TABLE `person_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(24) NOT NULL,
  `password` varchar(24) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `info` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'123','123','2019-11-22 13:21:29.416104','123的签名'),(2,'456','456','2019-11-22 09:45:23.416174',''),(3,'789','789','2019-11-22 10:20:21.790146','');
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-24  9:02:05
