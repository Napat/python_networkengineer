# โปรแกรมการเชื่อต่อบนระบบเครือข่าย

## Lab11

ภาษา python สามารถใช้ module subprocess เพื่อเรียกใช้งาน command ต่างๆของระบบเช่น ping ได้
หากต้องการผลลัพธ์จากการรันโปรแกรม สามารถใส่ parameter `stdout=subprocess.PIPE`
เพื่อเก็บผลลัพธ์ที่ได้จากการรันคำสั่งจะถูกเก็บไว้ใน stdout

ข้อจำกัดเบื้องต้น จะสามารถรันได้แค่ตำสั่งเดียว ไม่สามารถรันหลายๆคำสั่งและส่งต่อกันได้เช่น

``` cmd
windows> netstat -an | findstr "ESTABLISHED"
linux> netstat -an | grep "ESTABLISHED"
```
