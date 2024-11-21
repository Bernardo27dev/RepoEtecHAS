create database petshop

use petshop
create table petshop(
	id int identity primary key,
	tipo_pet varchar(30),
	nome_pet varchar(30),
	idade int
);
select * from petshop
use master
DROP DATABASE petshop


create database teste

use teste
create table petshop(
	id int identity primary key,
	tipo_pet varchar(30),
	nome_pet varchar(30),
	idade int
);
select * from petshop