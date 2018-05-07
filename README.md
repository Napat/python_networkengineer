# Python for network engineer

## Outline

### lab1

- โมดูล subprocess เรียกคำสั่งต่างๆของระบบ เช่น ping เพื่อดึง stdout เข้ามาเก็บไว้ในตัวแปรภายในโปรแกรม
- การเขียน Regular Expressions(regex) เพื่อดึงข้อมูลที่ต้องการ
- การค้นหาตำแหน่งของคำที่ต้องการใน string
- โมดูล time ฟังก์ชันด้านเวลา เช่น การจัดรูปแบบ, การหน่วงเวลาโปรแกรม
- โมดูล numpy เบื้องต้นเพื่อช่วยจัดการฟังก์ชันเกี่ยวกับตัวเลข เช่น random ตัวเลขชนิดต่างๆ
- โมดูล pandas ในการจัดการตัวเลขจาก numpy ให้อยู่ในรูปแบบ dataframe เพื่อให้ง่ายต่อการประมวลผล
- โมดูล matplotlib เพื่อนำเอาข้อมูล dataframe มาแสดงผลเป็นกราฟ/รูปภาพ และการทำ animation เพื่ออัปเดทข้อมูลในกราฟที่แสดงผล
- ทดลองใช้ความรู้ที่ได้สร้าง network monitor tool แสดงผลกราฟการ ping ip ปลายทางเป็นกราฟ
- สร้าง "ascii art text" สวยๆด้วย online tool เช่น http://patorjk.com/software/taag/ 

### lab2

- โมดูล paramiko สำหรับการ ssh เข้าไปยังเครื่องปลายทางและเรียกใช้คำสั่งต่างๆ รวมถึงการทำ sftp get()/put() เพื่อ download/upload ไฟล์ไปยังเครื่องปลายทาง
- โมดูล logging เพื่อจัดการ log level (debug/info/warning/error/critical)

### lab3

- โมดูล crassh สำหรับการจัดการอุปกรณ์ cisco ที่ง่ายขึ้นกว่าการเรียกโมดูล paramiko ตรงๆ

### lab4

- การดักจับข้อมูลการ login แบบ Basic authen ด้วย wireshark และการจับข้อมูลการกดปุ่ม FORM ในหน้า web config ของอุปกรณ์
- โมดูล requests เพื่อสั่งยิง HTTP POST METHOD เลียนแบบการกดปุ่ม web config


## Reference

- [Cisco Network Acedemy](https://www.netacad.com/)
