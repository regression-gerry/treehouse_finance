
-- a. 
SELECT *
FROM Employees one,
     Employees two
WHERE one.manager_id = two.id
  AND one.salary > two.salary;

-- Dan, Joe, Sally

-- b.

SELECT AVG(Employees.Salary)
FROM Employees
WHERE id not in (
    SELECT manager_id 
    FROM Employees
)
-- Average salary = 425