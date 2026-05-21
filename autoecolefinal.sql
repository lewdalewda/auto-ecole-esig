--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS auto;

CREATE DATABASE auto CHARACTER SET 'utf8';

USE auto;

--
-- Création des tables :
--

CREATE TABLE eleve (
	elv_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	elv_nom VARCHAR(30) NOT NULL,
	elv_prenom VARCHAR(30) NOT NULL,
	elv_age int(100),
	elv_heuresfts int(30),
	elv_heuresrest int(30),
	elv_boite bool,
    PRIMARY KEY (elv_id)
)
ENGINE=INNODB;


CREATE TABLE prof (
	pro_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	pro_nom VARCHAR(30) NOT NULL,
    pro_prenom VARCHAR(30) NOT NULL,
	pro_age int(100),
	pro_heurescas int(30),
	pro_heureslbr int(30),
	PRIMARY KEY (pro_id)
)
ENGINE=INNODB;


CREATE TABLE voiture(
	car_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	car_nom VARCHAR(30) NOT NULL,
	car_annee int,
	car_capa int,
	car_km int,
    car_hpw int,
    car_lstd INT UNSIGNED NOT NULL,
    car_boite bool,
	PRIMARY KEY (car_id)
)
ENGINE=INNODB;


CREATE TABLE heures (
	hr_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	hr_date DATE,
	hr_duree INT,
	hr_elv INT UNSIGNED NOT NULL,
	hr_prof INT UNSIGNED NOT NULL,
	hr_car INT UNSIGNED NOT NULL,
    hr_km INT,
	hr_depart timestamp,
	hr_fin timestamp,
	hr_boite bool,
    hr_passee bool,
	PRIMARY KEY (hr_id)
)
ENGINE=INNODB;



--
-- Insertion de valeurs dans les tables :
--

INSERT INTO eleve
VALUES	(1, 'COLE', 'Thea', 19, 30, 0, 0),
	(2, 'MONCONDUIT', 'Octavie', 19, 15, 15, 0),
	(3, 'DELGADO', 'Antonio', 50, 0,30, 1),
	(4, 'GOUGNAF', 'Jules', 5, 1,29,1);
	


INSERT INTO prof	
VALUES	(1, 'LEBEC', 'Nathan', 19, 20, 5),
	(2, 'GAUDEAU', 'Arthur', 20, 15, 10);
    
	


INSERT INTO voiture
VALUES	(10, 'Porshe GT3-RS', 2024, 300, 1000, 525, 1, 1),
	(20, 'Poshe 944', 1990, 250, 520, 220, 3, 0),
	(30, 'Mazda Miata mx-9', 1995, 150, 2500, 181, 2, 0);
	
	


INSERT INTO heures
VALUES	(1, '2026-04-01', 2, 1, 1, 10, 50, '2026-04-01 16:30', '2026-04-01 18:30', 1, 0),
	(2, '2026-04-02', 1, 2, 1, 10, 20, '2026-04-02 13:00', '2026-04-01 14:00', 1, 0),
	(3, '2026-04-03', 2.5, 1, 2, 20, 65, '2026-04-03 09:00', '2026-04-03 11:30', 0, 0),
	(4, '2026-03-26', 2, 2, 1, 30, 50, '2026-03-26 13:00', '2026-03-26 15:00', 0, 1);
	


-- 
-- Requêtes :
--


select *
from eleve







