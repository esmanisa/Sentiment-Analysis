from django.http import HttpResponse
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import torch
from transformers import AutoTokenizer
import numpy as np
import snscrape.modules.twitter as sntwitter
import string
import gensim.parsing.preprocessing as gsp
import re
from typing import List
from jpype import JClass, java
from nltk.tokenize import word_tokenize 
import nltk
from datetime import datetime
# nltk.download('punkt')

regex_for_remove_tags = r'<.*?>'
regex_mentions_or_emails = r'([A-Za-z]+[_ ]+[A-Za-z]*[0-9]*@\w+.[com]*)'
regex_links = r'http\S+|www.\S+'
regex_for_numbers = r'([0-9]+)'
whitelist = set('abcçdefgğhıijklmnoöpqrsştuüvwxyz ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ')
pytorch_model = ""

def index(request):
    if request.method == "POST":
        keras_model = load_model('model_sentiment.h5', compile=False)
        url = request.POST["urlInput"]
        temp = url.split("/")[-1]
        tweet_id = temp[:temp.index("?")]
        tweets = sntwitter.TwitterTweetScraper(tweet_id).get_items()

        for tweet in tweets:
            content = tweet.rawContent

        # preprocess = preprocess_text(content)
        
        max_length = 1781  # Eğitimde belirlediğiniz maksimum metin uzunluğunu kullanın
        tokenizer = Tokenizer(num_words=max_length, split=' ')  # Eğitimde kullandığınız tokenizer'ı yükleyin veya oluşturun
        text_sequence = tokenizer.texts_to_sequences([content])
        text_sequence = pad_sequences(text_sequence, maxlen=max_length)
        predictions = keras_model.predict(text_sequence)
        print(predictions)
        label_mapping = {'Positive': 2, 'Negative': 0, 'Notr': 1}
        # [0.82, 0.10, 0.42]
        # En yüksek olasılığa sahip sınıfın indeksini bulun
        predicted_class_index = np.argmax(predictions)
        print(predicted_class_index)
        # Etiketlerin sırasını kullanarak tahminin hangi sınıfa ait olduğunu belirleyin
        label_mapping_inverse = {v: k for k, v in label_mapping.items()}
        predicted_class = label_mapping_inverse[predicted_class_index]
        print(predicted_class)
        return render(request, 'index.html', {'content': content, 'predicted_class': predicted_class})
    else:
        return render(request, 'index.html')

def remove_punctuation(text):
    
    text_no_punctuation = [ch for ch in str(text) if ch not in string.punctuation]
    text_no_punctuation = "".join(text_no_punctuation)

    return text_no_punctuation

def remove_emojis(text):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"  
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, ' ', str(text))

