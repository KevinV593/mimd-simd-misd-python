
CREATE DATABASE `prueba_funcion_renal`;

USE `prueba_funcion_renal`;

-- PRIMERA TABLA
CREATE TABLE `registros_pacientes` (
    `id` INT NOT NULL PRIMARY KEY,
    `nombre` VARCHAR(50) NOT NULL,
    `apellido` VARCHAR(50) NOT NULL,
    `edad` INT NOT NULL,
    `sexo` CHAR(1) NOT NULL,
    `altura_cm` DOUBLE NOT NULL,
    `creatinina_mg_dl` DOUBLE NOT NULL,
    `urea_mg_dl` DOUBLE NOT NULL
);

-- SEGUNDA TABLA
CREATE TABLE `resultados_funcion_renal` (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `registro_id` INT NOT NULL,
    `arquitectura` VARCHAR(10) NOT NULL,
    `tfge_ml_min_1_73_m2` DOUBLE NULL,
    `creatinina_umol_l` DOUBLE NULL,
    `urea_mmol_l` DOUBLE NULL
);

-- RELACIÓN ENTRE LAS TABLAS
ALTER TABLE `resultados_funcion_renal`
ADD CONSTRAINT `fk_resultados_registros`
FOREIGN KEY (`registro_id`)
REFERENCES `registros_pacientes` (`id`);
