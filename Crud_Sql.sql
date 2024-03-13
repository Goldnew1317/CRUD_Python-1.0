create database Crud1
go
use Crud1
go
create table Datos
(
	id int identity(1,1) primary key,
	cedula bigint unique not null,
	nombre varchar(100),
	apellido varchar(100),
	edad int,
)


insert into Datos values
('12345678901','Sergio','Alcantara','46'),
('12341512341','Roberto Carlo','Fernandez','16')
