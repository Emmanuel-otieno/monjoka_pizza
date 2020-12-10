# monjoka_pizza

## Instalation
* python3.6 -m venv virtual
* pip install flask
* pip install flask-SQLAlchemy
* pip install flask-mysql
* pip install psycopg2-binary
* pip install flask-bootstrap
* pip install flask-wtf
* pip install flask-script
* python3.6 -m  pip install gunicorn

## DATABASE
* $ psql
psql (9.5.8)
Type "help" for help.

moringa=# 

* moringa=# CREATE DATABASE pizza;

##  DATABASE-URL
 * SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/pizza'


## Creating MySQL Table

* CREATE TABLE `order` (
	`id` int unsigned NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`price` double NOT NULL,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;


## Dumping Data

* INSERT INTO `order` (`id`, `name`, `price`) VALUES
(1, 'large pizza', 'AMTR01', 12000.00),
(2, 'middiam pizza', 'USB02', 600.00),
(3, 'Small pizza', 350.00),
(4, 'cheez', 400.00),
(5, 'beef', 500.00),
(6, 'veggys', 300.00),
(7, 'pork', 500.00),
(8, 'chilly hot',  400.00);