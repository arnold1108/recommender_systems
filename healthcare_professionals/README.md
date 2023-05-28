# Recommender System for Matching HealthCare Professionals with Jobs Using Cosine Similarity 

A healthcare staffing company has the potential to offer a convenient platform that connects healthcare facilities with pre-screened healthcare professionals such as nurses and medical technicians. The platform could use an algorithm to match professionals with facilities based on their skills and availability, creating a staffing solution that operates similarly to Uber. The company's marketplace would allow facilities to post job opportunities with specific requirements and schedules, and pre-qualified healthcare professionals would be notified of relevant job openings. The first person to accept the job would be booked and paid for their services, eliminating the need for traditional staffing agencies and providing a more streamlined and cost-effective process.

The company could also offer a pitching service for facilities to select the best candidates for their job opportunities and provide workforce management tools to manage their entire workforce, including employees and contractors. The use of technology could create a comprehensive solution for healthcare staffing needs, offering flexibility and efficiency for both facilities and professionals. The company's innovative approach has the potential to transform the healthcare staffing industry.

In addition, the company could use machine learning systems to improve the healthcare staffing industry. The system would use advanced algorithms to match healthcare professionals with facilities based on their skill set, experience, and availability. A recommendation system, specifically collaborative filtering, could be used to analyze data points such as past job performance to make the most accurate and efficient matches.

This project aims to create a recommender system that matches healthcare professionals with job vacancies based on their skills, experience, and work preferences. The system uses cosine similarity to identify the most similar jobs to a given healthcare professional.

## The Model 
### Getting Started
The following instructions will help you run the project on your local machine.
#### Prerequisites
To run this project, you will need the following:
* Python 3
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-learn
#### Running the project
To run the project, open the ```recommender.ipynb``` file in Jupyter Notebook and run the cells.
### Data
The project generates synthetic data for healthcare professionals and job vacancies. The healthcare professionals' data include their ID, skills, location, certifications, education, skill level, work preferences, and experience. The job vacancies' data include their ID, required skills, location, required certifications, required education, required skill level, work preferences, and required experience.
### Collaborative Filtering
The project uses collaborative filtering to recommend job vacancies to healthcare professionals. Collaborative filtering is a technique that uses the behavior and preferences of a group of users to recommend items to an individual user. In this project, the behavior and preferences of healthcare professionals are used to recommend job vacancies.
### Results
The recommender system recommends the top 5 job vacancies that match a given healthcare professional based on their skills, experience, and work preferences. The project also includes a function that maps the job ID to the job title.
## Job Posting Web Application
This code provides a basic implementation of a Flask application that creates a Job board. It uses PostgresQL database for storing Job data. The job data consists of skill, location, certification_required, skill_level_required, experience_required, and work_prefernce attributes.
### Prerequisites
* Python 3.x
* Flask
* Flask_SQLAlchemy
* PostgreSQL
### Installation and Usage
1. Clone the repository to your local machine.
```
git clone https://github.com/<username>/job-posting-app.git
```
2. Install the required packages
```
pip install -r requirements.txt
```
3. Create a PostgreSQL database for the application.
4. Update the ```app.config['SQLALCHEMY_DATABASE_URI']``` value in app.py to match your database URI.
5. Start the Flask server.
```
python app.py
```
6. Access the web application in your browser at http://localhost:5000.
## Job Posting Form
The job posting form, created using html allows users to enter the following information:
* Skill 
* Location
* Certification Required
* Education Required
* Skill Level Required
* Experience Required
* Work Preference

## Job Posting List
The job posting list displays all the job postings that have been created. Each job posting is displayed with its corresponding information.
