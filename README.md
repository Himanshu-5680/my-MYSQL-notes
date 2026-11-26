<div align="center">

# 📊 SQL for Data Science: Quick Revision Notes

*A structured compilation of SQL concepts optimized for quick revision and interview prep.* 🚀

![SQL](https://img.shields.io/badge/SQL-Data_Science-blue?style=for-the-badge&logo=postgresql) ![Python](https://img.shields.io/badge/Python-DB--API-yellow?style=for-the-badge&logo=python) ![Jupyter](https://img.shields.io/badge/Jupyter-Magic_Commands-orange?style=for-the-badge&logo=jupyter) ![Data Analysis](https://img.shields.io/badge/Data_Analysis-Pandas_%7C_Seaborn-success?style=for-the-badge)

<br>

> 📥 **Download:** [Get the PDF version of these notes here](https://github.com/Himanshu-5680/my-MYSQL-notes/blob/main/Raw_Notes-%26-PDF/SQL-for-Data-Science-Coursera-Cheatsheet.pdf.pdf?raw=true)
>
> 📥 **Download:** [New release](https://github.com/Himanshu-5680/SQL-for-Data-Science-Cheatsheet/releases/latest)

</div>

---

<details open>
<summary><b>📑 Table of Contents</b></summary>
<br>

1. [🗄️ SQL Basics](#1-%EF%B8%8F-sql-basics)
2. [🔍 SELECT Statement & Data Retrieval](#2--select-statement--data-retrieval)
3. [🧮 SQL Useful Expressions (COUNT, DISTINCT, LIMIT)](#3--sql-useful-expressions-count-distinct-limit)
4. [➕ INSERT Statement](#4--insert-statement)
5. [🔄 UPDATE & ❌ DELETE Statements](#5--update---delete-statements)
6. [🧠 Database Concepts](#6--database-concepts)
7. [🗂️ Types of SQL Statements](#7-%EF%B8%8F-types-of-sql-statements)
8. [🏗️ CREATE TABLE Statement](#8-%EF%B8%8F-create-table-statement)
9. [🛠️ ALTER, DROP & TRUNCATE Statements](#9-%EF%B8%8F-alter-drop--truncate-statements)
10. [🎯 Advanced Filtering Techniques (LIKE, BETWEEN, IN)](#10--advanced-filtering-techniques-like-between-in)
11. [📶 Sorting Result Sets (ORDER BY)](#11--sorting-result-sets-order-by)
12. [📊 Grouping and Filtering Result Sets](#12--grouping-and-filtering-result-sets)
13. [⚙️ Built-in Database Functions](#13-%EF%B8%8F-built-in-database-functions)
14. [🕒 Date and Time Functions](#14--date-and-time-functions)
15. [🪆 Subqueries (Nested Queries)](#15--subqueries-nested-queries)
16. [🔗 Accessing Multiple Tables (Implicit Joins)](#16--accessing-multiple-tables-implicit-joins)
17. [🐍 Accessing Databases with Python & SQL APIs](#17--accessing-databases-with-python--sql-apis)
18. [💻 Writing Code Using Python DB-API](#18--writing-code-using-python-db-api)
19. [📓 Jupyter Notebook Magic Commands & SQL Magic](#19--jupyter-notebook-magic-commands--sql-magic)
20. [📈 Data Analysis with Python (SQLite3, Pandas & Seaborn)](#20--data-analysis-with-python-sqlite3-pandas--seaborn)
21. [🔌 Connecting to IBM Db2 with Python (`ibm_db` API)](#21--connecting-to-ibm-db2-with-python-ibm_db-api)

</details>

---

## 1. 🗄️ SQL Basics

**SQL (Structured Query Language)** is used to query or retrieve data from relational databases.

### Core Concepts

* **Data:** A collection of facts (words, numbers, pictures). A critical asset for any business.
* **Database:** A program/repository to store, add, modify, and query data.
* **Relational Database:** Data organized in a tabular form (columns and rows, like a spreadsheet).
  * **Columns** contain item properties (e.g., `LastName`, `FirstName`).
  * Tables can have relationships with one another.

### DBMS vs RDBMS

| System | Description | Examples |
| :--- | :--- | :--- |
| **DBMS** | Database Management System. Tools to manage data within a database. | MongoDB, Redis |
| **RDBMS** | Relational Database Management System. Specifically for relational data. | MySQL, Oracle, DB2, PostgreSQL |

### 5 Basic SQL Commands 🛠️

1. `CREATE` - To create a table.
2. `INSERT` - To populate/fill data into a table.
3. `SELECT` - To view/retrieve data.
4. `UPDATE` - To modify existing data.
5. `DELETE` - To remove data.

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 2. 🔍 SELECT Statement & Data Retrieval

The `SELECT` statement is a **DML (Data Manipulation Language)** command used to read or retrieve data. It is often referred to as a query, and the output is called a *result set* or *result table*.

### Basic Syntax

> 💡 **Retrieve all columns:** *(Often read as "select star from table name")*

```sql
SELECT * 
FROM table_name;
```

> 💡 **Specific columns:** *(Columns are displayed in the exact order they are written).*

```sql
SELECT column1, column2 FROM table_name;
```

### WHERE Clause & Predicate

* The `WHERE` clause is used to filter and restrict the result set.
* **Predicate:** A condition that evaluates to true, false, or unknown.

```sql
SELECT book_id, title FROM book WHERE book_id = 'B1';
```

### Comparison Operators (Used within the WHERE clause)

1. Equal to (`=`)
2. Greater than (`>`)
3. Less than (`<`)
4. Greater than or equal to (`>=`)
5. Less than or equal to (`<=`)
6. Not equal to (`<>` or `!=`)

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 3. 🧮 SQL Useful Expressions (COUNT, DISTINCT, LIMIT)

### COUNT Function

* **Purpose:** Returns the total number of rows (count) that match the query criteria.
* **Examples:**
  * Count all rows: `SELECT COUNT(*) FROM tablename;`
  * Count with a condition: `SELECT COUNT(COUNTRY) FROM MEDALS WHERE COUNTRY = 'CANADA';`

### DISTINCT Keyword

* **Purpose:** Removes duplicate values from the result set, displaying only unique values.
* **Examples:**
  * Retrieve unique values: `SELECT DISTINCT columnname FROM tablename;`
  * Unique countries that won gold: `SELECT DISTINCT COUNTRY FROM MEDALS WHERE MEDALTYPE = 'GOLD';`

### LIMIT Clause

* **Purpose:** Restricts the number (quantity) of rows retrieved from the database.
* **Examples:**
  * View the first 10 rows: `SELECT * FROM tablename LIMIT 10;`
  * Apply limit on filtered data: `SELECT * FROM MEDALS WHERE YEAR = 2018 LIMIT 5;`

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 4. ➕ INSERT Statement

* **Purpose:** Used to add (populate) new rows of data into a table.
* **Type:** A DML (Data Manipulation Language) statement.

### Basic Syntax

```sql
INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
```

### Key Rules

1. **Column & Value Match:** The total count of values in the `VALUES` clause must be exactly equal to the number of columns listed.
2. **Order Matters:** The values provided must strictly follow the same sequence as the specified columns.

### Row Insertion Methods

1. **One row at a time:** Inserting a single record.
2. **Multiple rows at a time:** Inserting multiple records in a single `INSERT` statement by separating value sets with a comma (`,`).

```sql
INSERT INTO author (author_id, last_name, first_name) 
VALUES ('A1', 'Chong', 'Raul'), 
       ('A2', 'Ahuja', 'Rav');
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 5. 🔄 UPDATE & ❌ DELETE Statements

**Type:** Both are DML (Data Manipulation Language) statements used to modify or remove data.

### 1. UPDATE Statement

* **Purpose:** To alter or modify existing data within a table.
* **Basic Syntax:**

```sql
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
```

* **Example:**

```sql
UPDATE AUTHOR SET LAST_NAME = 'KATTA', FIRST_NAME = 'LAKSHMI' WHERE AUTHOR_ID = 'A2';
```

> ⚠️ **CRITICAL WARNING:** If you forget to include the `WHERE` clause, **ALL ROWS** in the table will be updated!

### 2. DELETE Statement

* **Purpose:** To permanently remove one or more rows from a table.
* **Basic Syntax:**

```sql
DELETE FROM table_name WHERE condition;
```

* **Example:**

```sql
DELETE FROM AUTHOR WHERE AUTHOR_ID IN ('A2', 'A3');
```

> ⚠️ **CRITICAL WARNING:** If you execute `DELETE FROM table_name;` without a `WHERE` clause, the entire data of the table will be deleted (the table will be emptied)!

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 6. 🧠 Database Concepts

### 1. Relational Model

* The most widely used data model.
* Stores data in a simple structure: Tables (Rows and Columns).
* **Main Advantage:** Provides Data Independence (Logical, Physical, and Physical storage independence).

### 2. ER Model (Entity-Relationship Model) & ERD

* Used as a conceptual tool to design relational databases.
* **ERD (Entity-Relationship Diagram):** A visual representation of entities and their relationships.
* **Building Blocks:**
  * **Entity:** Any real-world object (Noun: Person, Place, Thing) that exists independently. (ERD Symbol: Rectangle). Examples: Book, Author, Borrower.
  * **Attribute:** The characteristics or properties that provide details about the entity. (ERD Symbol: Oval). Examples: Title, Edition, and Year for a Book.

### 3. Mapping (ER Model to Relational Table)

| ER Model Component | Relational Database Equivalent |
| :--- | :--- |
| **Entity** | Table |
| **Attribute** | Column |
| **Data Values** | Row / Tuple |

### 4. Common Data Types

* **CHAR (Character):** For fixed-length text (e.g., ISBN, State codes).
* **VARCHAR (Variable Character):** For variable-length text (e.g., Title, Name, Email).
* **Numeric (INTEGER / DECIMAL):** For numbers (e.g., Edition, Year, Price).
* **Date / Time:** For storing dates and timestamps.

### 5. Database Keys

* **Primary Key (PK):** Uniquely identifies every single row (tuple) in a table. Prevents data duplication (no duplicates allowed, cannot be null).
* **Foreign Key (FK):** A Primary Key from another table that is added to the current table. Used to establish a relationship or link between tables.

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 7. 🗂️ Types of SQL Statements

SQL statements are used to interact with Entities (tables), Attributes (columns), and Tuples (rows/data values) in relational databases.

### 1. DDL (Data Definition Language)

* **Purpose:** To define, modify, or delete the structure of database objects (such as tables).
* **Common Statements:**
  * `CREATE`: To create a new table and define its columns/data types.
  * `ALTER`: To modify an existing table's structure.
  * `TRUNCATE`: To delete all data inside a table while keeping the table structure intact.
  * `DROP`: To permanently delete the entire table along with its structure.

### 2. DML (Data Manipulation Language)

* **Purpose:** To read and modify the data present inside tables. Often referred to as **CRUD** operations:
  * **C**reate ➔ `INSERT`
  * **R**ead ➔ `SELECT`
  * **U**pdate ➔ `UPDATE`
  * **D**elete ➔ `DELETE`

### SQL Statement Categories Comparison

| Category | Main Focus | Target | Common Commands |
| :--- | :--- | :--- | :--- |
| **DDL** | Defining the Structure / Schema | Database Objects (Tables) | CREATE, ALTER, TRUNCATE, DROP |
| **DML** | Manipulating the Data | Rows / Records | INSERT, SELECT, UPDATE, DELETE |

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 8. 🏗️ CREATE TABLE Statement

**Type:** The most common DDL statement. Used to create new tables (Entities) and their columns (Attributes).

### Basic Syntax Structure

```sql
CREATE TABLE table_name (
    column1_name data_type [constraints],
    column2_name data_type [constraints],
    column3_name data_type [constraints]
);
```

### Column Components

1. **Column Name:** The name of the attribute (e.g., `author_id`, `firstname`).
2. **Data Type:** The format of the stored data:
   * `CHAR(n)`: Fixed-length string.
   * `VARCHAR(n)`: Variable-length string.
3. **Optional Constraints:** Rules applied for data validation.

### Key Constraints Mentioned

* **PRIMARY KEY:** Uniquely identifies each row; does not allow duplicate records.
* **NOT NULL:** Ensures that a blank or NULL value cannot be inserted into the column.

### Practical Example (Library Database)

```sql
CREATE TABLE author (
    author_id CHAR(2) PRIMARY KEY NOT NULL,
    lastname VARCHAR(15) NOT NULL,
    firstname VARCHAR(15) NOT NULL,
    email VARCHAR(40),
    city VARCHAR(15),
    country CHAR(2)
);
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 9. 🛠️ ALTER, DROP & TRUNCATE Statements

### 1. ALTER TABLE Statement

* **Purpose:** To modify the structure of an existing table.
* **Operations & Syntax:**
  * **Add Column:**

    ```sql
    ALTER TABLE author ADD COLUMN telephone_number BIGINT;
    ```

  * **Modify Data Type:**

    ```sql
    ALTER TABLE author MODIFY telephone_number CHAR(20);
    ```

    > ⚠️ **Warning (Data Compatibility):** If the column already contains incompatible data, the query will fail.

  * **Drop Column:**

    ```sql
    ALTER TABLE author DROP COLUMN telephone_number;
    ```

### 2. DROP TABLE Statement

* **Purpose:** To permanently delete a table from the database (both structure and data).
* **Syntax Example:**

```sql
DROP TABLE author;
```

### 3. TRUNCATE TABLE Statement

* **Purpose:** To delete all rows (data) at once, while keeping the table structure intact. Much faster than a DELETE statement.
* **Syntax Example:**

```sql
TRUNCATE TABLE author IMMEDIATE;
```

### Quick Comparison: DROP vs TRUNCATE vs DELETE

| Command | Category | Table Structure Remains? | Data Deleted? | Speed |
| :--- | :--- | :--- | :--- | :--- |
| **DELETE** | DML | Yes | Yes (Selected or all rows) | Slow (Logs row-by-row) |
| **TRUNCATE** | DDL | Yes (Table becomes empty) | Yes (All rows) | Very Fast |
| **DROP** | DDL | No (Table is destroyed) | Yes (All rows) | Instant |

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 10. 🎯 Advanced Filtering Techniques (LIKE, BETWEEN, IN)

When we don't know the exact value for the `WHERE` clause, or when the query is getting too long, these three advanced filtering techniques are commonly used in the industry to make queries smarter and shorter.

### 1. String Patterns (`LIKE` Operator)

* **Purpose:** Used to search for a specific text pattern within a column.
* **Wildcard Character (`%`):** The percent sign (`%`) is used to substitute (replace) missing characters. It can be placed before, after, or on both sides of the text pattern.
* **Example Scenario:** We don't remember the exact name of an author, but we know it starts with the letter 'R'.
* **Query:**

```sql
SELECT firstname FROM author WHERE firstname LIKE 'R%';
```

* **Concept Output (Author Table):**

| firstname |
| :--- |
| Raul |
| Rav |

*(Only rows where the name starts with 'R' will be returned.)*

### 2. Ranges (`BETWEEN ... AND` Operator)

* **Purpose:** Used to filter values that fall within a specific range (inclusive of both start and end values).
* **Benefit:** It makes long conditions using `>=` (greater than or equal to) and `<=` (less than or equal to) shorter and much easier to read.
* **Example Scenario:** Retrieve books that have between 290 and 300 pages.
* **Query:**

```sql
-- Normal way (Long method):
-- WHERE pages >= 290 AND pages <= 300

-- Smart way (BETWEEN operator):
SELECT * FROM Book WHERE pages BETWEEN 290 AND 300;
```

### 3. Sets of Values (`IN` Operator)

* **Purpose:** Used to specify multiple exact values (a set of values) together in a single `WHERE` clause.
* **Benefit:** When data cannot be grouped into numeric ranges (like text values), we use `IN` to avoid writing multiple `OR` conditions over and over again.
* **Example Scenario:** We want data for authors who are from 'Australia' or 'Brazil'. If we needed to add Canada, India, and China as well, writing out `OR` conditions for each would make the query way too long.
* **Query:**

```sql
-- Without IN operator (Long method):
-- WHERE country = 'Australia' OR country = 'Brazil'

-- Smart way (IN operator):
SELECT * FROM author WHERE country IN ('Australia', 'Brazil');
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 11. 📶 Sorting Result Sets (ORDER BY)

When retrieving data, results are not automatically sorted. We use the `ORDER BY` clause to organize the output alphabetically or numerically.

### 1. Default Sorting (Ascending Order)

* **Rule:** By default, `ORDER BY` sorts data in Ascending order (A to Z, or lowest to highest number).
* **Example Scenario:** A list of book titles arranged alphabetically.
* **Query:**

```sql
SELECT title FROM book ORDER BY title;
```

* **Conceptual Output:**

| title (Sorted A-Z) |
| :--- |
| A Tale of Two Cities |
| Harry Potter |
| The Great Gatsby |
| To Kill a Mockingbird |

### 2. Descending Sorting (`DESC` Keyword)

* **Rule:** To sort data in reverse order (Z to A, or highest to lowest), add the `DESC` keyword.
* **Sorting Logic:** If the first characters match, the database checks character-by-character to determine the order.
* **Query:**

```sql
SELECT title FROM book ORDER BY title DESC;
```

* **Conceptual Output:**

| title (Sorted Z-A) |
| :--- |
| To Kill a Mockingbird |
| The Great Gatsby |
| Harry Potter |
| A Tale of Two Cities |

### 3. Sorting by Column Index

* **Rule:** Instead of typing the full column name, you can use its sequence number in the `SELECT` list.
* **Benefit:** Saves time and makes the query shorter.
* **Query:**

```sql
-- '2' represents the second column (pages)
SELECT title, pages FROM book ORDER BY 2; 
```

* **Conceptual Output:**

| title (Column 1) | pages (Column 2 - Sorted ASC) |
| :--- | :--- |
| The Great Gatsby | 180 |
| To Kill a Mockingbird | 281 |
| A Tale of Two Cities | 341 |
| Harry Potter | 500 |

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 12. 📊 Grouping and Filtering Result Sets

Used to summarize, count, and filter grouped data (critical for answering business questions like "total sales per product").

### 1. Eliminating Duplicates (`DISTINCT`)

* **Rule:** Returns only unique values from a column with repeated data.
* **Query:**

```sql
SELECT DISTINCT country FROM author ORDER BY 1;
```

### 2. Grouping Data & Counting (`GROUP BY`)

* **Rule:** Groups rows with identical values into summary rows. Almost always used with aggregate functions (`COUNT()`, `SUM()`, `AVG()`).
* **Example:** How many authors come from each country?
* **Query:**

```sql
SELECT country, COUNT(country) FROM author GROUP BY country;
```

### 3. Renaming Columns (`AS` Keyword)

* **Rule:** Gives a clean, readable alias to calculated columns (instead of showing ugly default names like `COUNT(country)`).
* **Query:**

```sql
SELECT country, COUNT(country) AS Count FROM author GROUP BY country;
```

### 4. Filtering Grouped Data (`HAVING` Clause)

* **Rule:** Filters data *after* it has been grouped.
* **Query:** Show only countries with more than 4 authors.

```sql
SELECT country, COUNT(country) AS Count FROM author GROUP BY country HAVING COUNT(country) > 4;
```

> 💡 **Interview Tip (WHERE vs. HAVING):** `WHERE` filters individual rows *before* grouping, while `HAVING` filters grouped totals/aggregates *after* grouping.

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 13. ⚙️ Built-in Database Functions

Using SQL functions directly is a best practice for processing large datasets efficiently before sending data to an application.

### 1. Aggregate Functions (Column Functions)

* **Rule:** Takes a collection of values (an entire column) and returns a single summarized value.
* **Common Functions:**
  * `SUM()`: Adds all values.
  * `MAX()` / `MIN()`: Finds highest/lowest values.
  * `AVG()`: Calculates the mean.
* **Query Examples:**

```sql
SELECT SUM(COST) AS SUM_OF_COST FROM PETRESCUE;
SELECT MAX(QUANTITY) FROM PETRESCUE;
SELECT AVG(COST / QUANTITY) FROM PETRESCUE WHERE ANIMAL = 'Dog';
```

### 2. Scalar & String Functions

* **Rule:** Operates row-by-row on individual values.
* **Common Functions:**
  * `ROUND()`: Rounds numbers.
  * `LENGTH()`: Returns string character count.
  * `UCASE()` / `LCASE()` (or `UPPER()` / `LOWER()`): Converts text casing.
* **Query Examples (Smart Filtering & Nesting):**

```sql
-- Lowercase filtering handles messy real-world data entries ('CAT', 'Cat', 'cat')
SELECT * FROM PETRESCUE WHERE LOWER(ANIMAL) = 'cat';

-- Nesting functions (Uppercase unique names)
SELECT DISTINCT(UPPER(ANIMAL)) FROM PETRESCUE;
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 14. 🕒 Date and Time Functions

Crucial for generating time-series reports and dashboards in analytics.

### 1. Data Types

* `DATE`: 8 digits (`YYYYMMDD`)
* `TIME`: 6 digits (`HHMMSS`)
* `TIMESTAMP`: 20 digits (`YYYYXXDDHHMMSSZZZZZZ` where XX=Month, ZZZZZZ=Microseconds)

### 2. Date Operations

* **Extracting Parts:** Use `DAY()`, `MONTH()`, `YEAR()` to pull specific parts of a date.

```sql
SELECT DAY(RESCUE_DATE) FROM PETRESCUE WHERE ANIMAL = 'Cat';
```

* **Filtering by Date:**

```sql
SELECT COUNT(*) FROM PETRESCUE WHERE MONTH(RESCUE_DATE) = 5;
```

* **Date Arithmetic:** Adding/subtracting time intervals.

```sql
SELECT DATE_ADD(RESCUE_DATE, INTERVAL 3 DAY) FROM PETRESCUE;
```

* **Special Registers:** Getting the current system time.

```sql
SELECT CURRENT_DATE - RESCUE_DATE FROM PETRESCUE;
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 15. 🪆 Subqueries (Nested Queries)

A query nested inside parentheses `()` within another main query. Used to bypass basic SQL limitations for complex data extraction.

### 1. In the `WHERE` Clause

* **Problem:** Aggregate functions (`AVG`, `MAX`) cannot be used directly in a `WHERE` clause.
* **Solution:** Use a subquery to calculate the aggregate first.
* **Query:** Retrieve employees earning less than the company average.

```sql
SELECT EMP_ID, FIRST_NAME, LAST_NAME, SALARY 
FROM EMPLOYEES 
WHERE SALARY < (SELECT AVG(SALARY) FROM EMPLOYEES);
```

### 2. In the Column List

* **Problem:** Comparing individual row data against an aggregate metric throws a `GROUP BY` error in standard queries.
* **Solution:** Put the subquery in the `SELECT` statement to calculate it for every row.
* **Query:**

```sql
SELECT EMP_ID, SALARY, (SELECT AVG(SALARY) FROM EMPLOYEES) AS AVG_SALARY 
FROM EMPLOYEES;
```

### 3. In the `FROM` Clause (Derived Tables)

* **Concept:** Treats the subquery result as a temporary, virtual table (useful for data security or staged grouping).
* **Query:**

```sql
SELECT * FROM (
    SELECT EMP_ID, FIRST_NAME, LAST_NAME, DEPT_ID FROM EMPLOYEES
) AS EMP4ALL;
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 16. 🔗 Accessing Multiple Tables (Implicit Joins)

Real industry projects require pulling data scattered across multiple tables.

### 1. Using Sub-queries with Multiple Tables

* **Rule:** Use the result of one table's query as a filter for another table.
* **Query:** Get employees working in a specific location by checking the departments table.

```sql
SELECT * FROM employees 
WHERE DEP_ID IN (SELECT DEP_ID_DEP FROM departments WHERE LOC_ID = 'L0002');
```

### 2. Implicit Joins (Cartesian Product)

* **Warning:** Simply running `SELECT * FROM table1, table2` creates a massive Cartesian product (every row joins with every row).
* **Fixing with `WHERE` (Matching IDs):** Link them on their common Primary/Foreign Key.

```sql
SELECT * FROM employees, departments 
WHERE employees.DEP_ID = departments.DEP_ID_DEP;
```

* **Using Table Aliases (Best Practice):** Give tables short nicknames in the `FROM` clause for cleaner code.

```sql
SELECT E.EMP_ID, D.DEP_NAME 
FROM employees E, departments D 
WHERE E.DEP_ID = D.DEP_ID_DEP;
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 17. 🐍 Accessing Databases with Python & SQL APIs

As a Data Analyst, we use Python to connect to databases, run SQL queries, and analyze the data all in one place (usually inside a Jupyter Notebook).

### 1. Why use Python for Database Access?

* **Rich Ecosystem:** Has powerful data science libraries (NumPy, Pandas, Matplotlib, SciPy).
* **Easy & Portable:** Simple syntax, open-source, and runs on any operating system without changing the code.
* **DB-API:** Python has a standard Database API (DB-API) that makes writing database code very easy and well-documented.

### 2. Jupyter Notebooks (The Workspace)

* **What is it?** A virtual web-based editor to create and share documents containing live code, visualizations, equations, and text.
* **Key Advantages:**
  * **Multi-language:** Supports 40+ languages (Python, R, Julia, Scala).
  * **Easy Sharing:** Share easily via Email, Dropbox, or GitHub.
  * **Rich Output:** Displays interactive HTML, images, videos, and LaTeX directly.
  * **Big Data Integration:** Works seamlessly with tools like Apache Spark, Pandas, scikit-learn, and TensorFlow.

### 3. How Python Talks to Databases (API Workflow)

An API (Application Programming Interface) is a set of functions that allows different software programs to talk to each other. When your Python code runs an SQL query, it follows a standard 4-step API workflow:

1. **Connect:** The program makes an API call to connect to the Database Management System (DBMS).
2. **Build & Send:** The program builds the SQL query as a text string in a buffer, and makes an API call to pass this text to the DBMS.
3. **Check Status:** It makes API calls to retrieve the query results, check the request status, and handle any errors.
4. **Disconnect:** Finally, it makes an API call to close the connection to the database.

### 4. Popular Database APIs (Important Table)

Every major database system uses its own specific proprietary API library to connect with applications. You must remember these pairings:

| Database System / Platform | SQL API / Library Used |
| :--- | :--- |
| MySQL | MySQL C API |
| PostgreSQL | psycopg2 |
| IBM DB2 | IBM_DB |
| Microsoft SQL Server | dblib |
| Oracle | OCI |
| Microsoft Windows OS (General) | ODBC |
| Java Applications | JDBC |

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 18. 💻 Writing Code Using Python DB-API

### 1. What is Python DB-API?

* **Definition:** It is the standard Application Programming Interface (API) for accessing relational databases in Python.
* **Core Benefit:** Write your database code once. Instead of learning a completely new way to code for every different database, DB-API provides a single, standard structure that works across multiple relational databases.
* **Advantages:** Easy to understand, ensures consistency across different Python modules, highly portable code, and provides broad database connectivity.

### 2. DB-API Libraries for Popular Databases

Every database system uses its own specific library to connect to Python applications.

| Database System | Python DB-API Library |
| :--- | :--- |
| IBM DB2 | `ibm_db` |
| MySQL | `mysql-connector-python` |
| PostgreSQL | `psycopg2` |
| MongoDB | `PyMongo` |

### 3. The Two Main Concepts: Connections vs. Cursors

#### A. Connection Objects

* **Purpose:** Used to connect to the database and manage transactions.
* **Key Methods associated with Connections:**
  1. `cursor()`: Creates and returns a new cursor object using the active connection.
  2. `commit()`: Saves (commits) any pending transactions or changes to the database.
  3. `rollback()`: Undoes any pending transactions, rolling the database back to its state before the transaction started.
  4. `close()`: Closes the database connection to free up system resources.

#### B. Cursor Objects (Query Objects)

* **Purpose:** Used to run SQL queries and scan/scroll through the fetched results.
* **How it works (The File Handle Analogy):**
  * A cursor behaves exactly like a file handle in programming.
  * Just as you open a file, read its contents tracking your current line, and then close it—you open a cursor, fetch query results tracking your current row position, and then close it.
* **Isolation Rule:** Cursors created from the same connection are **NOT** isolated. If one cursor makes a change to the database, the other cursors on that same connection can see those changes immediately.

### 4. Standard DB-API Coding Workflow (5 Steps)

Whenever you write Python code to query a database, you will follow this exact sequence:

1. **Import:** Import the specific database module/library (e.g., `import psycopg2`).
2. **Connect:** Use the `connect()` constructor and pass in your credentials (database name, username, password) to create a Connection Object.
3. **Create Cursor:** Call the `.cursor()` method on your connection object to create a Cursor Object.
4. **Execute & Fetch:** Use the cursor to run your SQL queries and fetch the results into your application.
5. **Close:** Call `.close()` on the connection to shut it down.

> ⚠️ **Crucial Rule:** Always close unused connections to prevent them from eating up system resources!

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 19. 📓 Jupyter Notebook Magic Commands & SQL Magic

### 1. What are Magic Statements?

* **Definition:** Special commands in Jupyter Notebooks that provide extra functionalities.
* **Nature:** They are not valid Python code, but they change how the notebook behaves to solve common data analysis problems.

### 2. Line Magics vs. Cell Magics

Magic commands are divided into two main categories:

| Feature | Line Magics | Cell Magics |
| :--- | :--- | :--- |
| **Prefix** | Single Percentage (`%`) | Double Percentage (`%%`) |
| **Scope** | Operates on a single line of input only. | Operates on multiple lines (the entire cell). |
| **Usage Rule** | You can use multiple line magics in one cell (each on a new line). | Must be placed at the very top of the cell. |
| **Example** | `%timeit` (Times one single statement) | `%%timeit` (Times the whole cell's execution) |

### 3. Popular Magic Commands (Cheat Sheet)

| Command | Type | What it does |
| :--- | :--- | :--- |
| `%pwd` | Line | Prints the Current Working Directory (folder path). |
| `%ls` | Line | Lists all files present in the current directory. |
| `%history` | Line | Shows the history of all executed commands. |
| `%who` | Line | Lists all user-defined variables in the memory. |
| `%whos` | Line | Gives detailed information about all variables (type, data). |
| `%reset` | Line | Deletes all variables and resets the namespace. |
| `%matplotlib inline` | Line | Forces Matplotlib plots to display directly inside the notebook. |
| `%lsmagic` | Line | Lists all available magic commands in Jupyter. |
| `%%writefile filename.txt` | Cell | Writes the entire contents of the cell into a text file. |

### 4. Running Other Languages (Cell Magics)

Cell magics allow you to run code other than Python inside a Jupyter cell.

* `%%HTML`: Renders HTML code (e.g., `<h1>Hello World</h1>`).
* `%%JS` or `%%Javascript`: Runs JavaScript code (e.g., pop-up alerts).
* `%%bash`: Runs terminal/command-prompt commands (e.g., `echo "Hello"`).

### 5. SQL Magic: Accessing Databases in Jupyter

To write direct SQL queries inside a Jupyter Notebook, follow this exact 4-step workflow:

**Step 1: Install the Dependency**

Run this in a cell to install the required library:

```python
!pip install ipython-sql
```

**Step 2: Load the SQL Extension**

Enable SQL magic in your notebook:

```python
%load_ext sql
```

**Step 3: Establish the Connection**

Connect to your specific database (Example using SQLite3 and a database named `HR.db`):

```python
%sql sqlite:///HR.db
```

**Step 4: Run SQL Queries**

Now you can write SQL queries directly!

* **For a short, 1-line query:**

```sql
%sql SELECT * FROM employee LIMIT 5;
```

* **For a complex, multi-line query:**

```sql
%%sql
SELECT department, COUNT(*) 
FROM employee 
GROUP BY department;
```

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 20. 📈 Data Analysis with Python (SQLite3, Pandas & Seaborn)

> **Dataset Used:** McDonald's Menu Nutritional Facts (from Kaggle) — **260 food items** across **9 unique categories** (e.g., Max Total Fat = 118).

### 1. Storing & Retrieving Data (SQLite3 + Pandas)

* **SQLite3:** An in-process Python library that provides a self-contained, serverless, zero-configuration transactional SQL database engine.

**4-Step Workflow:**

```python
import pandas as pd
import sqlite3

# 1. Read CSV into a Pandas DataFrame
data = pd.read_csv('menu.csv')

# 2. Connect to (or create) SQLite database
conn = sqlite3.connect('mcdonalds.db')

# 3. Load DataFrame into SQL as a table
data.to_sql('mcdonalds_nutrition', conn)

# 4. Query SQL table back into a DataFrame & preview top rows
df = pd.read_sql("SELECT * FROM mcdonalds_nutrition", conn)
df.head()
```

### 2. Exploratory Data Analysis (EDA) with Pandas

* **Goal:** Find which menu item has the highest **Sodium** content *(Healthy daily limit target:* $< 2,000$ *mg)*.

**3-Step Code Breakdown:**

```python
# Code 1: Check summary statistics for Sodium
df['Sodium'].describe()

# Code 2: Find the row index of the maximum Sodium value
df['Sodium'].idxmax()       # Output: 82

# Code 3: Get the exact Item name at index 82
df.at[82, 'Item']           # Output: 'Chicken McNuggets (40 piece)'
```

*(Exact code and outputs from the lesson)*

**Example Output Table (`df['Sodium'].describe()`):**

| Statistic | Value | Meaning |
| :--- | :--- | :--- |
| **count** | 260.0 | Total number of food items |
| **mean** | 495.75 | Average sodium value |
| **std** | 577.03 | Standard deviation (spread) |
| **min** | 0.0 | Lowest sodium value |
| **25% / 50% / 75%** | 107.5 / 190.0 / 865.0 | Quartiles (50% = median) |
| **max** | **3600.0** | Highest sodium value (Index 82) |

### 3. Data Visualization with Seaborn

Visualizations help detect **relationships, patterns, and outliers** quickly.

#### A. Swarm Plot (`swarmplot`) — Categorical Scatter Plot

* **Use:** Compare numeric values across categories (`x="Category"`, `y="Sodium"`, `data=df`).
* **Insight:** Clearly highlights an extreme sodium point near **3,600 mg**.

#### B. Joint Plot (`jointplot`) — Scatter Plot + Histograms

```python
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

plot = sns.jointplot(x="Protein", y='Total Fat', data=df)
plot.show()   # Practical tip: use plt.show() in newer Python/Seaborn versions
```

*(Code syntax from slide)*

* **Correlation:** Measures association between two variables (ranges from $-1$ to $+1$).
* **Insight:** Protein and Total Fat show a strong **positive correlation** (`pearsonr = 0.81`, $p = 3.7 \times 10^{-61}$).
* **Extra Details:** Displays two histograms (Protein on top, Total Fat on the right) and reveals a possible **outlier** outside the main pattern.

#### C. Box Plot (`boxplot`) — Distribution & Outliers

```python
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

plot = sns.set_style("whitegrid")
ax = sns.boxplot(x=df["Sugars"])
plot.show()   # Practical tip: use plt.show() in newer versions
```

*(Code syntax from slide)*

* **Structure:** The box captures the **middle 50%** of data; lines (whiskers) and dots show skewness and **outliers**.
* **Insight:** Average sugar is around **30g**, while extreme outliers reach up to **\~128g** (likely candies/desserts).

### 4. Quick Revision Cheat Sheet

| Function / Method | Library | Purpose |
| :--- | :--- | :--- |
| `pd.read_csv()` | Pandas | Reads a CSV file into a DataFrame |
| `sqlite3.connect()` | SQLite3 | Opens a connection to a SQLite database |
| `data.to_sql()` | Pandas | Saves a DataFrame as a SQL database table |
| `pd.read_sql()` | Pandas | Runs a SQL query and loads the result into a DataFrame |
| `df.describe()` | Pandas | Shows summary statistics (mean, min, max, std, quartiles) |
| `.idxmax()` | Pandas | Returns the row index of the maximum value |
| `.at[row, col]` | Pandas | Fetches a single exact value using row index and column name |
| `sns.swarmplot()` | Seaborn | Plots a categorical scatter plot |
| `sns.jointplot()` | Seaborn | Plots scatter plot + histograms + correlation (`pearsonr`) |
| `sns.boxplot()` | Seaborn | Shows data distribution (middle 50%) and highlights outliers |

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)

---

## 21. 🔌 Connecting to IBM Db2 with Python (`ibm_db` API)

### 1. What is the `ibm_db` API?

* A Python library providing functions to access and manipulate data in **IBM DB2** and **Informix** databases.
* **Under the Hood:** Uses the IBM Data Server Driver for **ODBC** and **CLI** APIs to connect.
* **Key Capabilities:** Connecting to databases, preparing/executing SQL statements, fetching rows, calling stored procedures, committing/rolling back transactions, handling errors, and retrieving metadata.

### 2. Required Connection Credentials

| Credential | Variable Name | Example Value |
| :--- | :--- | :--- |
| **Driver Name** | `dsn_driver` | `{IBM DB2 ODBC DRIVER}` |
| **Database Name** | `dsn_database` | `BLUDB` |
| **Host DNS / IP** | `dsn_hostname` | `your-hostname.appdomain.cloud` |
| **Host Port** | `dsn_port` | `32733` |
| **Protocol** | `dsn_protocol` | `TCPIP` |
| **User ID** | `dsn_uid` | `abc12345` |
| **User Password** | `dsn_pwd` | `YourPassword123` |
| **Security (Lab extra)** | `dsn_security` | `SSL` |

### 3. Connection Workflow (4 Steps)

1. **Import Library:** Install (if needed) and import `ibm_db` into your Python notebook.
2. **Build DSN Object:** Store all connection credentials in a `dsn` connection string.
3. **Establish Connection:** Pass `dsn` to `ibm_db.connect(dsn, "", "")` to create a non-persistent connection. Use `try-except` to confirm connection or print errors via `ibm_db.conn_errormsg()`.
4. **Close Connection:** Always run `ibm_db.close(conn)` at the end to free up system resources and prevent unused connections from consuming memory.

```python
import ibm_db

# 1. Build DSN string
dsn = (
    "DRIVER={IBM DB2 ODBC DRIVER};"
    "DATABASE=BLUDB;"
    "HOSTNAME=YourHostname;"
    "PORT=32733;"
    "PROTOCOL=TCPIP;"
    "UID=YourUserID;"
    "PWD=YourPassword;"
    "SECURITY=SSL;"
)

# 2. Connect to DB2
try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database!")
except:
    print("Unable to connect:", ibm_db.conn_errormsg())

# 3. Close connection to free resources
ibm_db.close(conn)
```

### 4. Key `ibm_db` Functions (Quick Reference)

| Function | Purpose |
| :--- | :--- |
| `ibm_db.connect(dsn, "", "")` | Establishes a non-persistent database connection |
| `ibm_db.conn_errormsg()` | Returns the error message if connection fails |
| `ibm_db.server_info(conn)` | Retrieves database server metadata (DBMS name, version, DB name) |
| `ibm_db.client_info(conn)` | Retrieves client/driver metadata (driver name, ODBC version) |
| `ibm_db.close(conn)` | Closes the connection and frees resources |

[⬆ Back to Top](#-sql-for-data-science-quick-revision-notes)