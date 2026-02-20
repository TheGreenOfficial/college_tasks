CREATE DATABASE IF NOT EXISTS college_clubs;
USE college_clubs;

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL
);

CREATE TABLE Club (
    ClubID INT PRIMARY KEY,
    ClubName VARCHAR(50) NOT NULL,
    ClubRoom VARCHAR(20),
    ClubMentor VARCHAR(50)
);

CREATE TABLE Membership (
    StudentID INT,
    ClubID INT,
    JoinDate DATE,
    PRIMARY KEY (StudentID, ClubID),
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClubID) REFERENCES Club(ClubID)
);

