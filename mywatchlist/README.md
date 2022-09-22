# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Link HTML : [https://bagas-tugas-django.herokuapp.com/mywatchlist/html/](https://bagas-tugas-django.herokuapp.com/mywatchlist/html/)
Link JSON : [https://bagas-tugas-django.herokuapp.com/mywatchlist/json/](https://bagas-tugas-django.herokuapp.com/mywatchlist/json/)
Link XML : [https://bagas-tugas-django.herokuapp.com/mywatchlist/xml/](https://bagas-tugas-django.herokuapp.com/mywatchlist/xml/)

## Perbedaan HTML, XML, dan JSON
* HTML atau _Hypertext Markup Language_ merupakan bahasa yang digunakan dalam menyajikan dokumen untuk ditampilkan oleh browser. Dalam penggunaanya, developer dapat mengkombinasikannya dengan CSS untuk melakukan _styling_, serta JavaScript untuk keperluan _scripting_. Selain it, manipulasi terhadap halaman web dapat dilakukan dengan HTML _Document Object Model_ (DOM) yang sifatnya hierarkis. HTML tidak dapat dipergunakan untuk pertukaran data, tidak seperti JSON dan XML, HTML tidak punya sintaks khusus untuk menyimpan data. Akan tetapi, HTML dapat digunakan untuk menyajikan data dalam bentuk teks, gambar, bahkan video pada halaman website.
* JSON atau _Javascript Object Notation_ merupakan format atau notasi yang dipergunakan untuk merepresentasikan objek-objek. Awalnya, JSON digunakan untuk merepresentasikan objek dalam JavaScript, sesuai dengan namanya. Sehingga syntax pada JSON sama dengan syntax pembuatan object pada JavaScript. Jika HTML dan XML didasari dengan konsep DOM, maka JSON didasari dengan konsep pasangan _key-value_, contohnya '{"title" : "Interstellar"}'
* XML atau _eXtensible Markup Language_ merupakan bahasa yang merepresentasikan data dengan penggunaan tag-tag, seperti '<field>'. Secara sekilas penggunaan tag-tag tersebut membuatnya mirip dengan HTML, bahkan pada XML terdapat struktur hierarkis dan konsep DOM yang dipergunakan untuk memanipulasi data. XML dapat digunakan dengan berbagai cara untuk pertukaran data.
* Perbedaan JSON dan XML :
  - JSON lebih cepat dalam membaca dan menulis
  - XML lebih aman dibandingkan JSON
  - JSON lebih mudah untuk diolah daripada XML
  - XML dapat diberi komentar, sementara JSON tidak
  - JSON bisa menggunakan array, sedangkan XML tidak

## Mengapa data _delivery_ diperlukan dalam implementasi suatu platform ?
Data _delivery_ diperlukan dalam suatu platform karena suatu aplikasi pastinya akan menyimpan dan mengambil data tertentu dari suatu server. Tanpa adanya transmisi data, aplikasi akan cenderung bersifat "statik" karena data yang ada didalamnya tidak berubah sesuai dengan kondisi yang ada. Dalam hal ini, transmisi data dapat dilakukan oleh XML dan JSON, yang dimana keduanya dapat mempermudah _formatting_ dan pengolahan data yang akan dikirimkan ke sisi user atau _frontend_.

## Implementasi poin 1 sampai 3
1.  Membuat aplikasi baru dengan menjalankan command berikut:
  
  ```shell
  django-admin startapp mywatchlist
  ```
2.  Menambahkan path mywatchlist ke dalam file 'settings.py' dan 'urls.py' yang ada di direktori 'project-django'
  
  ```shell
  INSTALLED_APPS = [
    ...
    'mywatchlist',
]
  ```
  
  ```shell
  urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
  ```
3.  Buka dan edit file models.py yang ada di direktori mywatchlist dan tambahkan class MyWatchList.
  
  ```shell
class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()
  ```

4. Buat folder fixtures dan di dalamnya buat file 'initial_data_mywatchlist_data.json'. Lalu isikan 10 data watchlist yang tiap datanya berisi detail film yang akan atau sudah ditonton.

5. Jalankan command untuk mempersiapkan migrasi model ke database Django lokal :
  ```shell
  python manage.py makemigrations
  ```
6. Jalankan command untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal :
  ```shell
  python manage.py migrate
  ```
7. Jalankan perintah 'python manage.py loaddata initial_mywatchlist_data.json' untuk memasukkan data tersebut ke dalam database Django lokal.

8. Buka file 'views.py' dan tambahkan fungsi-fungsi untuk menampilkan data pada database, baik dalam bentuk HTML, XML, dan JSON.
  ```shell
def show_mywatchlist(request):
    return HttpResponse("Tugas 3 PBP")

def show_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_json_by_id(request, id):
    data_mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

def show_xml_by_id(request, id):
    data_mywatchlist = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    
    watched = 0
    
    for film in data_mywatchlist:
        if film.watched == True:
            watched += 1
    
    if watched >= 5:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"
        
    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Bagas',
        'npm' : '2106708904',
        'message' : message
    }
    return render(request, "mywatchlist.html", context)
  ```
  
  9. Menambahkan data ke file 'watchlist.html' pada folder 'templates'.
  
  10. Membuat routing pada file 'urls.py' agar data dalam bentuk JSON, HTML, dan XML dapat diakses melalui URL
    ```shell
  ...
  urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('html/', show_html, name='show_html')
]
  ```
11. Membuat unit tests pada 'tests.py', lalu untuk menjalankannya lakukan command 'python manage.py test'
  
  ```shell
from django.test import TestCase, Client
from django.urls import resolve

class MyWatchListTest(TestCase):
    def test_html_url(self):
        response =  Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)

    def test_json_url(self):
        response =  Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
    
    def test_xml_url(self):
        response =  Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
  ```

12. Melakukan _deployment_ ke Heroku
  Lakukan 'add' ,'commit', dan 'push' ke repo tugas. Dan, karena pada tugas sebelumnya sudah dimasukkan '(HEROKU_APP_NAME)' serta API key '(HEROKU_API_KEY)' pada bagian secret repository di repo yang sama.
  Maka deploy akan dilakukan secara otomatis ke aplikasi di Heroku setelah melakukan push ke repo tugas.

## Screenshot akses URL via Postman.
  ### HTML
  ![HTML](https://drive.google.com/file/d/15sqHIfdTpAhBYzkwEGVcKPRPN4FJd55M/view?usp=sharing)
  ### JSON
  ![JSON](https://drive.google.com/file/d/1ga_kbZhDRBYfe50UYAtKBwJhkpQ7eHCu/view?usp=sharing)
  ### XML
  ![XML](https://drive.google.com/file/d/12GKitCq7t-61huV2jS0l8Lqs9X-iBWdQ/view?usp=sharing)
  
