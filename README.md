# Wine-Data-Set-Data-Analysis


### Wine Data Set’in Amacı
Bu veri setinin amacı, kimyasal özelliklerine bakarak bir şarabın hangi sınıfa (hangi üzüm türünden yapılan şarap grubuna) ait olduğunu tahmin etmektir.  

Yani:  
•Girdi (input): Şarabın 13 farklı kimyasal özelliği  
•Çıktı (output): Şarabın ait olduğu sınıf (0, 1 veya 2)  
________________________________________  

#### Detaylı Açıklama  

•	Veri seti, İtalya'nın aynı bölgesinde yetiştirilen üç farklı üzüm türünden üretilmiş şarapların kimyasal analizlerinden oluşur.  
•	Toplam 178 örnek (şarap) vardır.  
•	Her örnekte aşağıdaki gibi 13 sayısal özellik ölçülmüştür:  

| Özellik                 | Açıklama                              |
| ----------------------- | ------------------------------------- |
| 1. Alcohol              | Alkol oranı                           |
| 2. Malic acid           | Malik asit miktarı                    |
| 3. Ash                  | Kül miktarı                           |
| 4. Alcalinity of ash    | Kül alkaliliği                        |
| 5. Magnesium            | Magnezyum miktarı                     |
| 6. Total phenols        | Toplam fenoller                       |
| 7. Flavanoids           | Flavonoidler                          |
| 8. Nonflavanoid phenols | Flavonoid olmayan fenoller            |
| 9. Proanthocyanins      | Proantosiyaninler                     |
| 10. Color intensity     | Renk yoğunluğu                        |
| 11. Hue                 | Renk tonu                             |
| 12. OD280/OD315         | Şarapta seyreltilmiş absorbans ölçümü |
| 13. Proline             | Prolin (bir aminoasit türü) miktarı   |


##### 🎯 Hedef Değişken (Target):  
•	0 → Class_0 (birinci üzüm türü)  
•	1 → Class_1 (ikinci üzüm türü)  
•	2 → Class_2 (üçüncü üzüm türü)  
________________________________________  

##### 🧠 Bu veri seti neden önemli?  
•	Temiz ve dengeli bir veri setidir → yeni başlayanlar için idealdir.  
•	Sınıflandırma algoritmalarını (Logistic Regression, KNN, Decision Tree, SVM vb.) denemek için çok uygundur.  
•	Özelliklerin hepsi sayısaldır → veri ön işleme süreci basittir.  
•	Küçük boyutlu olduğu için hızlı eğitim yapılabilir.  



#### ax.hist() fonksiyonunun alabileceği parametreler:

| Parametre     | Açıklama                                                                        |
| ------------- | ------------------------------------------------------------------------------- |
| `x`           | Histogramını çizmek istediğin veri (liste, NumPy array, Pandas serisi olabilir) |
| `bins`        | Histogramdaki sütun sayısı ya da aralıklar (örn. `10`, `[0, 5, 10, 15]` vs.)    |
| `range`       | Verinin hangi aralıkta histogramı çıkarılacak (`(min, max)` gibi)               |
| `density`     | `True` olursa frekanslar yerine olasılık yoğunluğu gösterilir                   |
| `weights`     | Her veri noktasına bir ağırlık verebilirsin                                     |
| `cumulative`  | `True` olursa kümülatif histogram çizilir                                       |
| `bottom`      | Her barın nereden başlayacağı                                                   |
| `histtype`    | `'bar'`, `'barstacked'`, `'step'`, `'stepfilled'` olabilir                      |
| `align`       | Barların hizalaması (`'left'`, `'mid'`, `'right'`)                              |
| `orientation` | `'vertical'` veya `'horizontal'`                                                |
| `rwidth`      | Barlar arasındaki boşluk oranı                                                  |
| `log`         | `True` olursa logaritmik eksen kullanır                                         |
| `color`       | Barların rengi                                                                  |
| `label`       | Grafiğe eklenecek açıklama etiketi                                              |
| `stacked`     | `True` olursa histogramlar üst üste yığılır                                     |



#### Grafikler ve problem çıktıları:

##### Wine veri setinin ash özelliğinin dağılım grafiğini oluşturun.
<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/639335eb-fe34-45f4-a95d-24fe7dc4b86f" />

##### Wine veri setinin color_intensity özelliğinin dağılım grafiğini oluşturun.
<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/627cdb75-7392-499a-aba7-c7d2013d7f82" />

##### Wine veri setinin özelliklerinin dağılım matrisini oluşturun.
<img width="900" height="900" alt="image" src="https://github.com/user-attachments/assets/57428786-57c4-4afa-84f5-14b02338b66c" />

##### Seaborn kullanarak dağılım matrisini oluşturun. (daha şık ve renkli)
<img width="900" height="900" alt="image" src="https://github.com/user-attachments/assets/59f08f63-1a7c-4843-9bbc-288d919c359c" />




