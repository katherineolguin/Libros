-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_libros_
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_libros_
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_libros_` DEFAULT CHARACTER SET utf8 ;
USE `esquema_libros_` ;

-- -----------------------------------------------------
-- Table `esquema_libros_`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros_`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `UPDATED_AT` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros_`.`libros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros_`.`libros` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NULL,
  `numero_de_paginas` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_libros_`.`favoritos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_libros_`.`favoritos` (
  `usuario_id` INT NOT NULL,
  `libro_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `libro_id`),
  INDEX `fk_usuarios_has_libros_libros1_idx` (`libro_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_libros_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_libros_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `esquema_libros_`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_libros_libros1`
    FOREIGN KEY (`libro_id`)
    REFERENCES `esquema_libros_`.`libros` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
