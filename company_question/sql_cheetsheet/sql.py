# SQL MASTER CHEAT SHEET 🚀
### ---------------------------From Basic Queries → Advanced SQL

# 1. 🧠 SQL QUERY ORDER — MOST IMPORTANT
### Write SQL in this order:

'''
SELECT
FROM
JOIN ... ON
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
'''

### Easy Memory Trick:
'''WHAT → FROM WHERE → JOIN → FILTER → GROUP → FILTER GROUP → SORT → LIMIT

Example:

SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE salary > 30000
GROUP BY department
HAVING AVG(salary) > 50000
ORDER BY avg_salary DESC
LIMIT 5;
'''
# -------------------------------------------------
# 2. SELECT — WHAT DO YOU WANT?
'''
SELECT *
FROM employees;


SELECT name, salary
FROM employees;
'''
### Alias
'''
SELECT salary AS monthly_salary
FROM employees;
'''
### Calculation
'''
SELECT name, salary * 12 AS annual_salary
FROM employees;
'''
### Remove duplicates
'''
SELECT DISTINCT department
FROM employees;
'''

# ---------------------------------------------
# 3. WHERE — FILTER ROWS
'''
SELECT *
FROM employees
WHERE salary > 50000;
'''

### Operators
'''
=       Equal
<> / != Not equal
>       Greater
<       Smaller
>=      Greater/equal
<=      Smaller/equal
'''

### AND / OR / NOT
'''
WHERE salary > 50000 AND department = 'IT';

WHERE department = 'IT' OR department = 'HR';

WHERE NOT department = 'HR';
'''

### IN
'''
WHERE department IN ('IT', 'HR', 'Sales');
'''

### BETWEEN
'''
WHERE salary BETWEEN 30000 AND 60000;
'''

### NULL
'''
WHERE phone IS NULL;

WHERE phone IS NOT NULL;
'''

# ⚠️ Never use:
'''
WHERE phone = NULL;
'''
# ----------------------------------------


# 4. LIKE — PATTERN SEARCH
'''
% → any number of characters
_ → exactly one character
'''

'''
-- Starts with A
WHERE name LIKE 'A%';

-- Ends with A
WHERE name LIKE '%A';

-- Contains A
WHERE name LIKE '%A%';

-- Second character is A
WHERE name LIKE '_A%';
'''

# ---------------------------------------------

# 5. ORDER BY — SORT
'''
ORDER BY salary ASC;
'''

'''
ORDER BY salary DESC;
'''

### Multiple columns
'''
ORDER BY department ASC, salary DESC;
'''

# 6. LIMIT — TOP N
'''
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5;
'''
### Top 1 / highest salary
'''
ORDER BY salary DESC
LIMIT 1;
'''


# 7. 🔢 AGGREGATE FUNCTIONS
'''
COUNT() → Number
SUM()   → Total
AVG()   → Average
MAX()   → Highest
MIN()   → Lowest

Examples:

SELECT COUNT(*) FROM employees;

SELECT SUM(salary) FROM employees;

SELECT AVG(salary) FROM employees;

SELECT MAX(salary) FROM employees;

SELECT MIN(salary) FROM employees;
'''

### COUNT differences
'''
COUNT(*)                 -- all rows
COUNT(column)            -- non-NULL values
COUNT(DISTINCT column)   -- unique non-NULL values
'''

# 8. GROUP BY — MAKE GROUPS

### Example: employees per department
'''
SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department;
'''

### Average salary per department
'''
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
'''

### Golden Rule
'''
If you use:

GROUP BY department
'''
'''
then columns in `SELECT` generally must be either:
'''

'''
GROUP BY columns
OR
Aggregate functions
'''

# 9. HAVING — FILTER GROUPS

### WHERE → filters rows
### HAVING → filters groups
'''
SELECT department, COUNT(*) AS total
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
'''

### Remember:
'''
WHERE  → before GROUP BY
HAVING → after GROUP BY
'''

# 10. 🔗 JOINS
'''
Used when data is in multiple tables.
'''
### INNER JOIN
'''
Only matching rows:
'''

'''
SELECT e.name, d.department_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;
'''

