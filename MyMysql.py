import MySQLdb
from sae.const import (MYSQL_HOST,MYSQL_HOST_S,MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB)
from flask import g


def con():
	g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB, port=int(MYSQL_PORT))
	g.db.cursor()