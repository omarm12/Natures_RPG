import psycopg2

keyword = input("Please enter password: ")
con = psycopg2.connect(database="dfkhicfte5npdp", user="mcrhzpfvlfjgka", password=keyword, host="ec2-3-224-251-47.compute-1.amazonaws.com")
print("Database connected successfully")

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Account;")
print("Table dropped (if it existed)")

cur.execute("""CREATE TABLE ACCOUNT (
	USER_ID INT PRIMARY KEY NOT NULL,
    USERNAME CHAR(20) NOT NULL,
    LEVEL INT NOT NULL
);""")

con.commit()
print("Table created successfully")

cur.execute("INSERT INTO ACCOUNT(USER_ID, USERNAME, LEVEL) VALUES(1, 'CoolioCat56', 20);")
cur.execute("INSERT INTO ACCOUNT(USER_ID, USERNAME, LEVEL) VALUES(2, 'Natures-RPG', 10);")
cur.execute("INSERT INTO ACCOUNT(USER_ID, USERNAME, LEVEL) VALUES(3, 'JulesTheCat', 15);")

con.commit()
print("Data inserted successfully")

cur.execute("SELECT USER_ID, USERNAME, LEVEL FROM ACCOUNT")
rows = cur.fetchall()

for row in rows:
    print("USER_ID =", row[0])
    print("USERNAME =", row[1])
    print("LEVEL =", row[2])
    print("\n")

print("Data pulled successfully")

cur.execute("UPDATE ACCOUNT set LEVEL = 50 WHERE USER_ID = 1;")
con.commit()
print("Total updated rows:", cur.rowcount)

cur.execute("SELECT USER_ID, USERNAME, LEVEL from ACCOUNT;")
rows = cur.fetchall()
for row in rows:
    print("USER_ID =", row[0])
    print("USERNAME =", row[1])
    print("LEVEL =", row[2])
    print("\n")

cur.execute("DELETE from ACCOUNT where USERNAME='JulesTheCat';")
con.commit()

print("Total deleted rows:", cur.rowcount)
cur.execute("SELECT USER_ID, USERNAME, LEVEL FROM ACCOUNT;")
rows = cur.fetchall()
for row in rows:
    print("USER_ID =", row[0])
    print("USERNAME =", row[1])
    print("LEVEL =", row[2])
    print("\n")

con.close()