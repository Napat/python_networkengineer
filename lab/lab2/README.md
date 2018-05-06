# Automate backup database

## Lab2_1

ทดสอบใช้งาน paramiko ในการทำ ssh, sftp 

## Lab2_2

sftp get()/put() file

## Lab2_3

การใช้งาน logging module จัดการ log level ซึ่งมีอยู่ 5 ระดับ
1.DEBUG
2.INFO
3.WARNING
4.ERROR
5.CRITICAL
สามารถตั้งค่า api python ให้ write log เฉพาะ level ที่สูงกว่าที่กำหนดได้ด้วย

``` python
logger.setLevel(logging.WARNING)
```

ก็จะ write เฉพาะ log file เฉพาะ log ที่มี level สูงกว่าหรือเท่ากับ WARNING ได้แก่ logger.warning(), logger.error() และ logger.critical()

## Workshop2

โปรแกรม ssh เข้าสู่ server แล้วคอยสำรองฐานข้อมูลของระบบ (backup database) ในแต่ละวัน โดยตั้งชื่อไฟล์ในรูปแบบ YearMonthDate.sql และเก็บ log การทำงานของโปรแกรมเช่่น login สำเร็จหรือไม่ เป็นต้น


