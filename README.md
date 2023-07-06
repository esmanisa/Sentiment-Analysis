# Sentiment-Analysis

# Sentiment Analysis with Twitter Data

## Proje Konusunun Önemi ve Özgün Değeri

## Duygu Analizi Nedir?
Duygusal analiz veya fikir madenciliği, doğal dil işleme alanında, insanların metindeki öznelliğin hesaplı muamelesi yoluyla düşüncelerini, duygularını, değerlendirmelerini, tutumlarını ve duygularını analiz eden aktif bir çalışma alanıdır. 
Duygu analizi, basit bir şekilde, bir metin parçasının pozitif, negatif veya nötr olup olmadığı üzerine (istatistiksel olarak) çalışma sürecidir. Duyarlılık analiz yaklaşımlarının çoğu iki formdan birini alır: kutupluluk temelli veya değerlik temelli. Kutupluluk temelli yaklaşımda metin parçalarının olumlu veya olumsuz olarak sınıflandırılır, değerlilik temelli yaklaşıma ise yoğunluk göz önüne alınarak sınıflandırılır. Örneğin, “iyi” ve “mükemmel” kelimeleri polartitesine dayalı bir yaklaşımda aynı şekilde ele alınacak; “mükemmel” ise değerlik temelli bir yaklaşımda “iyi” den daha olumlu olarak değerlendirilecektir.

Twitter gibi sosyal medya mecralarından gelen mikro blog içeriği, yalnızca içerdiği veri miktarı nedeniyle değil, aynı zamanda duyguları ifade etmek için kullanılan dil türünden, yani kısa formlardan, emojilerden ve ifadelerden dolayı da incelemede ciddi zorluklar içermektedir.
Duygu analizi genellikle  işletmelerin müşteri geri bildirimlerinde marka ve ürün duyarlılığını izlemelerine ve müşteri ihtiyaçlarını anlamalarına yardımcı olmak için metinsel veriler üzerinde gerçekleştirilir. 

## Özgün Değer
Projede Twitter üzerinden politika, spor, kripto borsaları veya şirket hisseleri gibi konularda Türkçe paylaşılan metinler üzerinden yüksek doğruluklu duygu analizi yapılabilecek olunması, yapılan sınıflandırmalar sonucunda farklı konular hakkında tahminleme üzerinde çalışılacak olması (örneğin borsa veya hisse tahmini vb.) ve gelecek farklı model çalışmaları için Twitter üzerinden alınan verilerden Türkçe hazır veri seti oluşturulup yayınlanacak olması projenin özgün değerlerindendir.

## Projenin Amacı ve Hedefi
Proje özellikle ürün ve hizmetler için kullanıcı yorumları içeren veriler üzerinde analiz yapılarak bu ürün ve hizmetlerin daha iyi hale getirilmesi ve yeni çalışmalarda gelecek tahminlerin yapılabilmesi hedeflenmektedir. Böylelikle hem kullanıcılar hem de ürün ve hizmet üreticiler için fayda sağlanmış olacaktır. Ek olarak geliştirilecek web uygulamasıyla Twitter verileri üzerinden analiz yapmak isteyen geliştiriciler için Türkçe dilinde istenilen konu başlığında hazır veri setleri oluşturma imkanı sağlanacaktır. Böylelikle geliştiricilerin yapacakları analiz için veriseti oluşturma süresi azaltılıp verimlilik sağlanacaktır.

## Projenin iş-zaman çizelgesi

| İP. No. | İş Paketlerinin Adı ve Hedefleri | Zaman Aralığı (Haftalık) | Başarı Ölçütü  |
|---------|----------------------------------|--------------------------|----------------|
| 1 | **Literatür ve Makale Taraması:** Yapılacak proje ile ilgili daha önce yapılmış çalışmaların ayrıntılı olarak incelenmesi amaçlanmaktadır. | 1., 2., 3., 4., 5. ve 6. haftalar | Projenin daha önce yapılan projelere göre yenilikçi olması açısından, bu iş paketinin araştırmanın başarısına katkısı %10 oranındadır. | 
| 2 | **Veri seti Oluşturulması:** Yapılacak çalışma için Twitter üzerinden Türkçe paylaşılmış veriler alınarak veri seti oluşturulması amaçlanmaktadır. | 7., 8., 9. ve 10. haftalar | Proje ile ilgili işlemlerin yapılabilmesi sağlıklı verilere bağlı olduğundan bu iş paketinin araştırma başarısına katkı oranı %25 oranındadır. | 
| 3 | **Veri Ön işlemesi, Vektörlere Dönüştürülmesi ve Etiketlenmesi:** Oluşturulan veri setinin yapay zeka model başarımını olumsuz etkileyebilecek karakterlerden ayrıştırılıp düzenli bir veri  seti oluşturulması amacıyla bazı yöntemlerle ön işlenmesi, sayısal girdilere dönüştürülmesi ve olumlu, olumsuz ve nötr olarak etiketlenerek duygu analizi için model kurulmasına hazır hale getirilmesi amaçlanmaktadır. | 11., 12., 13., 14. ve 15. 16. haftalar | Proje ile ilgili işlemlerin yapılabilmesi sağlıklı verilere bağlı olduğundan bu iş paketinin araştırma başarısına katkı oranı %25 oranındadır. | 
| 4 | **Model:** Ön işlenen veri seti kullanılarak duygu analizi yapılabilecek model oluşturulması hedeflenmektedir. | 17., 18., 19., 20. ve 21. haftalar | Proje konusunun uygulamaya geçilebilmesi ve doğal dil işleme algoritmalarıyla çözülmesine bağlı olduğundan dolayı bu iş paketinin araştırmaya katkısı %25 oranındadır. | 
| 5 | **Uygulama:** Oluşturulan modelin kullanıcılara sunulması amacıyla Python Django frameworkü kullanılarak web sitesi oluşturulması hedeflenmektedir. | 22., 23., 24., 25. ve 26. haftalar | Oluşturulan modelin kullanıcılara kolay kullanım sunulması açısından, bu iş paketinin araştırmanın başarısına katkısı %10 oranındadır. | 
| 6 | **Doğrulama ve Test:** Uygulamayla birlikte oluşturulan modelden beklenen çıktıların alınması için son kontrollerin gerçekleştirilmesi hedeflenmektedir. | 27., ve 28. haftalar | Sonuçların başarılı ve doğru bir şekilde kullanıcılara sunulması için bu iş paketinin araştırmanın başarısına katkısı %5 oranındadır. | 

