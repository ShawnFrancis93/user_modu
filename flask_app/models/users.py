from flask_app.config.mysqlconnection import  connectToMySQL

class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def show_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_crud').query_db(query)
        users = []
        for k in results:
            users.append(cls(k))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW())"
        
        return connectToMySQL('user_crud').query_db(query,data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL('user_crud').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('user_crud').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('user_crud').query_db(query, data)
    