def remove_stopwords(text): 
    stop_words = ['çok', 'at', 'in', 'im', 'acaba','acep','allah','adamakıllı','adeta','ait','altmýþ','altmış','altý'
                  , 'altı','ama','amma','anca','ancak','arada','artýk','aslında','aynen','ayrıca','az','açıkça','açıkçası',
                  'bana','bari','bazen','bazý','bazı','başkası','baţka','belki','ben','benden','beni','benim',
                  'beri','beriki','beþ','beş','beţ','bilcümle','bile','bin','binaen','binaenaleyh','bir','biraz',
                  'birazdan','birbiri','birden','birdenbire','biri','birice','birileri','birisi','birkaç',
                  'birkaçı','birkez','birlikte','birçok','birçoğu','birþey','birþeyi','birşey','birşeyi','birţey',
                  'bitevi','biteviye','bittabi','biz','bizatihi','bizce','bizcileyin','bizden','bize','bizi','bizim',
                  'bizimki','bizzat','boşuna','bu','buna','bunda','bundan','bunlar','bunları','bunların','bunu','bunun',
                  'buracıkta','burada','buradan','burası','böyle','böylece','böylecene','böylelikle','böylemesine',
                  'böylesine','büsbütün','bütün','cuk','cümlesi','da','daha','dahi','dahil','dahilen','daima','dair',
                  'dayanarak','de','defa','dek','demin','demincek','deminden','denli','derakap','derhal','derken',
                  'deđil','değil','değin','diye','diđer','diğer','diğeri','doksan','dokuz','dolayı','dolayısıyla',
                  'doğru','dört','edecek','eden','ederek','edilecek','ediliyor','edilmesi','ediyor','elbet',
                  'elbette','elli','emme','en','enikonu','epey','epeyce','epeyi','esasen','esnasında','etmesi',
                  'etraflı','etraflıca','etti','ettiği','ettiğini','evleviyetle','evvel','evvela','evvelce',
                  'evvelden','evvelemirde','evveli','eđer','eğer','fakat','filanca','gah','gayet','gayetle','gayri',
                  'gayrı','gelgelelim','gene','gerek','gerçi','geçende','geçenlerde','gibi','gibilerden','gibisinden',
                  'gine','göre','gırla','hakeza','halbuki','halen','halihazırda','haliyle','handiyse','hangi','hangisi',
                  'hani','hariç','hasebiyle','hasılı','hatta','hele','hem','henüz','hep','hepsi','her',
                  'herhangi','herkes','herkesin','hiç','hiçbir','hiçbiri','hoş','hulasaten','iken','iki',
                  'ila','ile','ilen','ilgili','ilk','illa','illaki','imdi','indinde','inen','insermi','ise',
                  'ister','itibaren','itibariyle','itibarıyla','iyi','iyice','iyicene','için','iş','işte',
                  'iţte','kadar','kaffesi','kah','kala','kanýmca','karşın','katrilyon','kaynak','kaçı','kelli',
                  'kendi','kendilerine','kendini','kendisi','kendisine','kendisini','kere','kez','keza','kezalik',
                  'keşke','keţke','ki','kim','kimden','kime','kimi','kimisi','kimse','kimsecik','kimsecikler',
                  'külliyen','kýrk','kýsaca','kırk','kısaca','lakin','leh','lütfen','maada','madem','mademki',
                  'mamafih','mebni','međer','meğer','meğerki','meğerse','milyar','milyon','mu','mü','mý','mı',
                  'nasýl','nasıl','nasılsa','nazaran','naşi','ne','neden','nedeniyle','nedenle','nedense',
                  'nerde','nerden','nerdeyse','nere','nerede','nereden','neredeyse','neresi','nereye',
                  'netekim','neye','neyi','neyse','nice','nihayet','nihayetinde','nitekim','niye','niçin',
                  'o','olan','olarak','oldu','olduklarını','oldukça','olduğu','olduğunu','olmadı',
                  'olmadığı','olmak','olması','olmayan','olmaz','olsa','olsun','olup','olur','olursa','oluyor',
                  'on','ona','onca','onculayın','onda','ondan','onlar','onlardan','onlari','onlarýn','onları',
                  'onların','onu','onun','oracık','oracıkta','orada','oradan','oranca','oranla','oraya','otuz',
                  'oysa','oysaki','pek','pekala','peki','pekçe','peyderpey','rağmen','sadece','sahi','sahiden',
                  'sana','sanki','sekiz','seksen','sen','senden','seni','senin','siz','sizden','sizi','sizin',
                  'sonra','sonradan','sonraları','sonunda','tabii','tam','tamam','tamamen','tamamıyla','tarafından',
                  'tek','trilyon','tüm','var','vardı','vasıtasıyla','ve','velev','velhasıl','velhasılıkelam','veya',
                  'veyahut','ya','yahut','yakinen','yakında','yakından','yakınlarda','yalnız','yalnızca','yani',
                  'yapacak','yapmak','yaptı','yaptıkları','yaptığı','yaptığını','yapılan','yapılması','yapıyor',
                  'yedi','yeniden','yenilerde','yerine','yetmiþ','yetmiş','yetmiţ','yine','yirmi','yok','yoksa',
                  'yoluyla','yüz','yüzünden','zarfında','zaten','zati','zira','çabuk','çabukça','çeşitli',
                  'çok','çokları','çoklarınca','çokluk','çoklukla','çokça','çoğu','çoğun','çoğunca','çoğunlukla',
                  'çünkü','öbür','öbürkü','öbürü','önce','önceden','önceleri','öncelikle','öteki','ötekisi','öyle',
                  'öylece','öylelikle','öylemesine','öz','üzere','üç','þey','þeyden','þeyi','þeyler','þu','þuna',
                  'þunda','þundan','þunu','şayet','şey','şeyden','şeyi','şeyler','şu','şuna','şuncacık','şunda',
                  'şundan','şunlar','şunları','şunu','şunun','şura','şuracık','şuracıkta','şurası','şöyle',
                  'ţayet','ţimdi','ţu','ţöyle', 'hala', 'yer', 'güzel', 'büyük']
    stop_words = ['a','acaba','altı','altmış','ama','ancak','arada','artık','asla','aslında','aslında','ayrıca',
                  'az','bana','bazen','bazı','bazıları','belki','ben','benden','beni','benim','beri','beş',
                  'bile','bilhassa','bin','bir','biraz','birçoğu','birçok','biri','birisi','birkaç','birşey',
                  'biz','bizden','bize','bizi','bizim','böyle','böylece','bu','buna','bunda','bundan','bunlar',
                  'bunları','bunların','bunu','bunun','burada','bütün','çoğu','çoğunu','çok','çünkü','da',
                  'daha','dahi','dan','de','defa','değil','diğer','diğeri','diğerleri','diye','doksan','dokuz',
                  'dolayı','dolayısıyla','dört','e','edecek','eden','ederek','edilecek','ediliyor','edilmesi',
                  'ediyor','eğer','elbette','elli','en','etmesi','etti','ettiği','ettiğini','fakat','falan',
                  'filan','gene','gereği','gerek','gibi','göre','hala','halde','halen','hangi','hangisi',
                  'hani','hatta','hem','henüz','hep','hepsi','her','herhangi','herkes','herkese','herkesi',
                  'herkesin','hiç','hiçbir','hiçbiri','i','ı','için','içinde','iki','ile','ilgili','ise',
                  'işte','itibaren','itibariyle','kaç','kadar','karşın','kendi','kendilerine','kendine',
                  'kendini','kendisi','kendisine','kendisini','kez','ki','kim','kime','kimi','kimin',
                  'kimisi','kimse','kırk','madem','mi','mı','milyar','milyon','mu','mü','nasıl','ne',
                  'neden','nedenle','nerde','nerede','nereye','neyse','niçin','nin','nın','niye','nun',
                  'nün','o','öbür','olan','olarak','oldu','olduğu','olduğunu','olduklarını','olmadı',
                  'olmadığı','olmak','olması','olmayan','olmaz','olsa','olsun','olup','olur','olur','olursa',
                  'oluyor','on','ön','ona','önce','ondan','onlar','onlara','onlardan','onları','onların',
                  'onu','onun','orada','öte','ötürü','otuz','öyle','oysa','pek','rağmen','sana','sanki',
                  'sanki','şayet','şekilde','sekiz','seksen','sen','senden','seni','senin','şey','şeyden',
                  'şeye','şeyi','şeyler','şimdi','siz','siz','sizden','sizden','size','sizi','sizi',
                  'sizin','sizin','sonra','şöyle','şu','şuna','şunları','şunu','ta','tabii','tam',
                  'tamam','tamamen','tarafından','trilyon','tüm','tümü','u','ü','üç','un','ün','üzere',
                  'var','vardı','ve','veya','ya','yani','yapacak','yapılan','yapılması','yapıyor','yapmak',
                  'yaptı','yaptığı','yaptığını','yaptıkları','ye','yedi','yerine','yetmiş','yi','yı','yine',
                  'yirmi','yoksa','yu','yüz','zaten','zira','zxtest']
    
    stop_words = ['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'bir', 'birkaç', 'birşey', 'biz',
                  'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'den', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem',
                  'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü',
                  'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey',
                  'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani', 'dan']
    word_tokens = nltk.word_tokenize(text) 
    filtered_text = [word for word in word_tokens if word not in stop_words] 
    return ' '.join(filtered_text)

