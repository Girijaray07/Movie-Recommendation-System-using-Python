<h1 align="center">
  🎮✨ Movie Recommendation System ✨🎮
</h1>

<p align="center">
  <img src="https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif" width="200" alt="popcorn animation">
</p>

<p align="center">
  <b>Find your next favorite movie with AI-powered recommendations!</b>  
</p>

---

## 🧠 Project Overview

This project is a **content-based Movie Recommendation System** that suggests similar movies based on the user's chosen title.
It uses **machine learning** to understand movie attributes such as **genres, keywords, cast, and crew** — delivering personalized suggestions straight to your screen.

The backend is powered by **Flask** 🧩, while the core model is trained in a **Jupyter Notebook** using **Scikit-learn** and **NLTK**.
Currently, the **frontend is being developed** to beautifully display each recommended movie along with its **homepage link** 🌐.

---

## ⚙️ Features

✨ Recommends movies based on content similarity (genres, keywords, cast, and crew).
🎮 Simple and powerful REST API built with Flask.
📊 Jupyter Notebook for preprocessing, feature engineering, and model creation.
💮 Saves preprocessed data and similarity matrix using Pickle for quick loading.
💡 Frontend (in progress): displays recommended movies with their official links.

---

## 🧮 Technology Stack

| Layer                         | Technologies Used                            |
| ----------------------------- | -------------------------------------------- |
| 🎮️ **Backend**               | Python, Flask                                |
| 🧠 **Data Science / ML**      | Pandas, Scikit-learn, NLTK, Jupyter Notebook |
| 🎥 **Dataset**                | TMDB 5000 Movies Dataset                     |
| 💻 **Frontend (In Progress)** | HTML, CSS, JavaScript (or React)             |

---

## 🎮 Dataset

The system uses the **TMDB 5000 Movie Dataset**, consisting of:

* **tmdb_5000_movies.csv** → Movie details (title, overview, genres, etc.)
* **tmdb_5000_credits.csv** → Cast and crew details

📦 Both files are merged, cleaned, and processed in the notebook to build a rich movie feature database.

---

## 🤩 How It Works

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="300" alt="data flow animation">
</p>

1. **Data Processing & Model Training**

   * Run the `movie-recommend-system.ipynb` notebook.
   * Preprocesses and merges the datasets.
   * Extracts relevant movie features.
   * Uses **TF-IDF** or **CountVectorizer** for text vectorization.

2. **Similarity Calculation**

   * Computes a **cosine similarity matrix** between all movie pairs.

3. **Serialization**

   * Saves processed dataset and similarity matrix into `dataset_and_similarity.pkl`.

4. **Flask API Server**

   * `app.py` loads the pickled data and exposes `/recommend` endpoint.

5. **Recommendation Logic**

   * When a movie is requested, the API retrieves its similarity scores.
   * Returns **top 5 similar movies** along with their **homepage URLs**.

---

## 🚀 Setup & Usage

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Generate the Model

Run the Jupyter Notebook:

```bash
jupyter notebook movie-recommend-system.ipynb
```

This will create `dataset_and_similarity.pkl`, required by the Flask server.

### 3️⃣ Start the Backend Server

```bash
python app.py
```

The server runs locally at:
🔗 [http://127.0.0.1:5001](http://127.0.0.1:5001)

### 4️⃣ Get Recommendations

Make a GET request using your browser or Postman:

```
http://127.0.0.1:5001/recommend?movie=Avatar
```

You’ll receive a list of 5 similar movies with their homepage links 🎮️

---

## 💻 Frontend (Work in Progress)

🎨 The frontend is under development to:

* Take user input (movie title)
* Fetch recommendations from the Flask API
* Display movie posters, titles, and homepage links in a clean, animated interface

<p align="center">
  <img src="https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif" width="250" alt="UI development animation">
</p>

---

## 🌟 Example Output

**Input:**
`Avatar`

**Output (Top 5 Recommendations):**

| Movie                   | Homepage                                                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| Guardians of the Galaxy | [https://www.marvel.com/movies/guardians-of-the-galaxy](https://www.marvel.com/movies/guardians-of-the-galaxy) |
| The Fifth Element       | [https://www.sonypictures.com/movies/thefifthelement](https://www.sonypictures.com/movies/thefifthelement)     |
| Star Trek               | [https://www.startrek.com/](https://www.startrek.com/)                                                         |
| John Carter             | [https://movies.disney.com/john-carter](https://movies.disney.com/john-carter)                                 |
| Interstellar            | [https://www.interstellarmovie.net/](https://www.interstellarmovie.net/)                                       |

---

## 💡 Future Enhancements

🔹 Integrate a movie poster & trailer preview. 
🔹 Add collaborative filtering for user-personalized recommendations. 
🔹 Deploy on Render / Vercel for live demo access. 
🔹 Improve UI with React + Tailwind + Framer Motion. 

---

## 🧑‍💻 Author

👤 **Girija Shankar Ray**
🎥 Web Developer & ML Enthusiast
🌐 [LinkedIn]( https://www.linkedin.com/in/girija-shankar-ray/) | [GitHub](https://github.com)

---

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="250" alt="thanks animation">
</p>

<h3 align="center">
  ⭐ If you like this project, give it a star and share the magic of movies! ⭐
</h3>