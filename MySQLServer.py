#!/usr/bin/python3
import mysql.connector

try:
    # الاتصال بالسيرفر
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password_here"
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # إنشاء قاعدة البيانات لو مش موجودة
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
