import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from joblib import dump

def training():
    # CSV 파일 읽기
    df = pd.read_csv('sc_dataset2.csv')  
    
    # 결측값이 포함된 행 제거
    df.dropna(inplace=True)

    # 또는 결측값을 다른 값으로 채우기
    # 예: 'unknown'
    # df.fillna('unknown', inplace=True)

    # 데이터 준비
    X = df['hard_word']  # 독립 변수 (입력)
    y = df['easy_word']  # 종속 변수 (예측 대상)

    # 학습 데이터와 테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 모델 파이프라인 구축: 텍스트 벡터화 및 분류 모델
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # 모델 학습
    model.fit(X_train, y_train)

    # 모델 평가
    print("테스트 세트 점수: {:.2f}".format(model.score(X_test, y_test)))

    dump(model, 'model.joblib')

    return model