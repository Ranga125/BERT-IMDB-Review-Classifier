<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1><strong>IMDB-BERT Sentiment Analyzer 🎮🤖</strong></h1>

<h2><strong>Overview</strong></h2>
<p>IMDB-BERT Sentiment Analyzer is a <strong>text classification project</strong> that utilizes a <strong>fine-tuned BERT model</strong> to classify IMDB movie reviews as <strong>Positive</strong> or <strong>Negative</strong>. The model is deployed as a <strong>Streamlit web application</strong> for real-time sentiment analysis.</p>

<hr>

<h2><strong>Project Structure</strong></h2>
<pre>
IMDB-BERT-Sentiment-Analyzer/
👉 app.py                  # Streamlit web application  
👉 bert_model.pkl          # Trained BERT model (saved from Colab using Pickle)  
👉 requirements.txt        # Dependencies for the project  
👉 README.md               # Project documentation  

</pre>

<hr>

<h2><strong>Installation & Setup</strong></h2>

<h3><strong>1️⃣ Clone the Repository</strong></h3>
<pre>
git clone https://github.com/Ranga125/IMDB-BERT-Sentiment-Analyzer.git
cd IMDB-BERT-Sentiment-Analyzer
</pre>

<h3><strong>2️⃣ Create a Virtual Environment & Install Dependencies</strong></h3>
<pre>
pip install -r requirements.txt
</pre>

<h3><strong>3️⃣ Run the Streamlit App</strong></h3>
<pre>
streamlit run app.py
</pre>

<hr>

<h2><strong>Model Details</strong></h2>
<ul>
    <li>Pre-trained <strong>BERT</strong> model fine-tuned on IMDB movie reviews dataset</li>
    <li>Tokenization using <strong>Hugging Face’s BertTokenizer</strong></li>
    <li>Classification outputs: <strong>Positive (1) / Negative (0)</strong></li>
</ul>

<hr>

<h2><strong>Usage</strong></h2>
<ol>
    <li>Enter a movie review in the text box</li>
    <li>Click the <strong>Predict</strong> button</li>
    <li>Get sentiment classification output: <strong>Positive</strong> or <strong>Negative</strong></li>
</ol>

<hr>

<h2><strong>Contributing</strong></h2>
<p>Feel free to fork this repository, create a new branch, and submit a pull request! 🚀</p>

<hr>



</body>
</html>