### LEFT JOIN
'''
Everything from left table + matching right:
'''

'''
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;
'''

### RIGHT JOIN
'''
Everything from right table:
'''

'''
RIGHT JOIN departments d
ON e.department_id = d.department_id;
'''

### FULL OUTER JOIN
'''
Everything from both:
'''

'''
FULL OUTER JOIN departments d
ON e.department_id = d.department_id;
'''

### JOIN Memory
'''
INNER → matching only
LEFT  → all left
RIGHT → all right
FULL  → all both
'''

# 11. 🔥 MULTIPLE JOINS
'''
SELECT o.order_id, c.name, p.product_name
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN products p
ON o.product_id = p.product_id;
'''

# 12. 🧩 SUBQUERY
'''
Query inside another query.
'''
### Greater than average salary
'''
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
'''

### Highest salary
'''
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
'''

### Second highest salary
'''
SELECT MAX(salary)
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
);
'''
# 13. EXISTS

### Customers who have orders

```sql
SELECT *
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

### Customers with no orders

```sql
WHERE NOT EXISTS (...);
```

```text
EXISTS → matching record exists?
```

---

# 14. 🔀 CASE WHEN

SQL's IF/ELSE.

```sql
SELECT name, salary,
       CASE
           WHEN salary >= 100000 THEN 'High'
           WHEN salary >= 50000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_level
FROM employees;
```

### Basic structure

```sql
CASE
    WHEN condition THEN result
    WHEN condition THEN result
    ELSE result
END
```

---

# 15. NULL HANDLING

```sql
COALESCE(column, 'Default Value')
```

Example:

```sql
SELECT name,
       COALESCE(phone, 'Not Available') AS phone
FROM employees;
```

---

# 16. 📝 COMMON STRING FUNCTIONS

```sql
UPPER(name)
LOWER(name)
LENGTH(name)
TRIM(name)
CONCAT(first_name, last_name)
SUBSTRING(name, 1, 3)
```

---

# 17. 📅 DATE FUNCTIONS

Common concepts:

```text
CURRENT_DATE
CURRENT_TIMESTAMP
YEAR()
MONTH()
DAY()
DATEDIFF()
DATE_ADD()
```

⚠️ Exact syntax can differ between MySQL, PostgreSQL, SQL Server and Oracle.

---

# 18. 🏆 WINDOW FUNCTIONS

Used for ranking and calculations without collapsing rows.

### ROW_NUMBER

```sql
SELECT name, salary,
       ROW_NUMBER() OVER (
           ORDER BY salary DESC
       ) AS rn
FROM employees;
```

### RANK

```sql
RANK() OVER (ORDER BY salary DESC)
```

### DENSE_RANK

```sql
DENSE_RANK() OVER (ORDER BY salary DESC)
```

### Difference

```text
RANK:
1, 2, 2, 4

DENSE_RANK:
1, 2, 2, 3
```

---

# 19. 🔥 PARTITION BY

Ranking separately inside each group.

### Highest-paid employee in each department

```sql
ROW_NUMBER() OVER (
    PARTITION BY department
    ORDER BY salary DESC
)
```

Complete:

```sql
SELECT *
FROM (
    SELECT e.*,
           ROW_NUMBER() OVER (
               PARTITION BY department
               ORDER BY salary DESC
           ) AS rn
    FROM employees e
) x
WHERE rn = 1;
```

---

# 20. WITH — CTE

Used to make complicated queries easier.

```sql
WITH high_salary AS (
    SELECT *
    FROM employees
    WHERE salary > 50000
)
SELECT *
FROM high_salary;
```

### Multiple CTEs

```sql
WITH a AS (...),
     b AS (...)
SELECT ...
FROM a
JOIN b ON ...;
```

---

# 21. UNION

Combine results vertically.

```sql
SELECT name FROM employees
UNION
SELECT name FROM managers;
```

```text
UNION     → removes duplicates
UNION ALL → keeps duplicates
```

---

# 22. INSERT

```sql
INSERT INTO employees
(name, salary, department)
VALUES
('Piyush', 50000, 'IT');
```

---

# 23. UPDATE

```sql
UPDATE employees
SET salary = 60000
WHERE emp_id = 10;
```

⚠️ Without `WHERE`, all rows are updated.

---

# 24. DELETE

```sql
DELETE FROM employees
WHERE emp_id = 10;
```

⚠️ Without `WHERE`, all rows are deleted.

---

# 25. CREATE TABLE

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    department VARCHAR(50)
);
```

