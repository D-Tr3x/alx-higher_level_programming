-- Converts `hbtn_0c_0` database to UTF8(utf8mb4, utf8mb4_unicode_ci):
USE hbtn_0c_0;
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Database hbtn_0c_0 to UTF8
-- ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Table first_table to UTF8
-- ALTER TABLE `hbtn_0c_0`.`first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Field name in first_table to UTF8
-- ALTER TABLE `hbtn_0c_0`.`first_table` MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
