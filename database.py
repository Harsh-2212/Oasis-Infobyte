import sqlite3
from matplotlib import pyplot as plt

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return format(bmi, ".2f")

def create_tables():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS BMI_Data (
                 full_name TEXT,
                 age INTEGER,
                 height_cm REAL,
                 weight_kg REAL,
                 bmi_result REAL
                 )''')
    conn.commit()
    c.close()
    conn.close()

def create_histogram():
    conn = sqlite3.connect('bmi_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, bmi_result FROM BMI_Data")
    data = cursor.fetchall()

    usernames = [row[0] for row in data]
    bmi_scores = [row[1] for row in data]

    plt.bar(usernames, bmi_scores, color='skyblue', edgecolor='black')
    plt.xlabel('Username')
    plt.ylabel('BMI Score')
    plt.title('BMI Scores of Users')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    conn.commit()
    conn.close()

def insert_data(full_name, age, height, weight, bmi_result):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO BMI_Data (full_name, age, height_cm, weight_kg, bmi_result) VALUES (?, ?, ?, ?, ?)",
              (full_name, age, height, weight, bmi_result))
    conn.commit()
    c.close()
    conn.close()

create_tables()