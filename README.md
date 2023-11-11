# NewsGuadian
This is a machine Learning model on news prediction with complete interface of web (Using Flask)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/catiaspsilva/README-template">
    <img src="https://cdn-icons-png.flaticon.com/512/10729/10729305.png" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">NewsGuardian</h3>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#dependencies">Dependencies & Installations</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project leverages logistic regression, a powerful machine learning algorithm, to predict the authenticity of news articles—whether they are genuine or fake. Through the integration of Natural Language Processing (NLP) techniques, including the NLTK library, the model analyzes textual data to discern patterns and features indicative of misinformation.

## Key Features

* Logistic Regression Model: The core of this project utilizes logistic regression, a binary classification algorithm well-suited for discerning between real and fake news based on given features.
* NLP and NLTK Integration: Natural Language Processing is employed to extract meaningful insights from textual content. The NLTK library, a comprehensive toolkit for NLP tasks, enhances the model's understanding of language nuances.
* Accuracy and Reliability: The model is trained on a labeled dataset, honing its ability to make accurate predictions. Rigorous testing ensures the reliability of the predictions, making it a valuable tool for identifying misinformation.

<!-- GETTING STARTED -->
## Getting Started
``` bash
Clone the repository: git clone https://github.com/2003vivek/NewsGuardian.git
Install dependencies: pip install -r requirements.txt
Run the prediction script: python predict_fake_news.py
```

### Dependencies & Installations

* Scikit-learn library
  ```sh
  pip install sklearn
  ```
* Flask
  ```sh
  pip install flask
  ```
* nltk
  ```sh
  pip install nltk
  ```
<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
