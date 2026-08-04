# 🎬 Movie Recommendation System
A content-based Movie Recommendation System built with Python, Machine Learning, and Streamlit. The application recommends movies similar to the one selected by the user using natural language processing and cosine similarity.


## 📌 Overview
Finding movies that match a user's interests can be challenging with thousands of titles available. This project solves that problem by recommending movies based on their content rather than user ratings.

The recommendation engine analyzes movie metadata such as genres, keywords, cast, crew, and overview to identify movies with similar characteristics.

The application provides an interactive web interface where users can select a movie and instantly receive personalized recommendations.


## 🚀 Live Demo
Add your deployed Streamlit link here after deployment.

https://movie-recommender-system0925.streamlit.app/


## 📷 Application Preview
Add screenshots of your application inside the assets/ folder and display them here.

assets/
│── recommendations.png

Example:
<img width="1337" height="651" alt="recommendations" src="https://github.com/user-attachments/assets/c96f3308-2f93-44dc-8761-44edcaa4866c" />

## ✨ Features
Content-based movie recommendation
Interactive Streamlit web application
Fast recommendation generation
Movie selection using searchable dropdown
Top similar movie recommendations
Clean and user-friendly interface
Machine Learning powered recommendation engine


# 🛠️ Technologies Used
### Programming Language
- Python
### Libraries
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle
### Machine Learning
- CountVectorizer
- Cosine Similarity
- NLP Text Processing


# 📂 Project Structure
Movie-Recommender-System/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── movie_recommender.ipynb
│
└── assets/
    └── recommendations.png

# ⚙️ How It Works
### Step 1 – Data Collection
Movie metadata is collected from the TMDB Movie Dataset.
The dataset includes information such as:
- Movie title
- Genres
- Cast
- Crew
- Keywords
- Overview

### Step 2 – Data Preprocessing
The raw dataset is cleaned and transformed.
Operations performed include:

- Removing missing values
- Extracting genres
- Extracting top cast members
- Extracting director information
- Combining textual features
- Text normalization
- Stemming using NLTK PorterStemmer


### Step 3 – Feature Engineering
All textual information is combined into a single feature called tags.
Example:
Action Adventure Tom_Cruise Christopher_McQuarrie Mission Impossible

### Step 4 – Vectorization
The tags are converted into numerical vectors using:
CountVectorizer
Parameters used:
- max_features = 3000
- stop_words = "english"

### Step 5 – Similarity Calculation

Cosine Similarity is used to calculate similarity between movie vectors.

Movies with the highest similarity scores are recommended to the user.


# 💡 Future Improvements
- User authentication
- Hybrid recommendation system
- Collaborative filtering
- Movie posters using TMDB API
- Search autocomplete
- Genre-based filtering
- Ratings integration
- Deployment using Docker
- Recommendation explanation
- User watchlist

# 📈 Skills Demonstrated
- Data Cleaning
- Feature Engineering
- Natural Language Processing
- Machine Learning
- Recommendation Systems
- Streamlit Development
- Python Programming
- Git & GitHub
- Model Serialization using Pickle

# 📄 License
This project is developed for educational and portfolio purposes.

# 👨‍💻 Author
Mohd Anas

GitHub: https://github.com/mohdanas925

If you found this project useful, consider giving the repository a ⭐.
