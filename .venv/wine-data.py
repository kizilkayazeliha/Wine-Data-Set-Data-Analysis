import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from pandas.plotting import scatter_matrix
#verileri görselleştirmek için matplotlib kütüphanesi kullanılır.
from sklearn import datasets
# veri seti sklearn kütüphanesinde olduğu için ilk önce sklearn paketini kurmak gerekiyor.
    wine = datasets.load_wine() #veri setini dataset komutu ile yükler.
#print(wine.DESCR) #veri seti açıklamasını yapar.
#print(type(wine)) #sklearn.utils._bunch.Bunch yani türünü ifade eder.
print(wine.keys()) # veri türü içinde nelerin olduğu.
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names']).
# data = veri(sayısal değer), target = sınıf etiketi, frame =Pandas DataFrame olarak veri, target_name = hedef sınıf ismi, DESCR = açıklama, feature_names = özellik isimleri
#print(wine.data) #bütün veriyi sayısal olarak getirir.
print(wine.target) #bütün verilerin sınıf etiketini getirir ama sınıf ismi ile değil 0 , 1 ,2 şeklinde.
print(wine.target_names) #0,1,2 nin karşılığı, yani sınıfların isimleri.
print(wine.feature_names) #özellikleri getiri. Özellik isimlerini.
print(wine.data.shape) #veri örneklerinin (sample/instance) sayısı, yani veri sayısı da diyebiliriz , özellik sayısı.
# Veri setinde 178 tane sample 13 tane feature var.
print(np.bincount(wine.target)) #her bir tam sayının kaç kez geçtiğini hesaplar.
# Targetlardan kaçar tane olduğu, yani her bir hedeften kaç tane olduğunu gösterir.
# class_0' dan 59 tane, class_1'den 71 tane, class_2'den 48 tane var.

#dataFrame oluşturur.
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['label'] = wine.target
print(df.head())

""" 
#Şarap veri setinin ash özelliğinin dağılım grafiğini oluşturun.
x_index = wine.feature_names.index('ash') #istediğmiz özellik.
labels = wine.target_names #sınıflar (targetlar)
colors = ['blue', 'red' , 'green']
fig, ax = plt.subplots(figsize=(8,5)) #8 inç genişlik 5 inç yükseklik boyuutndan çerçeve yani figüran oluştur.


for label, color in zip (range(len(labels)),colors):
    ax.hist(wine.data[wine.target==label, x_index ],color= color,  label= labels[label])
#ax.hist histogram çizdirir çok fazla parametre alabilir. İlk değeri çizilmesi istenilen veri. Color değeri renk için. Label her histogram için legend’daki yazı class_0 → kırmızı class_1 → yeşil class_2 → mavi
#ax.hist(self, x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, *, data=None, **kwargs)

ax.set_title("Wine Dataset - Ash Dağılımı")
ax.set_xlabel("Ash")
ax.set_ylabel("Frekans (Şarap Sayısı)")
ax.legend() #sınıf isimlerini yazar. (Sağ üst köşe)
fig.show() #çerçeveyi göster.
"""



""" 
#Şarap veri setinin color_intensity özelliğinin dağılım grafiğini oluşturun.

x_index = wine.feature_names.index('color_intensity')
labels = wine.target_names
colors = ['blue', 'red' , 'green']
fig, ax = plt.subplots(figsize=(8,5))


for label, color in zip (range(len(labels)),colors):
    ax.hist(wine.data[wine.target==label, x_index ],color= color, bins=15, label= labels[label])


ax.set_title("Wine Dataset - color_intensity Dağılımı")
ax.set_xlabel("Color intensity")
ax.set_ylabel("Frekans (Şarap Sayısı)")
ax.legend()
fig.show()

"""

"""
#Şarap veri setinin özelliklerinin dağılım matrisini oluşturun.
df['target'] = wine.target  # sınıf etiketleri ekle
# Scatter matrix çiz
scatter_matrix(df, figsize=(15,15), diagonal='hist', c=df['target'], marker='o', alpha=0.8)
#scatter_matrix(df) → DataFrame’deki tüm sayısal sütunlar arasındaki scatter plotları çizer diagonal='hist' → Köşegenlerde histogram gösterir. c=df['target'] → Her sınıf farklı renkte gösterilir. marker='o' → Noktaların şekli. alpha=0.8 → Noktaların şeffaflığı.figsize=(15,15) → Grafik boyutu

plt.show()
"""
df['target'] = wine.target  # sınıf etiketleri ekle
sns.pairplot(df, hue='target', diag_kind='hist', plot_kws={'alpha':0.7}) #hue='target' → Sınıfları renklerle ayırır. diag_kind='hist' → Köşegenler histogram. plot_kws={'alpha':0.7} → Noktaların şeffaflığı
plt.show()

