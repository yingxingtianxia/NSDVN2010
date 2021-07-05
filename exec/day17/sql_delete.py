#!/usr/bin/env python
import pyconn

conn = pyconn.pyconn()
curses = conn.cursor()

sql_delete = "delete from mytb where id=%d"
curses.execute(sql_delete % (9))
conn.commit()
curses.close()
conn.close()