# โปรแกรมการเชื่อต่อบนระบบเครือข่าย

``` cmd
# python autocomplete module for python console
py -m pip install ipython pyreadline
```

## Lab1_1

ภาษา python สามารถใช้ module subprocess เพื่อเรียกใช้งาน command ต่างๆของระบบเช่น ping ได้
หากต้องการผลลัพธ์จากการรันโปรแกรม สามารถใส่ parameter `stdout=subprocess.PIPE`
เพื่อเก็บผลลัพธ์ที่ได้จากการรันคำสั่งจะถูกเก็บไว้ใน stdout

ข้อจำกัดเบื้องต้น จะสามารถรันได้แค่ตำสั่งเดียว ไม่สามารถรันหลายๆคำสั่งและส่งต่อกันได้เช่น

``` cmd
windows> netstat -an | findstr "ESTABLISHED"
linux> netstat -an | grep "ESTABLISHED"
```

ข้อความ String สามารถใช้ .find() เพื่อค้นหา*ตำแหน่ง*ของคำที่ต้องการได้ เช่น

``` python
arr = "hello world"
type(arr)           # <class 'str'>
arr.find("world")   # ุ6
arr.find("banana")   # -1
```

## Lab1_2

- การตัดคำบรรทัดสุดท้าย
- การใช้งาน regex เพื่อค้นหาตัวเลขทั้งหมดที่อยู่ในบรรทัดนั้นๆที่ตรงตาม pattern โดย

`\d` หมายถึงตัวเลขใดๆ  
`+` หมายถึงมีได้หลายๆตัว  
`\d+.\d+` หมายถึงตัวเลขที่มีทศนิยมกี่ตำแหน่งก็ได้ (ถ้าไม่มีทศนิยมเลยจะไม่ match กับกฏข้อนี้นะ) 

- การใช้งาน module เวลาเพื่อแสดงผลวันที่หรือใช้หน่วงเวลาการทำงาน

## Lab1_3

เป็นการ simmulate ค่าโดยอาศัยโมดูล numpy เพื่อ random ตัวเลขและเก็บค่า(append) ใส่ใน list เก็บเอาไว้ และวนลูปแสดงผลออกมาแบบ text mode

## Lab1_4

ตัวอย่างการใช้งาน pandas เพื่อจำลองข้อมูลเริ่มต้นที่ 11:00 สิ้นสุดที่ 11:20 โดยให้ step ทุกๆ 5 นาที
```
ts = pd.date_range("11:00", "11:20", freq="5min")
```
จากนั้นจึงสร้าง dataframe ของข้อมูลขึ้นมาและทดสอบฟังก์ชันต่างๆของโมดูล pandas 

## Lab1_5

เป็นตัวอย่างการสร้าง animation chart โดยการเรียก function ที่ทำการอัปเดทรูปทุกๆคาบเวลาใดๆโดยอาศัย function จากโมดูล matplotlib ในการ plot รูปร่วมกับข้อมูล dataframe จากโมดูล pandas

## Workshop1

โปรแกรม ping plotter จะทำการ ping server แล้วนำเอาค่า min, max, average มา plot และแสดงผลเป็น animation โดยจะอัปเดทรูปทุกๆหนึ่งหน่วยเวลา
