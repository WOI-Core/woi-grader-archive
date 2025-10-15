# เจแปนกับลูกธนูเพลิง (Fire Arrows)

<br>
เจแปน... เด็กหนุ่มผู้โชคร้าย เขาถูกลากมายังลานประลองของเทพแห่งการลงทัณฑ์เพื่อเข้ารับการทดสอบปัญญา
<br><br>
เทพยื่นข้อเสนอให้เจแปนตอบคำถามเพื่อเอาชีวิตรอด โดยมีคำถามอยู่ว่า:
<br><br>
**&quot;ในกลุ่มคนหนึ่งกลุ่ม จะต้องมีคนอย่างน้อยที่สุดกี่คน เพื่อให้ความน่าจะเป็นที่จะมีคนเกิดวันเดียวกัน (ไม่สนใจปีเกิด) อย่างน้อยหนึ่งคู่ มีค่าไม่น้อยกว่า $P$?&quot;**
<br><br>
เทพได้กล่าวทิ้งท้ายไว้ว่า &quot;หากเจ้าตอบผิดแม้แต่คนเดียว ลูกธนูไฟจะพุ่งเข้าใส่เจ้าตามจำนวนที่ตอบผิดไป จงตอบให้ดีล่ะ มนุษย์เอ๋ย...&quot;
<br><br>
แน่นอนว่าเจแปนไม่อยากโดนลูกธนูไฟ เขาจึงต้องหันมาพึ่งคุณซึ่งเป็นโปรแกรมเมอร์ที่เก่งที่สุดในโลกให้ช่วยเขียนโปรแกรมหาคำตอบที่ถูกต้องเพื่อเอาชีวิตรอด!
<br><br>
(สมมติว่า 1 ปีมี 365 วัน และโอกาสเกิดในแต่ละวันเท่ากันทั้งหมด)

<div style="page-break-after: always;"></div>

## Input :

มีทั้งหมด $1$ บรรทัด

รับจำนวนจริง $1$ จำนวน ได้แก่ $P$ แทนความน่าจะเป็นที่เจแปนต้องการ

## Output :

มี $1$ บรรทัด คือ จำนวนเต็มของจำนวนคนที่น้อยที่สุด ที่ทำให้ความน่าจะเป็นที่จะมีคนเกิดวันเดียวกันอย่างน้อยหนึ่งคู่มีค่าไม่น้อยกว่า $P$

## Examples :

### ตัวอย่างที่ 1

<table width="100%" cellspacing="0" cellpadding="0" style="border-collapse: collapse;"\>
<tr align="center"\>
<th style="padding: 5px;">ข้อมูลนำเข้า</th>
<th style="padding: 5px;">ข้อมูลส่งออก</th>
</tr>
<tr\>
<td width="50%" style="vertical-align:top; padding: 1; margin: 0;"\>
<pre style="background-color: transparent; border: 0; margin: 0; padding: 0;"\>
0.5
</pre\>
</td\>
<td style="vertical-align:top; padding: 1; margin: 0;"\>
<pre style="background-color: transparent; border: 0; margin: 0; padding: 0;"\>
23
</pre\>
</td\>
</tr>
</table>

### ตัวอย่างที่ 2

<table width="100%" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="center">
<th style="padding: 5px;">ข้อมูลนำเข้า</th>
<th style="padding: 5px;">ข้อมูลส่งออก</th>
</tr\>
<tr>
<td width="50%" style="vertical-align:top; padding: 1; margin: 0;">
<pre style="background-color: transparent; border: 0; margin: 0; padding: 0;">
0.75
</pre>
</td>
<td style="vertical-align:top; padding: 1; margin: 0;">
<pre style="background-color: transparent; border: 0; margin: 0; padding: 0;">
32
</pre>
</td>
</tr>
</table>

### ตัวอย่างที่ 3

<table width="100%" cellspacing="0" cellpadding="0" style="border-collapse: collapse;">
<tr align="center">
<th style="padding: 5px;">ข้อมูลนำเข้า</th>
<th style="padding: 5px;">ข้อมูลส่งออก</th>
</tr>
<tr>
<td width="50%" style="vertical-align:top; padding: 1; margin: 0;">
<pre style="background-color: transparent; border: 0; margin: 0; padding: 0;">
0.9
</pre>
</td>
<td style="vertical-align:top; padding: 1; margin: 0;">
<pre style="background-color: transparent; border: 0; margin: 0; padding: 0;">
41
</pre>
</td>
</tr>
</table>

<div style="page-break-after: always;"></div>

## คำอธิบายตัวอย่างที่ 1

เมื่อมีคนในห้อง 23 คน ความน่าจะเป็นที่จะมีคนเกิดวันเดียวกันอย่างน้อยหนึ่งคู่จะมีค่าประมาณ 0.507 ซึ่งมากกว่า 0.5 เป็นครั้งแรก ดังนั้นคำตอบคือ 23

## Constraints :

  - $0 \le P \le 1$

## Subtasks :

1.  (100 points) ไม่มีเงื่อนไขเพิ่มเติม

## Limits :

  - Time limit: 1 seconds
  - Memory limit: 256 MB

## Author :

  - ผู้ออกโจทย์ : ธีร์ เหมจินดา
  - *** โจทย์เหล่านี้จัดทำขึ้นเพื่อการพัฒนาผู้ที่มีความสนใจด้าน Competitive Programming อนุญาตให้มีการนำไปใช้ในด้านการศึกษา หากมีข้อผิดพลาดหรือข้อสงสัย สามารถติดต่อสอบถามผู้ออกโจทย์เพื่อที่จะปรับปรุงแก้ไขโจทย์ต่อไป \*\*\*

## Contacts :
* Github : xHexlabx 
* Facebook : ธีร์ เหมจินดา
* Instagram : hextex.ipynb