def correct_old_characters(text):
    text = re.sub(r"Â", "A", text)
    text = re.sub(r"Î", "I", text)
    text = re.sub(r"î", "ı", text)
    text = re.sub(r"â", "a", text)
    text = re.sub(r"û", "u", text)
    text = re.sub(r"Û", "U", text)
    return text

def remove_two_ch_words(text):
  text = ' '.join([w for w in text.split() if len(w)>2])
  return text

def correct_letters(text):
   text = ''.join(filter(whitelist.__contains__, text))
   return text

def remove_tags(text):
  text = re.sub(pattern=regex_for_remove_tags, repl=' ', string=text)
  return text

def remove_links(text):
   text = re.sub(pattern=regex_links, repl=' ', string=text)
   return text

def remove_numbers(text):
   text = re.sub(pattern=regex_for_numbers, repl=' ', string=text)
   return text

def remove_email_or_email(text):
   text = re.sub(pattern=regex_mentions_or_emails, repl=' ', string=text)
   return text

def lower(text):
    text = re.sub(r"İ", "i", text)
    text = re.sub(r"I", "ı", text)
    text = re.sub(r"Ç", "ç", text)
    text = re.sub(r"Ş", "ş", text)
    text = re.sub(r"Ü", "ü", text)
    text = re.sub(r"Ğ", "ğ", text)
    text = text.lower() # for the rest use default lower
    return text

