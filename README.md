# 🎬 Movie Recommender System

A content-based machine learning web application that recommends movies based on user preferences. By analyzing movie metadata—such as plot overviews, genres, cast, and crew—this system calculates the similarity between films and suggests the top 5 closest matches to your selection.

## 🚀 Features
* **Content-Based Filtering:** Uses Natural Language Processing (NLP) to understand and compare movie themes and cast data.
* **Interactive UI:** A clean, easy-to-use web interface built with Streamlit.
* **Pre-computed Models:** Utilizes serialized pickle files for fast, real-time recommendations.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning & NLP:** Scikit-learn (CountVectorizer, Cosine Similarity), NLTK (PorterStemmer)
* **Frontend:** Streamlit

## 📁 Project Structure
```angular2html
      movie_recommender/
   ├── data/
   │   └── final_data.csv
   ├── notebook/
   │   ├── model.ipynb
   │   └── movie_clean_data.ipynb
   ├── script/
   │   └── app.py
   ├── README.md
   └── requirement.txt
```

## ⚙️ Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-directory>
   ```

2. **Install the required dependencies:**
    ```bash
    pip install pandas numpy scikit-learn nltk streamlit scipy
    ```

3. **Run the Data Pipeline (Optional):**
    If you want to train the model from scratch, run the Jupyter notebooks in order:

    First, execute movie_clean_data.ipynb to generate final_data.csv.

    Next, execute model.ipynb to generate similarity_distance.pkl and final_data.pkl.

4. **Launch the Web App:**
    ```bash
    streamlit run app.py
    ```
   

