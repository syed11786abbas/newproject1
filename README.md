# newproject11. Download and install Python 2.7 in C drive.

2. Download and extract OpenCV 2.13.4

3. Download and install SQLite 3.1.1

4. Open the OpenCV extracted folder goto build > python > 2.7 > x86, copy the cv2.pyd file
	and paste it into C: > python27 > Lib > site-packages

5. Download and Add numPY library:
	open cmd and type: cd c:/python27/scripts (press enter)
		then type: pip install numpy (press enter, make sure your internet is working)

6. Download and Add Pillow library:
		open cmd and type: cd c:/python27/scripts (press enter)
		then type: pip install pillow (press enter, make sure your internet is working)

7. Make sure there is "FireBase" named database in the project folder, if not create database named "FireBase" using SQLite
	and make a table "People" with "ID" as integer attribute and "Name" as character attribute in the table.

8. Now open the login.py file, enter "cse" as username and "integral" as password.

9. Now, first register the face, then train it, and finally recognise it.
