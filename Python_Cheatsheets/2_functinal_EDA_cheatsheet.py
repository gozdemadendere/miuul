
##########################################################################
# ADVANCED FUNCTIONAL EDA
##########################################################################

## Önümüze bir veri seti geldiğinde izlemeniz gereken adımlar

# 1) Data Exploration (Genel Resim):
# Veri setinin başından ve sonundan birkaç satırı gözden geçirin, kaç sütun ve satır olduğunu kontrol etmek

# 2) Kategorik değişken analizi:
# Kategorik değişkenlerin benzersiz değerlerini ve sıklıklarını incelemek
# Bu, her bir kategorinin veri setinde ne kadar yaygın olduğunu anlamamıza yardımcı olur.

# 3) Sayısal değişken analizi:
# Sayısal değişkenlerin temel istatistiklerini (ortalama, standart sapma, minimum, maksimum, medyan, çeyreklikler) kontrol etmek
# Bu, sayısal değişkenlerin dağılımını anlamamıza ve potansiyel aykırı değerleri belirlemenmize yardımcı olur.

# 4) Hedef değişken analizi:
# Eğer bir hedef değişkeniniz varsa (örneğin, bir tahmin yapmak istediğiniz bir değişken), bu değişkenin dağılımını ve istatistiklerini incelemek
# Hedef değişkenin diğer özelliklerle ilişkisini anlamak için grafikler ve tablolar kullanabiliriz.

# 5) Korelasyon analizi:
# Sayısal değişkenler arasındaki ilişkiyi anlamak için korelasyon matrisini oluşturmak
# Korelasyon, değişkenler arasındaki doğrusal ilişkiyi ölçer ve değişkenlerin birbiriyle nasıl ilişkilendiğini anlamamıza yardımcı olabilir.

# Son olarak: Veri analizi sonuçlarını raporlamak






# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import dataframe
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")




#############################################
### 1) Data Exploration (Genel Resim):
#############################################

### check_df: Data Exploration Function : Displays basic characteristics of a DataFrame.
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


# use the function
check_df(df, head=5)



#############################################
### 2) Kategorik değişken analizi:
#############################################

### grab_col_names: Identifies categorical, numeric, and categorical ordinal variables in the dataset.

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Returns the names of categorical, numeric, and categorical ordinal variables in the dataset.

    Parameters:
    ----------
    dataframe: pandas.core.DataFrame
        DataFrame for which variable names are to be retrieved.
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
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and str(dataframe[col].dtypes) in ["int32", "float32", "int64", "float64"]]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and str(dataframe[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int64", "float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


grab_col_names(df, cat_th=10, car_th=20)




### cat_summary: Summarizes and optionally visualizes value counts and ratios for categorical variables.

def cat_summary(dataframe, col_name, plot=False):
    """
    Summarizes value counts and ratio analysis of a categorical variable in the given DataFrame.
    If plot is True, it also visualizes the distribution.

    Parameters:
    ----------
    dataframe: pandas.core.DataFrame
    col_name: str
    plot: bool

    Returns:
    -------
    None
    """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("###################################################")

    if plot:
        if dataframe[col_name].dtypes == "bool":
            sns.countplot(x=dataframe[col_name].astype(int), data=dataframe)
            plt.show(block=True)
        else:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)


cat_summary(df, "sex", plot=False)


















#############################################
### 3) Sayısal değişken analizi:
#############################################



# num_summary: Provides descriptive statistics and optional visualization for numerical variables.

def num_summary(dataframe, numerical_col, plot=False):
    """
    Displays descriptive statistics and optionally visualizes the distribution of a numerical variable.

    Parameters:
    ----------
    dataframe: pandas.core.DataFrame
    numerical_col: str
    plot: bool

    Returns:
    -------
    None
    """
    quantiles = [0.05, 0.10, 0.30, 0.40, 0.50, 0.60, 0.70, 0.90, 0.95]
    print(f"##################### {numerical_col} & Describe #############################")
    print(dataframe[numerical_col].describe(quantiles).T)
    print("##################################################################################")

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

num_summary(df, "fare", plot=False)










#############################################
### 4) Hedef değişken analizi:
#############################################

# target_summary_with_cat: Computes the mean of the target variable based on a categorical column.

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
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))


target_summary_with_cat(df, "survived", "sex")




# target_summary_with_num: Computes the mean of the target variable based on a numerical column.

def target_summary_with_num(dataframe, target, numerical_col):
    """
    Computes the mean of the target variable based on a numerical column in the given DataFrame.

    Parameters:
    ----------
    - dataframe: pandas.core.DataFrame
        DataFrame for analysis.
    - target: str
        Name of the target variable.
    - numerical_col: str
        Name of the numerical column.

    Returns:
    -------
    None

    Example Usage:
    target_summary_with_num(df, 'Target_Column', 'Numeric_Column')
    """
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


target_summary_with_num(df, "survived", "fare")










#############################################
### 5) Korelasyon analizi:
#############################################

# hig_correlated_cols: Identifies columns with high correlation and optionally visualizes the correlation matrix.

def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    """
    Identifies columns with high correlation in the given DataFrame.
    If plot is True, it visualizes the correlation matrix.

    Parameters:
    ----------
    - dataframe: pandas.core.DataFrame
        DataFrame for analysis.
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

high_correlated_cols(df)