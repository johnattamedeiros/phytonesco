# phytonesco
Phytonesco é uma rest api em python, apenas para estudos



## INSTALL
```bash
pip install psycopg2 
pip install flask flask-jsonpify flask-sqlalchemy flask-restful

## BEFORE RUN
Install postgres

SQLS PRE PROJECT

```bash
CREATE SCHEMA tasks AUTHORIZATION postgres;

CREATE TABLE tasks.task (
	id serial4 NOT NULL,
	description varchar NULL,
	status bpchar(1) NOT NULL,
	CONSTRAINT task_pk PRIMARY KEY (id)
);

## TO RUN
```bash
flask --app main.py --debug run


