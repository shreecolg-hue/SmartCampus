# SmartCampus

# 🎓 Smart Campus Information System

A multi-functional web application built using **Streamlit** that integrates essential academic management modules into a single platform. This project demonstrates the use of Python for building interactive data-driven applications with real-world use cases.

---

## 📌 Overview

The **Smart Campus Information System** is designed to simulate a digital academic environment where users can manage student data, course enrollment, file handling, and performance analytics. The application uses an intuitive UI with a sidebar-based navigation system for seamless module switching.

---

## 🚀 Features

### 🏠 Dashboard

* Displays key metrics such as number of students, courses, IDs, and records
* Shows recent student activity

### 📝 Grade Evaluation

* Accepts student name and score
* Assigns grades based on predefined criteria
* Stores and displays student records

### 📚 Course Enrollment

* Add courses with credit values
* Limit of 5 courses per session
* Calculates total enrolled credits

### 🗃️ Student Records

* Stores student details (name, age, grades)
* Calculates average marks
* Implements **set operations** for event participation:

  * Intersection (common participants)
  * Union (all participants)
  * Difference (exclusive participants)

### 🔍 Sort & Search IDs

* Maintains student ID list
* Sorts IDs automatically
* Searches IDs efficiently using indexed lookup

### 💰 Fee Calculator

* Computes total fees based on:

  * Tuition
  * Hostel
  * Transport
* Displays breakdown and total cost

### 📂 File Records

* Saves student records to CSV file
* Loads and displays stored data
* Demonstrates **file handling operations**

### 📁 Directory Scanner

* Scans and displays folder structure
* Uses **OS module traversal**
* Handles invalid paths with error messages

### 📊 Performance Analytics

* Upload CSV dataset
* Performs statistical analysis using:

  * **NumPy** (mean, median, standard deviation)
  * **Pandas** (data summary)
* Identifies top performers
* Visualizes data using built-in charts

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** (UI framework)
* **Pandas** (data manipulation)
* **NumPy** (numerical analysis)
* **OS & Tempfile** (file system handling)

---

## 📂 Project Structure

* Single Python file containing:

  * UI components
  * Business logic
  * Data processing functions
* Session-based storage using Streamlit session state

---


## 📈 Learning Outcomes

* Understanding of **interactive web app development** using Streamlit
* Application of **data structures** like lists, dictionaries, and sets
* Implementation of **file handling and directory traversal**
* Use of **data analysis libraries** for real-time insights
* Integration of multiple modules into a single system

---

## 📌 Conclusion

This project demonstrates how Python can be used beyond scripting to build full-fledged applications that combine UI, data processing, and analytics. It serves as a strong foundation for developing real-world systems such as campus management platforms.


