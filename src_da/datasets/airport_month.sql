create database lect;  
use lect;  
create table t_airport_month (
	reg_month	varchar(7),
	Gimpo	int,
	Gimhae	int,
	Jeju	int,
	Cheongju	int,
	Incheon	int
);

insert into t_airport_month values 
('2020.01', 2077132, 1394866, 2612063, 258155, 6309369),
('2020.02', 1230157, 667932, 1325440, 115798, 3381632),
('2020.03', 813378, 243471, 979490, 76001, 609516),
('2020.04', 849988, 265298, 1045784, 75899, 153514),
('2020.05', 1241164, 432974, 1616998, 153132, 137924)