def tokenizasyon(text):
    return word_tokenize(text)

def lemmatizer(text):
    lemma_words = []
    TurkishMorphology = JClass('zemberek.morphology.TurkishMorphology')
    morphology = TurkishMorphology.createWithDefaults()
    for text in tokenizasyon(text):
      lemma_word = str(morphology.analyzeAndDisambiguate(str(text)).bestAnalysis()[0].getLemmas()[0])
      lemma_words.append(lemma_word)
    text = ' '.join(lemma_words)
    return text

def preprocess_text(text):
    r_mentions = remove_email_or_email(text)
    r_links = remove_links(r_mentions)
    r_punctuation = remove_punctuation(r_links)
    r_emojis = remove_emojis(r_punctuation)
    r_numbers = remove_numbers(r_emojis)
    remove_non_tr = correct_letters(r_numbers)
    remove_2_ch = remove_two_ch_words(remove_non_tr)
    r_tags = remove_tags(remove_2_ch)
    strip_spaces = gsp.strip_multiple_whitespaces(r_tags)
    lower_ch = lower(strip_spaces)
    return lower_ch

def predict_sentiment_pytorch(request):
    tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased",do_lower_case=True, add_prefix_space=True, use_fast=False)
    content = ""
    inputs = tokenizer(content, return_tensors='pt', padding=True, truncation=True)

    # Modeli kullanarak tahmin yapın
    outputs = pytorch_model(**inputs)
    probability = torch.softmax(outputs.logits, dim=-1)

    # En yüksek olasılığa sahip sınıfın indeksini alın
    predicted_class_index = torch.argmax(probability[0]).item()

    # İndeksi etiket adına dönüştürün
    senti_map = {2: 'Positive', 0: 'Negative', 1: "Notr"}
    predicted_label = senti_map[predicted_class_index]

    return HttpResponse(predicted_label)

## redirect(url) -> o sayfaya yönlendirir
## render('index.html')