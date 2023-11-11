from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from flask import Flask,render_template,request

df=pd.read_csv('fake_or_real_news.csv')

nltk.download('stopwords')
print(stopwords.words('english'))

df.isnull().sum()
df=df[['title','text','label']]

label=pd.get_dummies(df['label'])

df=pd.concat([df,label],axis='columns')
df=df.drop(['label','REAL'],axis='columns')

stem=PorterStemmer()
def stemmer(content):
    stem_con=re.sub('[^a-zA-Z]',' ',content)
    stem_con=stem_con.lower()
    stem_con=stem_con.split()
    stem_con=[stem.stem(word) for word in stem_con if not word in stopwords.words('english') ]
    stem_con=' '.join(stem_con)
    return stem_con

X=df['title'] + " "+ df['text']
df['content']=X
df['content']=df['content'].apply(stemmer)

X=df['content']
y=df['FAKE']
X

lr=LogisticRegression()
cv=TfidfVectorizer()
x_vectorized=cv.fit_transform(X)
X_train,X_test,y_train,y_test=train_test_split(x_vectorized,y,test_size=0.2,random_state=2,stratify=y)

lr.fit(X_train,y_train)


def predict(i):
    tr=cv.transform([i])
    inp=lr.predict(tr)
    return inp[0]


app=Flask(__name__)
@app.route("/")
def apps():
    if request.method=="POST":
        news=request.form.get('news')
        
        if news:
            pred=predict(news)
            
    return render_template("home.html",predi=pred)

if __name__=='__main__':
    app.run()
    