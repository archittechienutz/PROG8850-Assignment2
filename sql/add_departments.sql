-- For CI/CD test: create 'departments' table
CREATE TABLE IF NOT EXISTS departments (
  department_id   INT AUTO_INCREMENT PRIMARY KEY,
  department_name VARCHAR(100),
  location        VARCHAR(100)
);
