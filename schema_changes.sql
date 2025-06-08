-- 1a) Create 'projects' table
CREATE TABLE IF NOT EXISTS projects (
  project_id   INT AUTO_INCREMENT PRIMARY KEY,
  project_name VARCHAR(255) NOT NULL,
  start_date   DATE,
  end_date     DATE
);

-- 1a) Add 'budget' column
ALTER TABLE projects
  ADD COLUMN budget DECIMAL(10,2);

-- 2c) Create 'departments' table for testing
CREATE TABLE IF NOT EXISTS departments (
  department_id   INT AUTO_INCREMENT PRIMARY KEY,
  department_name VARCHAR(100),
  location        VARCHAR(100)
);
