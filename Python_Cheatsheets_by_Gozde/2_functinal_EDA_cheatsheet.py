##########################################################################
# ADVANCED FUNCTIONAL EDA
##########################################################################

## Önümüze bir veri seti geldiğinde izlememiz gereken adımlar:

# 1) Data Exploration (Genel Resim):
# Veri setinin başından ve sonundan birkaç satırı gözden geçiririz, kaç sütun ve kaç satır olduğuna bakarız, veri tiplerini kontrol ederiz

# 2) Kategorik Değişken Analizi:
# Kategorik değişkenlerin benzersiz değerlerini ve sıklıklarını inceleriz ve istersek görselleştiririz
# Bu, her bir kategorinin veri setinde ne kadar yaygın olduğunu anlamamıza yardımcı olur

# 3) Sayısal Değişken Analizi:
# Sayısal değişkenlerin temel istatistiklerini (ortalama, standart sapma, minimum, maksimum, medyan, çeyreklikler) kontrol ederiz
# Bu, sayısal değişkenlerin dağılımını anlamamıza ve potansiyel aykırı değerleri belirlememize yardımcı olur

# 4) Hedef Değişken Analizi:
# Eğer bir hedef değişkenimiz varsa (örneğin, bir tahmin yapmak istediğiniz bir değişken), bu değişkenin dağılımını ve istatistiklerini inceleriz
# Hedef değişkenin diğer değişkenlerle ilişkisini inceleriz ve istersek görselleştiririz

# 5) Korelasyon Analizi:
# Yüksek korelasyona sahip sütunları tanımlarız ve isteğe bağlı olarak korelasyon matrisini görselleştiririz
# Korelasyon, değişkenler arasındaki doğrusal ilişkiyi ölçer ve değişkenlerin birbiriyle nasıl ilişkilendiğini anlamamıza yardımcı olabilir.

# Son olarak: Veri analizi sonuçlarını raporlarız.






# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import dataframe
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")




##########################################################################
### 1) Data Exploration (Genel Resim):
##########################################################################

### Function : check_df: Data Exploration > Displays basic characteristics of a DataFrame.


# Create the function
def check_df(dataframe, head=5):
    """
    Function to check basic characteristics of a DataFrame.

    Parameters:
    ----------
    dataframe: pandas.core.DataFrame
        DataFrame to be checked.
    head: int
        Number of rows to display from the beginning and end of the DataFrame.

    Returns:
    -------
    None

    Example Usage:
    --------------
    check_df(df, head=10)
    """
    print("###################### First 5 Rows ######################")
    print(dataframe.head(head))
    print("###################### Last 5 Rows ######################")
    print(dataframe.tail(head))
    print("###################### Shape: Rows x Columns ######################")
    print(dataframe.shape)
    print("###################### General Info ######################")
    print(dataframe.info())
    print("###################### Null Values ######################")
    print(dataframe.isnull().sum().sort_values(ascending=False))
    print("###################### Statistical Info ######################")
    print(dataframe.describe().T)


# Use the function
check_df(df, head=5)           # head=10 gibi degisiklik yapabiliriz.






### Function : grab_col_names: Identifies categorical, numeric, and categorical ordinal variables in the dataset.

