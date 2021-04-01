import sys
import psycopg2
import unittest

class ModifyValuesTest(unittest.TestCase):
    def test_write(self):
        compare = [("1", "CoolioCat56", "20"), ("2", "Natures-RPG", "10"), ("3", "JulesTheCat", "15")]
        check = write_values()
        self.assertRaises(Exception)
        self.assertNotEqual(check, compare)

    def test_change(self):
        compare = [("1", "CoolioCat56", "50"), ("2", "Natures-RPG", "10"), ("3", "JulesTheCat", "15")]
        check = modify_values()
        self.assertRaises(Exception)
        self.assertNotEqual(check, compare)

    def test_delete(self):
        compare = [("1", "CoolioCat56", "50"), ("2", "Natures-RPG", "10")]
        check = delete_values()
        self.assertRaises(Exception)
        self.assertNotEqual(check, compare)

print("Please enter password:")
keyword = input()
try:
    con = psycopg2.connect(dbname="dfkhicfte5npdp", user="mcrhzpfvlfjgka", password=keyword, host="ec2-3-224-251-47.compute-1.amazonaws.com")
    cur = con.cursor()

except:
    print("Login failed\nInvalid Password")
    sys.exit()

def read_values():
    cur.execute("SELECT USER_ID, USERNAME, LEVEL FROM ACCOUNT")
    con.commit()
    rows = cur.fetchall()
    return rows

def write_values():
    cur.execute("INSERT INTO ACCOUNT(USER_ID, USERNAME, LEVEL) VALUES(1, 'CoolioCat56', 20);")
    cur.execute("INSERT INTO ACCOUNT(USER_ID, USERNAME, LEVEL) VALUES(2, 'Natures-RPG', 10);")
    cur.execute("INSERT INTO ACCOUNT(USER_ID, USERNAME, LEVEL) VALUES(3, 'JulesTheCat', 15);")
    con.commit()
    return read_values()

def modify_values():
    cur.execute("UPDATE ACCOUNT set LEVEL = 50 WHERE USER_ID = 1;")
    con.commit()
    return read_values()

def delete_values():
    cur.execute("DELETE from ACCOUNT where USERNAME='JulesTheCat';")
    con.commit()
    return read_values()

def clean_db():
    cur.execute("DROP TABLE IF EXISTS Account")
    cur.execute("""CREATE TABLE IF NOT EXISTS ACCOUNT (
	USER_ID INT PRIMARY KEY NOT NULL,
    USERNAME CHAR(20) NOT NULL,
    LEVEL INT NOT NULL
    );""")
    con.commit()

if __name__ == '__main__':
    clean_db()
    unittest.main()
    con.close()