// Abstraction means hiding complex implementation details and showing only the necessary features of an object. It can be achieved using abstract classes and interfaces (pure virtual functions in C++).
// An abstract class in C++ is a class that contains at least one pure virtual function, which makes it incomplete and non-instantiable (you can't create objects of it directly). But apart from that, it can contain a wide variety of members.
// abstract class can contain Pure virtual functions(definitely), regular (concreate) member function, data members(variables), constructor, destructor, static function and static members but it can't instantiate directly. 

#include <iostream>
using namespace std;

// A class becomes abstract when it has at least one pure virtual function.
class AbstractDatabase {
public:
    // Pure virtual functions (must be implemented by derived classes)
    virtual void connect() = 0; // pure virtual function
    virtual void disconnect() = 0;
    virtual bool executeQuery(const string& query) = 0;
    
    // Concrete method that uses the abstract operations
    void performTransaction(const string& query) {
        connect();
        bool success = executeQuery(query);
        if (success) {
            cout << "Transaction successful" << endl;
        } else {
            cout << "Transaction failed" << endl;
        }
        disconnect();
    }
    
    // Virtual destructor
    // always add a virtual destructor to abstract classes
    virtual ~AbstractDatabase() {}
};

class MySQLDatabase : public AbstractDatabase {
public:
    void connect() override {
        cout << "Connecting to MySQL database..." << endl;
        // Implementation details
    }
    
    void disconnect() override {
        cout << "Disconnecting from MySQL database..." << endl;
        // Implementation details
    }
    
    bool executeQuery(const string& query) override {
        cout << "Executing MySQL query: " << query << endl;
        // Implementation details
        return true;
    }
};

class PostgreSQLDatabase : public AbstractDatabase {
public:
    void connect() override {
        cout << "Connecting to PostgreSQL database..." << endl;
        // Implementation details
    }
    
    void disconnect() override {
        cout << "Disconnecting from PostgreSQL database..." << endl;
        // Implementation details
    }
    
    bool executeQuery(const string& query) override {
        cout << "Executing PostgreSQL query: " << query << endl;
        // Implementation details
        return true;
    }
};

int main(){
    MySQLDatabase mysql_db; //call default constructor if parenthesis is not written
    mysql_db.connect();
    mysql_db.executeQuery("use dbs");
    mysql_db.disconnect();

    PostgreSQLDatabase postgres_db;
    postgres_db.connect();
    postgres_db.executeQuery("use dbs");
    postgres_db.disconnect();

    return 0;
}