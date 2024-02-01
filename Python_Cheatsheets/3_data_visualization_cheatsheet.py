##########################################################################
# DATA VISUALIZATION WITH PYTHON : SEABORN
##########################################################################
import pandas as pd
import numpy as np
import random

import seaborn as sns
from matplotlib import pyplot as plt
from pandas._config import display

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 500)
pd.set_option("display.precision", 2)
pd.set_option("display.width", 500)

# Sample tech product names
product_names = [
    "iPhone 13 Pro Max", "Samsung Galaxy S21 Ultra", "Dell XPS 13", "HP Spectre x360", "Sony PlayStation 5",
    "MacBook Pro", "Google Pixel 6", "Microsoft Surface Pro 8", "iPad Air", "Samsung Galaxy Tab S7",
    "Apple Watch Series 7", "Sony WH-1000XM4", "Dell Alienware M15", "HP Omen 15", "Microsoft Xbox Series X"
]

# Generating sample data
data = {
    "quantity": np.random.randint(1, 10, size=1000),
    "sku": [f"SKU{i}" for i in range(1, 1001)],
    "unit_price": np.random.randint(50, 500, size=1000),
    "date": pd.date_range(start='2023-01-01', periods=1000),
    "name": random.choices(product_names, k=1000),
    "price": np.random.randint(100, 1000, size=1000),
    "subcategory": [random.choice(["Laptop", "Smartphone", "Tablet", "Smartwatch"]) for _ in range(1000)],
    "category": "Technology",
    "brand": [random.choice(["Apple", "Samsung", "Dell", "HP", "Sony", "Google", "Microsoft"]) for _ in range(1000)],
    "revenue": np.random.randint(500, 5000, size=1000),
    "discount": np.random.randint(0, 100, size=1000),
    "discount_rate": np.random.uniform(0, 0.5, size=1000),
    "discount_range": [random.choice(["Low", "Medium", "High"]) for _ in range(1000)]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Increase values for "Apple" and "Samsung" brands
df.loc[df['brand'].isin(["Apple", "Samsung"]), :] *= 1.2
# Increase values for "Laptop" and "Smartphone" subcategories
df.loc[df['subcategory'].isin(["Laptop", "Smartphone"]), :] *= 1.2

# Adding month and year columns
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

df.head()





# 1) countplot / barplot       : Kategorik değişkenlerde !
# 2) pie chart / donut chart   : Kategorik değişkenlerde !
# 3) grouped countplot         : Kategorik değişkenlerde !
# 4) histogram                 : Sayisal değişkenlerde !
# 5) boxplot                   : Sayisal değişkenlerde !
# 6) lineplot                  : Sayisal değişkenlerde !




##########################################################################
# 1) countplot / barplot : BRAND BASED BREAKDOWNS
##########################################################################

##### 1. YOL | countplot : sadece x="brand" tanimlayabiliriz. Bu da bize brand e ait quantity leri getirir.

# Markalari quantity e gore buyukten kucuge siralamak icin:
quantity_ranking = df['brand'].value_counts().sort_values(ascending=False)


# Sutun satir boyutlari
plt.figure(figsize=(12, 12))

# Font bilgileri
sns.set(font_scale=1.5)
sns.set_style("white")

# Grafik bilgileri
sns.countplot(data=df,
              x="brand",
              order=quantity_ranking.index,  # markaları sıralı olarak belirtir
              palette="viridis")

# Baslik bilgileri
plt.title("Product Quantity by Brand", fontsize=25)
plt.xlabel('Brand', fontsize=22)
plt.ylabel('Product quantity', fontsize=22)
plt.xticks(rotation=45)  # x eksenindeki etiketleri 45 derece döndürür

plt.show()




##### 2. YOL | barplot : x="brand" ve ek olarak y="revenue" / "price" tanimlayabiliriz. Bu da bize brand e ait revenue/price lari getirir.

# Markalari revenue ya gore buyukten kucuge siralamak icin:
revenue_ranking = df.groupby("brand").agg({"revenue": "sum"}).sort_values(by="revenue", ascending=False)

# Satir sutun boyutlari
plt.figure(figsize=(12, 12))

# Font bilgileri
sns.set(font_scale=1.5)
sns.set_style("white")

# Grafik bilgileri
sns.barplot(data=df,
            x="brand",
            y="revenue",
            order=revenue_ranking.index,
            palette="viridis")

# Baslik bilgileri
plt.title("Total Revenue by Brand", fontsize=25)
plt.xlabel('Brand', fontsize=22)
plt.ylabel('Total Revenue', fontsize=22)
plt.xticks(rotation=45)       #x eksenindeki  etiketleri 45 derece döndür

plt.show()





##########################################################################
### 2) pie chart : BRAND BASED BREAKDOWNS
##########################################################################
###  Kategorik değişkenlerde, sınıf sayısı fazla ise Pie chart anlamsız olur, bar plot daha mantıklıdır.

# Satir sutun boyutlari
# Font bilgileri
fig = plt.figure(figsize=(6, 5))
sns.set(font_scale=1.2)

# Brand bazında toplam miktarları hesaplayalım
brand_quantity = df.groupby('brand')['quantity'].sum()

# Pie chart için renkler belirleyelim
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink', 'orange']

# Bazı dilimleri vurgulamak için explode listesi oluşturalım
explode = (0, 0, 0, 0, 0.1, 0, 0)    # Microsoft dilimini vurgulayalım, 4. indexte

# Pie chart oluşturalım
plt.pie(brand_quantity,
        labels=brand_quantity.index,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        startangle=140)


# Baslik bilgileri
plt.axis('equal')  # Dairesel çizim sağlar
plt.title("Brand Based Quantities", fontsize=20)
plt.show()


##########################################################################
### BONUS : donut chart : BRAND BASED BREAKDOWNS

# Satir sutun boyutlari
# Font bilgileri
fig = plt.figure(figsize=(6, 5))
sns.set(font_scale=1.2)

# Brand bazında toplam miktarları hesaplayalım
brand_quantity = df.groupby('brand')['quantity'].sum()

# Pie chart için renkler belirleyelim
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink', 'orange']

# Bazı dilimleri vurgulamak istersek explode listesi oluşturalım
explode = (0, 0, 0, 0, 0, 0, 0)    # vurgulanmak istenen index yerine 0.1 yazilir

# Pie chart oluşturalım
plt.pie(brand_quantity,
        labels=brand_quantity.index,
        colors=colors,
        explode=explode,
        autopct='%1.1f%%',
        startangle=140)

# İç kısmı delik yapmak için beyaz bir daire ekleyelim
hole = plt.Circle((0, 0), 0.5, facecolor='white')
plt.gcf().gca().add_artist(hole)


# Baslik bilgileri
plt.axis('equal')  # Dairesel çizim sağlar
plt.title("Brand Based Quantities", fontsize=20)
plt.show()







##########################################################################
# 3) grouped countplot : SUBCATEGORY x DISCOUNT RANGE  x QUANTITY
##########################################################################

# Sutun satir boyutlari
plt.figure(figsize=(12, 12))

# Grafik bilgileri
sns.countplot(data=df,
              x="discount_range",
              palette="Spectral",
              hue="subcategory")

# Baslik bilgileri
plt.title("Discount Range by Subcategory", fontsize=25)
plt.xlabel('Discount range', fontsize=22)
plt.ylabel('Product quantity', fontsize=22)

plt.show()






##########################################################################
# 4) Histogram : PRICE
##########################################################################
# Tek bir değişkene ait veri dağılımını gösterir.

plt.figure(figsize=(10, 10))
plt.style.use("ggplot")

sns.distplot(df['unit_price'],
             color='seagreen',
             kde=True)

plt.title("Distribution of Prices", fontsize=20)
plt.xlabel("Unit Price", fontsize=15)
plt.ylabel("Density", fontsize=15)

plt.show()




##########################################################################
# 5) boxplot : PRICE
##########################################################################
###  Boxplot   : Tek bir değişkene ait veri dağılımını ve aykırı değerleri gösterir.

plt.figure(figsize=(16,8))

sns.set(font_scale=1.2)
sns.set_style("white")

sns.boxplot(data=df,
            x="brand",
            y="price",
            palette="Spectral")

plt.title("Distribution of Prices", fontsize=20)
plt.xlabel("Brand", fontsize=17)
plt.ylabel("Price", fontsize=17)

plt.show()






##########################################################################
# 6) line plot
##########################################################################
# Plot ciziminden once, month veya year gibi sutunlari olustur!

sns.set(font_scale=1)
sns.set_style("whitegrid")

sns.lineplot(data=df,
             x="month",
             y="price",
             color="blue")

sns.lineplot(data=df,
             x="month",
             y="unit_price",
             color="green")

plt.title("Price vs Unit price", fontsize=17)
plt.xlabel ("Month", fontsize=15)
plt.ylabel ("Unit price", fontsize=15)

plt.show()