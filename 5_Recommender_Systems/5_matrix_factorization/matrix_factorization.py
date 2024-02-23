#############################
# Model-Based Collaborative Filtering: Matrix Factorization
#############################

# User-Based Collaborative Filtering, kullanıcı benzerliğine dayanırken, Model-Based Matrix Factorization öğrenilmiş bir modeli kullanır.

# Matrixteki / dataframedeki null değerleri yani boşlukları doldurmayı hedefliyoruz.
# Boşlukları doldurmak için, user lar ve movie ler için var olduğu varsayılan gizli feature ların ağırlıkları var olan ver üzerinden bulunur
# ve bu ağırlıklar ile var olmayan gözlemler için tahmin yapılır.

# Matris Çarpanlarına Ayırma (Matrix Factorization) : Veriyi matrislere bölmek için kullanılır.
# Bu yöntem, bir veri matrisini iki veya daha fazla alt matrise ayırarak karmaşık veri yapılarını daha basit parçalara böler.
# Bu parçalar daha sonra yeniden birleştirilerek orijinal veri matrisi yeniden oluşturulabilir.
# Matrix Factorization özellikle öneri sistemleri gibi alanlarda kullanılır.

# Filmlere puan verilme kriterleri: rating, user factors, movie factors
# Öyle p ve q değerleri oluşturmalıyızki, bu tahminler ve gerçek değerler arasındaki farkların kareleri arasındaki fark mınimum olsun
# Sonra bu p ve q lar ile matrix teki boş yerleri doldururuz.

# !pip install surprise
import pandas as pd
from surprise import Reader, SVD, Dataset, accuracy
from surprise.model_selection import GridSearchCV, train_test_split, cross_validate
pd.set_option('display.max_columns', None)


# PROJE ADIMLARI
# Adım 1: Veri Setinin Hazırlanması
# Adım 2: Modelleme
# Adım 3: Model Tuning
# Adım 4: Final Model ve Tahmin



#############################
# Adım 1: Veri Setinin Hazırlanması
#############################

# Gradyan İniş (Gradient Descent), bir optimizasyon algoritmasıdır ve çeşitli optimizasyon problemlerini çözmek için kullanılır. (Doğrusal regresyon analizi.)
# Temel amaç, bir fonksiyonun minimum veya maksimum noktasını bulmaktır.
# Bir fonksiyonun türevi, o fonksiyonun artış yönünü verir.

movie = pd.read_csv('datasets/movie_lens_dataset/movie.csv')
rating = pd.read_csv('datasets/movie_lens_dataset/rating.csv')
df = movie.merge(rating, how="left", on="movieId")
df.head()

# 4 film ile ilerleyelim
movie_ids = [130219, 356, 4422, 541]
movies = ["The Dark Knight (2011)",
          "Cries and Whispers (Viskningar och rop) (1972)",
          "Forrest Gump (1994)",
          "Blade Runner (1982)"]

sample_df = df[df.movieId.isin(movie_ids)]
sample_df.head()

sample_df.shape  # (97343, 6)

# kullanıcı-film matrisi oluşturalım:
user_movie_df = sample_df.pivot_table(index=["userId"],
                                      columns=["title"],
                                      values="rating")

user_movie_df.shape  # (76918, 4)


# Surprise kütüphanesini kullanarak öneri sistemleri için hazır bir veri seti oluşturalım.
# İlk olarak, Reader sınıfını kullanarak puan ölçeğini (burada 1 ile 5 arasında) belirliyoruz.
reader = Reader(rating_scale=(1, 5))

# Dataset.load_from_df yöntemini kullanarak sample_df'den gerekli sütunları (userId, movieId ve rating) seçiyoruz
# ve bu veriyi önceki adımda belirlediğimiz Reader nesnesiyle birlikte bir Dataset nesnesine yüklüyoruz.
data = Dataset.load_from_df(sample_df[['userId',
                                       'movieId',
                                       'rating']], reader)




##############################
# Adım 2: Modelleme
##############################

# Modelleme (Modeling) aşaması: Model oluşturmayı ifade eder ve sınıflandırma, regresyon ve kümeleme gibi birçok görevi içerir.

# Veriyi Train ve Test olarak ayıralım
trainset, testset = train_test_split(data, test_size=.25) # verinin %25'ini test kümesi olarak ayıralım

