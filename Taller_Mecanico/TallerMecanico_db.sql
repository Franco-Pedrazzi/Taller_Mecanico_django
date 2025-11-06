DROP DATABASE IF EXISTS `TallerMecanico`;
CREATE DATABASE `TallerMecanico`;
USE `TallerMecanico`;

CREATE TABLE `Persona` (
  `dni` varchar(10) PRIMARY KEY NOT NULL,
  `nombre` varchar(10) NOT NULL,
  `apellido` varchar(10) NOT NULL,
  `tel` varchar(10),
  `dir` varchar(25)
);

CREATE TABLE `Cliente` (
  `cod_cliente` int PRIMARY KEY auto_increment,
  `dni_cliente` varchar(10)  NOT NULL
);

CREATE TABLE `Empleado` (
  `legajo` int auto_increment PRIMARY KEY,
  `dni_empleado` varchar(10) NOT NULL
);

CREATE TABLE `Provedor` (
  `cod_Provedor` int auto_increment PRIMARY KEY,
  `dni_Provedor` varchar(10)  NOT NULL
);


alter table Cliente
add index Fk_dni_cliente (`dni_cliente`);

alter table Cliente
add constraint Fk_dni_cliente
foreign key (`dni_cliente`)
    references Persona (`dni`)
    ON DELETE CASCADE
    on update cascade;

alter table Empleado
add index Fk_dni_empleado (`dni_empleado`);

alter table Empleado
add constraint Fk_dni_empleado
foreign key (`dni_empleado`)
    references Persona (`dni`)
    ON DELETE CASCADE
    on update cascade;

CREATE TABLE `Vehiculo` (
  `matricula` varchar(10) PRIMARY KEY,
  `color` varchar(10),
  `modelo` varchar(10),
  `dni_cliente` varchar(10) ,
   FOREIGN KEY (dni_cliente) REFERENCES Persona(dni) ON DELETE CASCADE
);



CREATE TABLE `Repuesto` (
  `nombre` varchar(25) PRIMARY KEY,
  `precio_x_unidad` float,
  `cantidad` int
);

CREATE TABLE `Reparaciones` (
  `id` int auto_increment PRIMARY KEY,
  `fecha_entrada` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `matricula_vehiculo` varchar(25),
  FOREIGN KEY (`matricula_vehiculo`) REFERENCES `Vehiculo` (`matricula`) ON DELETE CASCADE
);

CREATE TABLE `detalle_Reparacion` (
  `id` int auto_increment PRIMARY KEY,
  `legajo` INT,
  `repuesto` varchar(25),
  `reparacion_id` int,
  `cantidad` int,
  `Precio` float,
  FOREIGN KEY (`legajo`) REFERENCES `Empleado` (`legajo`) ON DELETE CASCADE, 
  FOREIGN KEY (`repuesto`) REFERENCES `Repuesto` (`nombre`) ON DELETE CASCADE,
  FOREIGN KEY (`reparacion_id`) REFERENCES `Reparaciones` (`id`) ON DELETE CASCADE
);

CREATE TABLE `Ficha_Tecnica` (
  `id_FT` int auto_increment primary Key,
  `Vehiculo_Matricula` varchar(10),
  `nroEmpleados` int,
  `subtotal`float,
  `mano_de_obra`float,
  `total`float,
  FOREIGN KEY (`Vehiculo_Matricula`) REFERENCES `Vehiculo` (`matricula`) ON DELETE CASCADE
);
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL UNIQUE,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL PRIMARY KEY,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
);

insert into Persona values(1,"Name","LastName","12","12");
insert into Empleado values (1,1);
INSERT INTO `auth_user` 
(`password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`)
VALUES
-- usuario administrador
('pbkdf2_sha256$1000000$CrI1sYOXoG3cmrhp6fL6Av$7AsEvNpFxeGtHJdZ/rpgPu6Jg3RyrcZiIxItVgyHE3s=', NOW(), 1, 'admin', 'Administrador', 'General', 'admin@example.com', 1, 1, NOW()),

-- usuario normal
('pbkdf2_sha256$1000000$CrI1sYOXoG3cmrhp6fL6Av$7AsEvNpFxeGtHJdZ/rpgPu6Jg3RyrcZiIxItVgyHE3s=', NOW(), 0, 'robert', 'Robert', 'Smith', 'robert@example.com', 0, 1, NOW()),

-- otro usuario activo sin permisos
('pbkdf2_sha256$1000000$CrI1sYOXoG3cmrhp6fL6Av$7AsEvNpFxeGtHJdZ/rpgPu6Jg3RyrcZiIxItVgyHE3s=', NOW(), 0, '1', 'Francisco', 'López', 'fran@example.com', 0, 1, NOW());

