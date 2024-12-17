-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 158.179.221.250    Database: AcademiaDB
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cursos`
--

DROP TABLE IF EXISTS `Cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cursos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio_mensual` float NOT NULL,
  `descripcion` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cursos`
--

LOCK TABLES `Cursos` WRITE;
/*!40000 ALTER TABLE `Cursos` DISABLE KEYS */;
INSERT INTO `Cursos` VALUES (1,'Matemáticas',100,'Curso avanzado de álgebra y análisis matemático'),(2,'Física',200,'Curso de fundamentos de física');
/*!40000 ALTER TABLE `Cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Estudiantes`
--

DROP TABLE IF EXISTS `Estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Estudiantes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `estudiante_correo` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estudiantes`
--

LOCK TABLES `Estudiantes` WRITE;
/*!40000 ALTER TABLE `Estudiantes` DISABLE KEYS */;
INSERT INTO `Estudiantes` VALUES (1,'Pedro Sanchez','pedroSanchez@gmail.com'),(2,'Mariano Rajoy','marianoRajoy@gmail.com');
/*!40000 ALTER TABLE `Estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Matriculas`
--

DROP TABLE IF EXISTS `Matriculas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Matriculas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `estudiante_id` int NOT NULL,
  `curso_id` int NOT NULL,
  `calificacion` float DEFAULT NULL,
  `fecha_matricula` date NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `matricula_estudiante_id` (`estudiante_id`),
  KEY `matricula_curso_id` (`curso_id`),
  CONSTRAINT `Matriculas_ibfk_1` FOREIGN KEY (`estudiante_id`) REFERENCES `Estudiantes` (`id`),
  CONSTRAINT `Matriculas_ibfk_2` FOREIGN KEY (`curso_id`) REFERENCES `Cursos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Matriculas`
--

LOCK TABLES `Matriculas` WRITE;
/*!40000 ALTER TABLE `Matriculas` DISABLE KEYS */;
INSERT INTO `Matriculas` VALUES (1,1,1,5,'2024-12-17','2024-06-15','2024-12-15');
/*!40000 ALTER TABLE `Matriculas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-17 17:17:19
