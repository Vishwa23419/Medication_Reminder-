# Medication_Reminder-
Medication Reminder is a simple Python program that lets users add medicines, view the list, and check missed or upcoming doses. It uses functions, lists, and user input with a menu-driven interface. <br>

1.Overview<br>

This is a Python program that helps users keep track of medicines and their scheduled times. It works in the terminal and stores data only while the program is running.<br>

2.Structure<br>

The program uses four main functions:<br>
add_med() – Adds a medicine and its time<br>
view_med() – Shows all added medicines<br>
check_due() – Checks if a dose is missed or upcoming<br>
med_menu() – Displays the menu and handles user choices<br>
All data is stored in a simple list called med_list.<br>

3.Data Format<br>

Medicines are stored as:<br>
["Medicine Name", "HH:MM"]<br>
Example:<br>
["Paracetamol", "09:00"]<br>

4.How It Works<br>

User opens the program<br>
A menu appears<br>
User can add, view, or check medicines<br>
Time is compared as strings (e.g., "14:00" > "09:00")<br>
Program runs until the user selects "Back"<br>

5.Limitations<br>
No real notifications<br>
Works only with correct HH:MM input<br>
