USE college_clubs;

-- Insert a new student
INSERT INTO Student VALUES (8, 'Rita', 'rita@email.com');

-- Insert a new club
INSERT INTO Club VALUES (5, 'Art Club', 'R404', 'Ms. Laxmi');

-- Display all students
SELECT * FROM Student;

-- Display all clubs
SELECT * FROM Club;

-- JOIN query: Student Name, Club Name, Join Date
SELECT 
    s.StudentName,
    c.ClubName,
    m.JoinDate
FROM Membership m
JOIN Student s ON m.StudentID = s.StudentID
JOIN Club c ON m.ClubID = c.ClubID;

