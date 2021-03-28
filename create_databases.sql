drop database if exists pika;
drop user if exists pika;

create database pika;
create user pika with password 'pika' createdb;
grant all privileges on database pika to pika;
