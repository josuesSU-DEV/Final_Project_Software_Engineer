create database TIF;
use TIF;
create table Usuario(
	id integer primary key,
    nombre varchar(30),
    apellido varchar(30),
    correo varchar(30) unique
);

create table Asistente(
	id integer primary key,
    foreign key (id) references Usuario(id)
);

create table Ponente(
	id integer primary key,
	numEvento integer,
    foreign key (id) references Usuario(id)
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
    detalles varchar(100),
    link varchar(30),
    primary key(idEvento,idPonente,idLista),
    foreign key (idPonente) references Ponente(id),
    foreign key (idLista) references Lista(idLista)
);

create table Asiste(
	idAsistente integer,
    idEvento integer,
    primary key (idAsistente,idEvento),
    foreign key (idAsistente) references Asistente(id),
    foreign key (idEvento) references Evento(idEvento)
);


