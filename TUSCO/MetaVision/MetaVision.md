
# Meta Vision

<center><image src="https://firebasestorage.googleapis.com/v0/b/task-pdf-writer.appspot.com/o/assets%2Ff4c1914f-ee50-4786-a399-d8d81cf30c3d.jpeg?alt=media&token=e58ed23a-5d03-46ed-be96-c3e57ef4503d" style="width:80%"></center>

<br>ขณะคุณกำลังอยู่ในแมตช์ฟุตบอลสุดดุเดือด <br>
โดยตำแหน่งของคุณคือกองกลางและลูกบอลอยู่ที่เท้าคุณในวินาทีที่ $0$ <br><br>
ในวินาทีที่ $1$ 
คุณสามารถเลือกได้ว่าจะส่งบอลให้เพื่อนร่วมทีมหรือเลี้ยงบอลต่อเองอีก $1$ วินาที <br><br>
ถ้าคุณเลือกส่งบอลให้เพื่อนร่วมทีม เพื่อนร่วมทีมจะเลี้ยงบอลต่ออย่างน้อย $1$ วินาที แล้วเลือกระหว่างเลี้ยงบอลต่ออีก $1$ วินาที หรือส่งบอลให้คนอื่นเช่นกัน <br><br>
จากสุดยอดทักษะในการอ่านเกมของคุณทำให้คุณสามารถรู้ได้ในทันทีว่าในวินาทีที่ $N$ จะมีผู้เล่นที่มีโอกาสได้ลูกบอลมากที่สุดกี่คน(รวมตัวคุณเองด้วย) <br><br>
เนื่องจากสนามฟุตบอลนี้อาจมีผู้เล่นในแต่ละทีมมากกว่า $11$ คน และอาจมีจำนวณมหาศาลมากๆ จึงให้ตอบด้วยเศษเหลือจากการหารจำนวณผู้เล่นด้วย $10^9+7$

## Input :
มีทั้งหมด $1$ บรรทัด

รับจำนวนเต็ม $1$ จำนวน ได้แก่ $N$ แทนวินาทีที่คุณต้องการรู้จำนวณผู้เล่นที่มีโอกาสได้ลูกบอลมากที่สุด (รวมตัวคุณเองด้วย)

## Output :

มี $1$ บรรทัด คือ เศษเหลือจากการหารจำนวณผู้เล่นที่มีโอกาสได้ลูกบอลมากที่สุด (รวมตัวคุณเองด้วย) ด้วย $10^9+7$
  

## Examples :



### ตัวอย่างที่ 1

<table  width="100%"  cellspacing="0"  cellpadding="0"  style="border-collapse: collapse;">

<tr  align="center">

<th  style="padding: 5px;">ข้อมูลนำเข้า</th>

<th  style="padding: 5px;">ข้อมูลส่งออก</th>

</tr>

<tr>

<td  width="50%"  style="vertical-align:top; padding: 1; margin: 0;">

<pre  style="background-color: transparent; border: 0; margin: 0; padding: 0;">

4

</pre>

</td>

<td  style="vertical-align:top; padding: 1; margin: 0;">

<pre  style="background-color: transparent; border: 0; margin: 0; padding: 0;">

5

</pre>

</td>

</tr>

</table>

### ตัวอย่างที่ 2

<table  width="100%"  cellspacing="0"  cellpadding="0"  style="border-collapse: collapse;">

<tr  align="center">

<th  style="padding: 5px;">ข้อมูลนำเข้า</th>

<th  style="padding: 5px;">ข้อมูลส่งออก</th>

</tr>

<tr>

<td  width="50%"  style="vertical-align:top; padding: 1; margin: 0;">

<pre  style="background-color: transparent; border: 0; margin: 0; padding: 0;">

5

</pre>

</td>

<td  style="vertical-align:top; padding: 1; margin: 0;">

<pre  style="background-color: transparent; border: 0; margin: 0; padding: 0;">

8

</pre>

</td>

</tr>

</table>

### ตัวอย่างที่ 3

<table  width="100%"  cellspacing="0"  cellpadding="0"  style="border-collapse: collapse;">

<tr  align="center">

<th  style="padding: 5px;">ข้อมูลนำเข้า</th>

<th  style="padding: 5px;">ข้อมูลส่งออก</th>

</tr>

<tr>

<td  width="50%"  style="vertical-align:top; padding: 1; margin: 0;">

<pre  style="background-color: transparent; border: 0; margin: 0; padding: 0;">

20

</pre>

</td>

<td  style="vertical-align:top; padding: 1; margin: 0;">

<pre  style="background-color: transparent; border: 0; margin: 0; padding: 0;">

10946

</pre>

</td>

</tr>

</table>

## คำอธิบายตัวอย่างที่ 1
<center><image src="https://firebasestorage.googleapis.com/v0/b/task-pdf-writer.appspot.com/o/assets%2F769eec44-3de8-4382-b72c-6bd04623cdcc.png?alt=media&token=4fdfe030-8094-4565-bb75-8da81ed77a8d" style="width:80%"></center>

## Constraints :
- $0 ≤ N ≤ 1,000,000$

## Subtasks :

  1. (100 points) ไม่มีเงื่อนไขเพิ่มเติม

## Limits :

- Time limit: 1 seconds
- Memory limit: 256 MB

## Author :

* ผู้ออกโจทย์ : ธนัท สมุทฐา ( NineSama )

*  *** โจทย์เหล่านี้จัดทำขึ้นเพื่อการพัฒนาผู้ที่มีความสนใจด้าน Competitive Programming อนุญาตให้มีการนำไปใช้ในด้านการศึกษา หากมีข้อผิดพลาดหรือข้อสงสัย สามารถติดต่อสอบถามผู้ออกโจทย์เพื่อที่จะปรับปรุงแก้ไขโจทย์ต่อไป ***

  

## Contacts :

* Github : Tanat Samuttha

* Facebook : ธนัท สมุทฐา

* Instagram : nine.nsm