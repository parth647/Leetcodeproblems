

SQL ONE IN ALL COMMAND LIST

# I want to ~select~ delete all the duplicate emails in my database 

1. Self Join on where emails are equal 
2. condition : where id1>id2

DELETE P1 FROM PERSON AS P1,PERSON AS P2 WHERE P1.EMAIL = P2.EMAIL AND P1.ID>P2.ID



# show the ids where the temperature on the next day was more than the temp on prev day

1. self Join
2. condition where date is greater than prev date by 1 (use dateadd function) and tempareture is greater than prev day
