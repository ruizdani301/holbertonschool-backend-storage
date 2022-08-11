-- 1. In and not out
-- Write a SQL script that creates a table users following these requirements:

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country ENUM ('US', 'CO', 'TN') DEFAULT 'US'
    PRIMARY KEY (id)
)
