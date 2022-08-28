drop database if exists TIF;
create database TIF;
use TIF;

/*
drop table ponente;
drop table asistente;
drop table usuario;
drop table lista;	
drop table evento;
drop table asiste;
drop table listevento;
*/

create table Usuario(
	idUsuario integer primary key,
    nombre varchar(30),
    apellido varchar(30),
    correo varchar(30) unique
);

create table Asistente(
	idAsistente integer primary key,
    foreign key (idAsistente) references Usuario(idUsuario)
);

create table Ponente(
	idPonente integer primary key,
	numEvento integer,
	descripcion varchar(100),
    foreign key (idPonente) references Usuario(idUsuario)
);

create table Tema(
	idTema integer primary key,
	nombre varchar(30)
);

create table Lista(
	idLista integer primary key,
    cantidad integer
);

create table listEvento(
	idListaEvento integer primary key,
    nombre varchar(30),
    foreign key (idListaEvento) references Lista(idLista)
);

create table Evento(
	idEvento integer,
    idPonente integer,
    idLista integer,
    nombre varchar(30),
    detalles varchar(200),
    link varchar(30),
	idTema integer,
    primary key(idEvento,idPonente,idLista),
    foreign key (idPonente) references Ponente(idPonente),
    foreign key (idLista) references Lista(idLista)
);

create table Asiste(
	idAsistente integer,
    idEvento integer,
    primary key (idAsistente,idEvento),
    foreign key (idAsistente) references Asistente(idAsistente),
    foreign key (idEvento) references Evento(idEvento)
);

show tables;

drop procedure if exists insertarPonente;
Delimiter $$
create procedure insertarPonente(
in id integer,
in nombre varchar(30),
in apellido varchar(30),
in correo varchar(30),
in numEvento integer,
in descripcion varchar(100))
begin
	if (select exists (select 1 from ponente where ponente.idPonente = id))then
		select 'Ponente ya existe!';
    else
		if (select exists (select 1 from usuario where usuario.idUsuario = id))then
			insert into ponente values(id,numEvento);
		else
			insert into usuario values(id,nombre,apellido,correo);
			insert into ponente values(id,numEvento,descripcion);
		end if;
	end if;
end$$
Delimiter ;

drop procedure if exists insertarAsistente;
Delimiter $$
create procedure insertarAsistente(
in id integer,
in nombre varchar(30),
in apellido varchar(30),
in correo varchar(30))
begin
	if (select exists (select 1 from asistente where asistente.idAsistente = id))then
		select 'Asistente ya existe!';
    else
		if (select exists (select 1 from usuario where usuario.idUsuario = id))then
			insert into asistente values(id);
		else
			insert into usuario values(id,nombre,apellido,correo);
			insert into asistente values(id);
		end if;
	end if;
end$$
Delimiter ;

drop procedure if exists listaEvento;
Delimiter $$
create procedure listaEvento(
in id integer,
in cantidad integer)
begin
	if (select exists (select 1 from lista where lista.idLista = id))then
    select 'Lista ya existe!';
    else 
		insert into lista values(id,cantidad);
	end if;
end$$
Delimiter ;

drop procedure if exists insertarEvento;
Delimiter $$
create procedure insertarEvento(
in id integer,
in idPonente integer,
in idLista integer,
in nombre varchar(30),
in detalles varchar(100),
in link varchar(30),
in idTema integer)
begin
	if (select exists (select 1 from evento where evento.idEvento = id))then
    select 'Evento ya existe ya existe!';
    else 
		insert into evento values(id,idPonente,idLista,nombre,detalles,link,idTema);
	end if;
end$$
Delimiter ;

drop procedure if exists asiste;
Delimiter $$
create procedure asiste(
in idAsistente integer,
in idEvento integer)
begin
	if (select exists (select 1 from evento where evento.idEvento = idEvento))then
		if(select exists (select 1 from asistente where asistente.idAsistente = idAsistente))then
			insert into asiste values(idAsistente,idEvento);
		end if;
    else 
		select 'No existe evento o usuario(asistente)!';
	end if;
end$$
Delimiter ;

/*Insertar Ponente*/
call insertarPonente(1,"Josue","Sumare","JosueS@gmail.com",1,'pipipipipipipipipi');
call insertarPonente(2,"Moises","Casaverde","MoisesC@gmail.com",2,'pipipipipipipipipi');
call insertarPonente(3,"Levi","Castillon","LeviC@gmail.com",3,'pipipipipipipipipi');
call insertarPonente(4,"Samuel","Chambi","SamuelC@gmail.com",4,"pipipipipipipipipi");

/*Insertar Asistentes*/
call insertarAsistente(4,"Samuel","Chambi","SamuelC@gmail.com");
call insertarAsistente(5,"Alejandro","Villa","AlejandroV@gmail.com");
call insertarAsistente(6,"Julio","Yauri","JulioY@gmail.com");


/*Insertar lista Evento*/
call listaEvento(1,150);
call listaEvento(2,150);
call listaEvento(3,150);
insert into listevento values(1,"Biologia");
insert into listevento values(2,"Ciencia");
insert into listevento values(3,"Psicologia");

/*Insertar Evento*/
call insertarEvento(1,1,1,"Biologia","seres vivos","https//:Bilogia.com",1);
call insertarEvento(2,2,2,"Ciencia","tecnologia","https//:Ciencia.com",2);
call insertarEvento(3,3,3,"Psicologia","el comportamiento humano","https//:Psicologia.com",3);

/*Insertar si un asistente asiste a un evento*/
call asiste(4,1);
call asiste(5,2);
call asiste(6,3);

select * from asistente;
select * from ponente;
select * from usuario;

