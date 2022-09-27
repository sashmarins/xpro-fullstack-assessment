import mysql.connector

con = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database="Sasha_Marinskiy"
)

cur = con.cursor()

# print("creating clients table")
# cur.execute(
# "    CREATE TABLE Clients ( "
# "    ID INT NOT NULL AUTO_INCREMENT, "
# "    COMPANY_NAME varchar(30) NOT NULL, "
# "    PRIMARY KEY (ID))"
# )
# print("done creating clients table")

# print("creating users table")
# cur.execute(
# '''CREATE TABLE Users (
#     ID INT NOT NULL AUTO_INCREMENT,
#     LAST_NAME varchar(30) NOT NULL,
#     FIRST_NAME varchar(30) NOT NULL,
#     USERNAME varchar(30) NOT NULL,
#     ROLE varchar(9) NOT NULL,
#     PHONE varchar(15),
#     ADDRESS varchar(30),
#     CLIENT_ID INT NOT NULL,
#     FOREIGN KEY (CLIENT_ID) REFERENCES Clients(ID),
#     PRIMARY KEY (ID))'''
#     )
# print("done creating users table")

# print("inserting clients")
# cur.execute('''INSERT INTO Clients (COMPANY_NAME)
# VALUES ("Meshuggah")'''
# )
# cur.execute('''INSERT INTO Clients (COMPANY_NAME)
# VALUES ("Animals As Leaders")'''
# )
# cur.execute('''INSERT INTO Clients (COMPANY_NAME)
#  VALUES ("Admins")'''
# )
# print("done inserting clients")

# print("creating users for Meshuggah")
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Haake",
#     "Tomas",
#     "tomashaake17",
#     "Client",
#     "888-012-3444",
#     "100 Royals Street",
#     1
# )'''
# )
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Kidman",
#     "Jens",
#     "meshugaahsinger44",
#     "User",
#     "111-111-2314",
#     "32 Combustion Avenue",
#     1
# )'''
# )
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Thordendal",
#     "Fredrik",
#     "riffmonster7",
#     "User",
#     "123-456-7890",
#     "491 Koloss Street",
#     1
# )'''
# )
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Hagström",
#     "Mårten",
#     "martenhag18",
#     "User",
#     "000-111-1234",
#     "10 Obzen Road",
#     1
# )'''
# )
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Lövgren",
#     "Richard",
#     "probassist7",
#     "User",
#     "123-123-1234",
#     "500 Water Lane",
#     1
# )'''
# )
# print("done creating users for meshuggah")

# print("creating users for Animals as leaders")
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Abasi",
#     "Tosin",
#     "LeaderOfAnimals",
#     "Client",
#     "000-000-0000",
#     "000 Cafo Road",
#     2
# )'''
# )
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Reyes",
#     "Javier",
#     "javireyes11",
#     "User",
#     "111-111-1111",
#     "111 Impulse Avenue",
#     2
# )'''
# )
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Garstka",
#     "Matt",
#     "djentleman99",
#     "User",
#     "222-222-2222",
#     "222 Soraya Lane",
#     2
# )'''
# )
# print("done creating users for animals as leaders")

# print("Creating Super Users")
# cur.execute('''INSERT INTO Users (LAST_NAME, FIRST_NAME, USERNAME, ROLE, PHONE, ADDRESS, CLIENT_ID)
# VALUES (
#     "Marinskiy",
#     "Sasha",
#     "sashmarins",
#     "Admin",
#     "813-573-3519",
#     "10123 Parley Drive",
#     3
# )'''
# )
# print("done creating super users")

con.commit()