## Projede kullanılacak yöntem, donanımlar ve yazılımlar ile ilgili bilgiler

## Yöntem
İlk olarak deneysel çalışmalara ön ayak olması adına proje için daha önce yapılmış çalışmalar incelenecektir. 
Proje çerçevesinde tüm uygulama Python programlama dili kullanılarak gerçekleştirilecektir.
Çalışma için gerekli olan veri seti Twitter platformunun sağladığı Application Programming Interface (API) yardımıyla oluşturulacaktır. Bu API’a erişim için Python programlama dili için geliştirilmiş Tweepy kütüphanesi ile erişim sağlanıp veri seti oluşturulacaktır.
Oluşturulan veri  seti üzerinde cümlelerin aynı formata gelmesi ve daha verimli sonuçlar alınabilmesi amacıyla önişleme adımları gerçekleştirilecektir. Bu önişleme adımlarından bazıları Türkçe dilini işlemek için java programlama diliyle geliştirilmiş Zemberek kütüphanesi ile yapılacaktır. Örneğin duygu analizi yapılabilmesi için kelimelerin köklerine inilmesi, kelimelerin token ve lemmalarına ayrılması gibi. Proje Python programlama dili ile gerçekleştirileceğinden projede Zemberek kütüphanesinin Python için geliştirilmiş olan github deposu kullanılacaktır. Zemberek kütüphanesi aracılığıyla gerçekleştirilecek önişleme adımlarının yanında özel durumlar için regular expressionların geliştirilmesi, durak kelimelerin kaldırılması, emojilerin, alfanümerik olmayan karakterlerin ve argo ifadelerin kaldırılması, İngilizce klavye ile yazılmış Türkçe kelimelerin karşılıklarının bulunması adımları gerçekleştirilecektir. Ayrıca önişleme adımları literatür taraması ile desteklenecek, araştırmalar sonucu en iyi sonucu verecek önişleme adımları da uygulanabilecektir.
Temizlenen veriler daha sonra makine öğrenmesi algoritmalarında işlenebilmesi için vektörlere dönüştürülecektir. Verilerin vektörlere dönüştürülmesinde mevcut olan yöntemler (Word2Vec, BERT, BoW) denenerek en verimli sonucun alındığı yöntem seçilecektir.

Duygu analizi için oluşturulacak modeller, en doğru sonucun alınabilmesi için literatürde en iyi sonucu veren makine öğrenmesi ve/veya derin öğrenme metotlarıyla gerçekleştirilecektir. 
Projede gerçekleştirilecek her adımdan daha hızlı sonuç alınabilmesi adına model geliştirme adımları Google tarafından bulut tabanlı ve ücretsiz olarak hizmete sunulan Colaboratory ortamı tercih edilecektir.

Proje kapsamında kullanıcı arayüzü Django frameworkü kullanılarak web sitesi şeklinde geliştirilecektir. Geliştirilecek web sitesinde kullanıcılar duygu analizi yapmak istediği tweetin url’sini arayüze girdi olarak vererek paylaşılan tweet içeriğinin olumlu, olumsuz veya nötr bir ifade olup olmadığını görebilecektir. Ek olarak kullanıcılar Türkçe tweet içeriklerinde istedikleri anahtar kelimeler veya konu başlığı etiketleri ile hazır veriseti oluşturabilecektir.

## Donanımlar
En az iki çekirdeğe (core) sahip işlemci, en az 8 GB ana bellek (RAM), en az 128 GB ikinci bellek (SSD ya da HDD), 4 GB ana belleğe sahip ekran kartı donanımlarını içeren bir bilgisayar gerekmektedir. 

## Yazılımlar
Projede kullanılacak programlama dili Python’dur. Twitter tarafından sunulan API’den veri alma kolaylığı, akademik çalışmalar için genişletilmiş veri sunması gibi avantajlardan dolayı Twitter API tercih edilmiştir [8]. API ve Tweepy kütüphanesi yardımıyla Twitter üzerinden istenilen konudaki verileri alarak duygu analizi için Türkçe hazır veri seti oluşturulabilecektir.

Verilerin ön işlenmesi ve model oluşturulması yine Python programlama dili kullanılarak gerçekleştirilecektir. Bu işlemler Java programlama dili ile geliştirilmiş Türkçe metinleri işlemek için olan Zemberek kütüphanesi kullanılarak gerçekleştirilecektir. Duygu analizi için geliştirilecek modeller makine öğrenmesi algoritmaları için scikit-learn, derin öğrenme yöntemleri için keras ve tensorflow kütüphanelerinden yararlanılacaktır.
Oluşturulan modelin kullanıcılar tarafından kullanılabilmesi ve uygulanabilir bir hale dönüşmesi için geliştirilecek web uygulamasında django frameworkü kullanılacaktır. Bu frameworkün seçilme sebepleri arasında hızlı, ölçeklenebilir ve güvenli geliştirme sunmasıdır.
