//Creando nuestra base de datos
CREATE SCHEMA `t.inter` ;

//Creando tabla de usuario
CREATE TABLE `t.inter`.`login` (
  `cui` INT NOT NULL,
  `contrasenia` VARCHAR(45) NULL,
  PRIMARY KEY (`cui`));


//Creando tabla de usuarios
CREATE TABLE `t.inter`.`usuarios` (
  `cui` INT NOT NULL,
  `nombres` VARCHAR(45) NULL,
  `apellidos` VARCHAR(45) NULL,
  `escuela` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `imagen` VARCHAR(45) NULL,
  PRIMARY KEY (`cui`));
  
//Creando tabla de cursos de estudiante
CREATE TABLE `t.inter`.`curso del estudiante` (
  `cui` INT NOT NULL,
  `curso1` VARCHAR(45) NULL,
  `curso2` VARCHAR(45) NULL,
  `curso3` VARCHAR(45) NULL,
  `curso4` VARCHAR(45) NULL,
  `curso5` VARCHAR(45) NULL,
  PRIMARY KEY (`cui`));

//Creando tabla de escuela
CREATE TABLE `t.inter`.`escuela` (
  `idEscuela` INT NOT NULL,
  `escuela` VARCHAR(45) NULL,
  `anio` INT NULL,
  `numero_estudiantes` VARCHAR(45) NULL,
  PRIMARY KEY (`idEscuela`));