# Create the function
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Returns the names of categorical, numeric, and categorical ordinal variables in the dataset.

    Parameters:
    ----------
    dataframe: dataframe
        dataframe for which variable names are to be retrieved.
    cat_th: int, float
        Threshold value for numeric but categorical variables.
    car_th: int, float
        Threshold value for categorical but cardinal variables.

    Returns:
    cat_cols: list
        List of categorical variables
    num_cols: list
        List of numeric variables
    cat_but_car: list
        List of categorical-looking cardinal variables

    Notes:
    -------
    cat_cols + num_cols + cat_but_car = total variable count
    num_but_cat is within cat_cols.
    """
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in dataframe.columns if
                   dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print("############   Categorical, Numeric, and Categorical Ordinal Variables in the Dataset   #############")
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    print("#####################################################################################################")

    return cat_cols, num_cols, cat_but_car


# Use the function
grab_col_names(df, cat_th=10, car_th=20)








##########################################################################
### 2) Kategorik Değişken Analizi  (Analysis of Categorical Variables)
##########################################################################


### Dataframedeki tum kategorik degiskenleri bulalim:
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]  # Sonucta tum kategorik degiskenler



### Function : cat_summary : Summarizes and optionally visualizes value counts and ratios for categorical variables.

# Create the function
def cat_summary(dataframe, col_name, plot=False):
    """
    Summarizes value counts and ratio analysis of a categorical variable in the given DataFrame.
    If plot is True, it also visualizes the distribution.

    Parameters:
    ----------
    dataframe: dataframe
    col_name: str
    plot: bool

    Returns:
    -------
    None    
    """
    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print("############################################")
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("############################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe, hue=dataframe[col_name], palette="viridis")
            plt.show(block=True)
    else:
        print("############################################")
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("############################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe, hue=dataframe[col_name], palette="viridis")
            plt.show(block=True)


# Use the function
cat_summary(df, "adult_male", plot=True)       # plot=False dersek plot gelmeyecektir.


# Use the function for "all categorical columns"
for col in cat_cols:
    cat_summary(df, col, plot=True)








##########################################################################
### 3) Sayısal Değişken Analizi   (Analysis of Numerical Variables)
##########################################################################


### Dataframedeki tum sayisal degiskenleri bulalim:
num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
num_cols = [col for col in num_cols if col not in cat_cols]   # Sonucta tum sayisal degiskenler


### Function : num_summary : Provides descriptive statistics and optional visualization for numerical variables.

# Create the function
def num_summary(dataframe, numerical_col, plot=False):
    """
    Displays descriptive statistics and optionally visualizes the distribution of a numerical variable.

    Parameters:
    ----------
    dataframe: dataframe
    numerical_col: str
    plot: bool

    Returns:
    -------
    None
    """
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(f"############## {numerical_col} > Describe ##############")
    print(dataframe[numerical_col].describe(quantiles).T)
    print("############################################")

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col, fontsize=13)
        plt.ylabel("Density", fontsize=13)
        plt.title(numerical_col, fontsize=18)
        plt.show(block=True)


# Use the function
num_summary(df, "age", plot=True)

# Use the function for "all numerical columns"
for col in num_cols:
    num_summary(df, col, plot=True)








##########################################################################
### 4) Hedef Değişken Analizi (Analysis of Target Variable)
##########################################################################



### Hedef Değişkenin Kategorik Değişkenler ile Analizi

### Function : target_summary_with_cat: Computes the mean of the target variable based on a categorical column.

# Create the function
def target_summary_with_cat(dataframe, target, categorical_col):
    """
    Computes the mean of the target variable based on a categorical column in the given DataFrame.

    Parameters:
    ----------
    - dataframe: pandas.core.DataFrame
        DataFrame for analysis.
    - target: str
        Name of the target variable.
    - categorical_col: str
        Name of the categorical column.

    Returns:
    -------
    None

    Example Usage:
    ----------
    target_summary_with_cat(df, 'Target_Column', 'Categorical_Column')
    """
    print("############################################")
    print(pd.DataFrame({"Target_Variable_Mean": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")
    print("############################################")


# Use the function
target_summary_with_cat(df, "survived", "pclass")


# Use the function for "all categorical columns"
for col in cat_cols:
    target_summary_with_cat(df, "survived", col)





### Hedef Değişkenin Sayısal Değişkenler ile Analizi

### Function : target_summary_with_cat: Computes the mean of the target variable based on a categorical column.

# Create the function
def target_summary_with_num(dataframe, target, numerical_col):
    print("############################################")
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")
    print("############################################")


# Use the function
target_summary_with_num(df, "survived","age")


# Use the function for "all numeric columns"
for col in num_cols:
    target_summary_with_num(df, "survived", col)








##########################################################################
### 5) Korelasyon Analizi (Analysis of Correlation)
##########################################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()




# Sayısal sütunları seç
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

# Korelasyon matrisini hesapla
corr = df[num_cols].corr()

### Create a heatmap
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

# Yüksek Korelasyonlu Değişkenlerin Silinmesi
cor_matrix = df.corr().abs()






### Function : high_correlated_cols: Identifies columns with high correlation and optionally visualizes the correlation matrix.

# Create the function
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    """
    Identifies columns with high correlation in the given DataFrame.
    If plot is True, it visualizes the correlation matrix.

    Parameters:
    ----------
    - dataframe: dataframe
        dataframe for analysis.
    - plot: bool
        Used to visualize the correlation matrix.
    - corr_th: float
        Threshold for high correlation.

    Returns:
    -------
    drop_list: list
        List of columns with high correlation.

    Example Usage:
    --------------
    high_correlated_cols(df, plot=True, corr_th=0.85)
    """
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


# Use the function
high_correlated_cols(df)

drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)