svd_model = SVD()                         # SVD tabanlı bir model oluşturalım
svd_model.fit(trainset)                   # fit yöntemi ile, Train veri seti üzerinde modeli eğitelim
predictions = svd_model.test(testset)     # test yöntemi ile, Test veri seti üzerinde tahminler yapalım

# accuracy.rmse fonksiyonu, train ve test işlemlerini gerçekleştirerek SVD modelinin performansını RMSE metriği ile değerlendirir.
# RMSE(Root Mean Squared Error), tahminlerin gerçek değerlere ne kadar yakın olduğunu ölçen bir performans metriğidir.
accuracy.rmse(predictions)
# RMSE: 0.9365


svd_model.predict(uid=1.0, iid=541, verbose=True)
# Prediction(uid=1.0, iid=541, r_ui=None, est=4.1690940205274565, details={'was_impossible': False})

svd_model.predict(uid=1.0, iid=356, verbose=True)
# Prediction(uid=1.0, iid=356, r_ui=None, est=3.9748372742483338, details={'was_impossible': False})

sample_df[sample_df["userId"] == 1]
#          movieId                title                  genres  userId  rating            timestamp
# 3612352      541  Blade Runner (1982)  Action|Sci-Fi|Thriller     1.0     4.0  2005-04-02 23:30:03




##############################
# Adım 3: Model Tuning
##############################

# Model Kurma (Model Tuning): Modelin hiperparametrelerini ayarlama ve performansını iyileştirme işlemidir.

# Modeli GridSearchCV ile optimize edelim.

#  Hiperparametre arama alanını belirleyen bir sözlüktür.
#  n_epochs ve lr_all (learning rate) hiperparametreleri için belirlenen değerler listelenir.
param_grid = {'n_epochs': [5, 10, 20],
              'lr_all': [0.002, 0.005, 0.007]}


gs = GridSearchCV(SVD,
                  param_grid,                 # SVD modeli için bir grid search yapısı oluşturur.
                  measures=['rmse', 'mae'],   # Performans ölçümlerini belirler. Burada 'rmse' ve 'mae' (Mean Absolute Error) ölçümleri kullanılmıştır.
                  cv=3,                       # Bu durumda, 3 katsayılı çapraz doğrulama yapılmıştır.
                  n_jobs=-1,                  # -1 değeri, mevcut tüm işlemcilerin kullanılmasını sağlar.
                  joblib_verbose=True)        # Grid search işlemi sırasında kullanılan iş parçacığı hakkında ayrıntılı çıktı sağlar.


# fit: Grid search'i gerçekleştiren ve en iyi hiperparametreleri bulan fonksiyondur.
gs.fit(data)

# En iyi RMSE değerini verir.
gs.best_score['rmse']  # 0.9309

# En iyi RMSE değerine karşılık gelen en iyi hiperparametreleri içeren bir sözlük döndürür.
gs.best_params['rmse'] # {'n_epochs': 5, 'lr_all': 0.002}




##############################
# Adım 4: Final Model ve Tahmin
##############################

# Son modelin seçilmesi ve gerçek verilerle tahminlerin yapılmasını ifade eder.

# dir(svd_model) yöntemi, bir nesnenin içinde bulunan özelliklerin (attributes) ve yöntemlerin (methods) listesini döndürür.
# Bu özellikler ve yöntemler, nesnenin özelliklerini, davranışlarını ve üzerinde çalışabileceğiniz işlevleri temsil eder.
dir(svd_model)

# SVD modelinin eğitimi sırasında kullanılan döngü sayısını (epoch) verir.
svd_model.n_epochs

# bulunan en iyi parametreler kullanılır.
svd_model = SVD(**gs.best_params['rmse'])


# eğitim verisi tam bir eğitim setine dönüştürülür.
data = data.build_full_trainset()

# bu tam eğitim seti üzerinde svd_model.fit(data) kullanılarak SVD modeli eğitilir.
svd_model.fit(data)


# Bu, modelin tüm eğitim verisi üzerinde eğitilmesini sağlar ve daha sonra bu eğitilmiş modelle tahminler yapabilirsiniz.
svd_model.predict(uid=1.0, iid=541, verbose=True)