---

# 26. ALTER TABLE

```sql
ALTER TABLE employees
ADD email VARCHAR(100);
```

```sql
ALTER TABLE employees
DROP COLUMN email;
```

---

# 🧠 SQL QUESTION → WHAT SHOULD I USE?

```text
"What columns?"
        ↓
SELECT

"Which table?"
        ↓
FROM

"Another table?"
        ↓
JOIN + ON

"Which rows?"
        ↓
WHERE

"Per department/city/category?"
        ↓
GROUP BY

"Count / total / average?"
        ↓
COUNT / SUM / AVG / MAX / MIN

"Filter the groups?"
        ↓
HAVING

"Highest / lowest / top?"
        ↓
ORDER BY

"Only top 5?"
        ↓
LIMIT

"Greater than average?"
        ↓
SUBQUERY

"Exists / doesn't exist?"
        ↓
EXISTS / NOT EXISTS

"Rank?"
        ↓
RANK / DENSE_RANK / ROW_NUMBER

"Rank within each group?"
        ↓
PARTITION BY

"IF / ELSE?"
        ↓
CASE

"Complicated query?"
        ↓
CTE / WITH
```

---

# ⭐ THE MASTER SQL TEMPLATE

When you don't know where to start, write this:

```sql
SELECT ...
FROM ...
JOIN ...
    ON ...
WHERE ...
GROUP BY ...
HAVING ...
ORDER BY ...
LIMIT ...;
```

Then remove the parts you don't need.

---

# 🧠 LOGICAL SQL EXECUTION ORDER

Very important for understanding SQL:

```text
1. FROM
2. JOIN
3. ON
4. WHERE
5. GROUP BY
6. HAVING
7. SELECT
8. DISTINCT
9. ORDER BY
10. LIMIT
```

### Writing order:

```text
SELECT → FROM → JOIN → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

### Execution order:

```text
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

---

# 🔥 FINAL MASTER QUESTION

## Database

### employees

```text
emp_id
name
department_id
salary
hire_date
manager_id
```

### departments

```text
department_id
department_name
```

### projects

```text
project_id
project_name
department_id
budget
```

### employee_projects

```text
emp_id
project_id
hours_worked
```

---

## QUESTION

Write **one SQL query** that:

> Find the **top 2 highest-paid employees in each department**, showing their **name, department name, salary, salary category (High/Medium/Low), number of projects they worked on, and total hours worked**. Include departments even if they have no projects. Consider only employees whose salary is **greater than the overall average salary**. Show only departments having **at least 2 such employees**. Rank employees within each department by salary descending. If two employees have the same salary, rank them by name. Finally, sort the result by department name and salary descending.

### This single question tests:

```text
✅ SELECT
✅ FROM
✅ JOIN
✅ LEFT JOIN
✅ ON
✅ WHERE
✅ SUBQUERY
✅ AVG()
✅ GROUP BY
✅ HAVING
✅ COUNT()
✅ SUM()
✅ CASE WHEN
✅ COALESCE()
✅ CTE
✅ ROW_NUMBER()
✅ PARTITION BY
✅ ORDER BY
```

### Suggested approach:

```text
Step 1 → Calculate overall average salary
Step 2 → Filter employees above average
Step 3 → Join departments
Step 4 → Join projects
Step 5 → GROUP BY employee
Step 6 → COUNT projects + SUM hours
Step 7 → HAVING at least 2 employees per department
Step 8 → Create salary category using CASE
Step 9 → ROW_NUMBER() PARTITION BY department
Step 10 → Keep rank <= 2
Step 11 → ORDER BY department + salary
```

### 🔥 If you can solve this question without looking at the cheat sheet, you have a very strong foundation in SQL.
