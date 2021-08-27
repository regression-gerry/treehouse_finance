CREATE TABLE Employees (
    id int,
    Name varchar(20),
    Salary int,
    manager_id int
);

INSERT INTO Employees (id, Name, Salary, manager_id) VALUES (1, 'John', 300, 3);
INSERT INTO Employees (id, Name, Salary, manager_id) VALUES (2, 'Mike', 200, 3);
INSERT INTO Employees (id, Name, Salary, manager_id) VALUES (3, 'Sally', 550, 4);
INSERT INTO Employees (id, Name, Salary, manager_id) VALUES (4, 'Jane', 500, 7);
INSERT INTO Employees (id, Name, Salary, manager_id) VALUES (5, 'Joe', 600, 7);
INSERT INTO Employees (id, Name, Salary, manager_id) VALUES (6, 'Dan', 600, 3);
INSERT INTO Employees (id, Name, Salary, manager_id) VALUES (7, 'Phil', 550, null);

-- 1 a.
SELECT *
FROM Employees one,
     Employees two
WHERE one.manager_id = two.id
  AND one.salary > two.salary;
-- Dan, Joe, Sally

-- 1 b.
SELECT AVG(Salary)
FROM Employees
WHERE id in (
    SELECT id
	FROM   Employees e1
	WHERE not exists (select id from Employees e2 where e2.manager_id = e1.id)
)
-- Average salary = 425