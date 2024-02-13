############################################
# Sorting Reviews (Müşteri yorumlarının sıralanması)
############################################

# Yorumun veya ürünün düşük/yüksek puanlı olmasıyla ilgilenmiyoruz. Kullanıcıya, en faydalı sonucu ulaştırmaya çalışıyoruz.
# Örneğin, 300 kişinin faydalı bulduğu bir yorumun, en tepede gösterilmesi gibi..


# 1) Up-Down Difference Score = (up ratings) − (down ratings)
# 2) Average Rating Score = (up ratings) / (all ratings)
# 3) Wilson Lower Bound Score



import pandas as pd
import math
import scipy.stats as st

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)



###################################################
# 1)  Up-Down Difference Score = (up ratings) − (down ratings)
###################################################

# Yorumlardaki beğeni sayısına göre sıralama yapar.

def score_up_down_diff(up, down):
    return up - down

# Review 1 Score:
score_up_down_diff(600, 400)

# Review 2 Score
score_up_down_diff(5500, 4500)




###################################################
# 2) Average Rating Score = (up ratings) / (all ratings)
###################################################

def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)

score_average_rating(600, 400)     # 0.6
score_average_rating(5500, 4500)   # 0.55




###################################################
# 3) Wilson Lower Bound Score
###################################################

# WLB Skoru, ürün veya yorum sıralamalarında kullanılan istatistiksel bir yöntemdir.
# Yoruma ait puanı ve yorum yapan "müşterinin yorum sayısını da dikkate alarak" sıralama yapar. Müşterinin yorum sayısı, yorumun ne kadar güvenilir olduğunu belirtir. !
# Wilson Lower Bound yöntemi, yorumların güvenilirliği ve puanların istatistiksel olarak anlamlı olup olmadığını değerlendirmek için Bayes Teoremi matematiksel formülünden faydalanır.

def wilson_lower_bound(up, down, confidence=0.95):
    """
    Wilson Lower Bound Score hesapla

    - Bernoulli parametresi p için hesaplanacak güven aralığının alt sınırı WLB skoru olarak kabul edilir.
    - Hesaplanacak skor ürün sıralaması için kullanılır.
    - Not:
    Eğer skorlar 1-5 arasıdaysa 1-3 negatif, 4-5 pozitif olarak işaretlenir ve bernoulli'ye uygun hale getirilebilir.
    Bu beraberinde bazı problemleri de getirir. Bu sebeple bayesian average rating yapmak gerekir.

    Parameters
    ----------
    up: int
        up count
    down: int
        down count
    confidence: float
        confidence

    Returns
    -------
    wilson score: float

    """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)

# Yani 600 adet up ratings ve 400 adet down ratings yorumu icin, bu yorumları yapan müşterilerin, yorum sayısını da baz alarak wilson_lower_bound score u üretilir.
wilson_lower_bound(600, 400)     # 0.56
wilson_lower_bound(5500, 4500)   # 0.54

wilson_lower_bound(2, 0)         # 0.34
wilson_lower_bound(100, 1)       # 0.94







###################################################
# Case Study
###################################################

# Comments isimli dataframede, yorumlar için up ratings ve down ratings sayıları yer almaktadır:
up = [15, 70, 14, 4, 2, 5, 8, 37, 21, 52, 28, 147, 61, 30, 23, 40, 37, 61, 54, 18, 12, 68]
down = [0, 2, 2, 2, 15, 2, 6, 5, 23, 8, 12, 2, 1, 1, 5, 1, 2, 6, 2, 0, 2, 2]
comments = pd.DataFrame({"up": up, "down": down})


#########
# 1) Up-Down Difference Score = (up ratings) − (down ratings)
#########
def score_up_down_diff(up, down):
    return up - down

# Üstte oluşturduğumuz fonksiyonu uygulatarak, Dataframe de yeni bir sütun oluşturalım.
comments["score_pos_neg_diff"] = comments.apply(lambda x: score_up_down_diff(x["up"], x["down"]), axis=1)




#########
# 2) Average rating Score = (up ratings) / (all ratings)
#########
def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)

# Üstte oluşturduğumuz fonksiyonu uygulatarak, Dataframe de yeni bir sütun oluşturalım.
comments["score_average_rating"] = comments.apply(lambda x: score_average_rating(x["up"], x["down"]), axis=1)




#########
# 3) Wilson Lower Bound Score
#########
def wilson_lower_bound(up, down, confidence=0.95):
    """
    Wilson Lower Bound Score hesapla

    - Bernoulli parametresi p için hesaplanacak güven aralığının alt sınırı WLB skoru olarak kabul edilir.
    - Hesaplanacak skor ürün sıralaması için kullanılır.
    - Not:
    Eğer skorlar 1-5 arasıdaysa 1-3 negatif, 4-5 pozitif olarak işaretlenir ve bernoulli'ye uygun hale getirilebilir.
    Bu beraberinde bazı problemleri de getirir. Bu sebeple bayesian average rating yapmak gerekir.

    Parameters
    ----------
    up: int
        up count
    down: int
        down count
    confidence: float
        confidence

    Returns
    -------
    wilson score: float

    """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)

# Üstte oluşturduğumuz fonksiyonu uygulatarak, Dataframe de yeni bir sütun oluşturalım.
comments["wilson_lower_bound"] = comments.apply(lambda x: wilson_lower_bound(x["up"], x["down"]), axis=1)


comments.sort_values("wilson_lower_bound", ascending=False)








