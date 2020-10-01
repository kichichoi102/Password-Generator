# Password Generator
 Inspired from Google Autofill Password generator

Introduction:
When you make a new account in most trusted websites, Google Chrome detects that you are doing so, and suggests a "strong password". However, I personally don't trust Google's privacy rules, but want strong passwords at the same time, so I decided to make my own. To do so, I have configured upper and lower letters, numbers from 0-9, and characters including: !,@,#,$,%,^,&,*,-,=,+.

intro():
The program asks for the desired length of your password.

randomChar():
Brute forced through random fxn to achieve nearly absolute randomness. To do so, I randomly assigned numbers to upper, lower, num, and char, and made sure their numbers added up to your desired length. If it did not, this function would repeat until it was the case. 

passGen():
Using the number assigned for these cases, I assigned random item from its respective files, and appended to the "password". Changed the format into a list. Then, I shuffled the order of this string of characters. To finalize, I joined the shuffled characters, and printed into the terminal.

Future updates/work:
-Save the passwords and print them on a seperate note file.
-Make this into a chrome extension, so only it will auto fill the passwords.
-Give user options to add and/or omit certain characters.

Conclusion:
Not really a hard concept, troubles arouse from formatting and error handling.
