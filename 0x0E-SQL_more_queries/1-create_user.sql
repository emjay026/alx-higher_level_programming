-- a script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXIST 'user_0d_1'@'localhost'
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
