from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(cls, data):
        query = "INSERT INTO email (email, created_at, updated_at) VALUES(%(email)s, NOW(), NOW());"
        results = connectToMySQL("email_validation_schema").query_db(query, data)

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM email ORDER BY id DESC;"
        results = connectToMySQL("email_validation_schema").query_db(query)
        email = []
        for row in results:
            email.append(cls(row))
        return email

    @staticmethod
    def validate_email(thisispain):
        is_valid = True
        if not EMAIL_REGEX.match(thisispain['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid