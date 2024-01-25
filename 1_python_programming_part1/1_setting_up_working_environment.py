
########################################################
# Virtual Environment & Package Management
########################################################

### Sanal Ortam (Virtual Environment): İzole çalışma ortamları oluşturmak için kullanılır.
# Projeler birbirini etkilemeyecek şekilde çalışır.
# Projelere ait Python sürümleri veya kütüphane sürümleri farklı olabilir, böylece çakışmaları önler.
# Sanal ortam araçları: venv, virtualenv (paket yönetim aracı olarak pip'i kullanırlar), pipenv, conda



### Paket Yönetimi (Package Management):
# Conda > Pip
# Conda: Hem sanal ortam yönetim aracı, hem paket yönetim aracıdır. (Hem sanal ortam oluşturur, hem paket indirme/ yükleme / yönetme yapar.)
# Pip: Sadece paket yönetim aracıdır. (Yani kutuphane yukler, indirir, degistirir, bagimsizliklarini saglar.)


# ** PyCharm: Hem Python çalışma ortamı sağlar, hem de işletim sistemiyle (terminal aracılığıyla) çalışmak için alanlar sağlar.



### Conda ile
# Sanal ortamların listelenmesi için terminale yaz: conda env list (* icinde bulunulan aktif ortamı gösterir)
# Sanal ortam oluşturmak için terminale yaz: conda create -n my_env
# Sanal ortamı aktifleştirme: conda activate my_env
# Sanal ortamı inaktifleştirme: conda deactivate
# Yüklü paketlerin listelenmesi: conda list
# Paket yükleme: conda install numpy veya conda install numpy pandas scipy (y yaz ve onayla)
# Paket silme: conda remove package_name
# Belirli bir versiyona göre paket yükleme (paketi once sil, sonra yeni vers yukle): conda install numpy=1.20.1 (pip'te == kullanilir)
# Paket yükseltme: conda upgrade numpy
# Tüm paketleri yükseltme: conda upgrade --all



### Pip ile
# pip: pypi (python package index) paket yönetim aracı
# Paket yükleme: pip install pandas
# Belirli bir versiyona göre paket yükleme: pip install pandas==1.2.1

### Versiyonları birine aktarmak için yaml file oluşturma:
# conda env export > environment.yaml (veya yml) enter & sonra alt satira listelemek icin ls yaz enter
# Bu yaml file ciktisi kullanilarak nasil calisma ortami yaratilir? : conda deactivate enter (onceki calisma ortamini kapatir) sonra:
# Bu calisma ortamini nasil kullaniriz?
# once, onceki environmenti sil: conda env remove -n my_env
# Oluşturulan yaml dosyasını kullanarak çalışma ortamı yaratma: conda env create -f environment.yaml
# conda list



## Yeni Proje Oluşturma:
# Projects - New project - Location: sonuna proje ismi ekle
# "Anaconda'nın sağladığı base environment"i seç:
# Interpreter'ın en sonundaki üç noktaya tıkla
# Conda environment'a tıkla - interpreterın en sonundaki üç noktaya tıkla
# En sonda python3'ü seç - OK - OK - Create
