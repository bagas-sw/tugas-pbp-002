# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

* [TODOLIST Page](https://bagas-tugas-django.herokuapp.com/todolist/)</br>
* [Register Page](https://bagas-tugas-django.herokuapp.com/todolist/register/)</br>
* [Login Page](https://bagas-tugas-django.herokuapp.com/todolist/login/)</br>
* [Create New Task Page](https://bagas-tugas-django.herokuapp.com/todolist/create-task/)</br>

## Kegunaan `{% csrf_token %}` pada elemen `<form>` dan apa yang terjadi apabila tidak ada potongan kode tersebut?
Kegunaan dari `_csrf_token_` adalah untuk melindungi semua data dari form yang menggunakan method POST dari pembobolan. Apabila tidak menggunakan `csrf_token_` pada `<form>`, eksploitasi dapat dengan mudah dilakukan dengan memanfaatkan _authenticated state_ yang dimiliki korban. Maka dari itu, Django mengimplementasikan csrf_token untuk menghindari CSRF Attack dari penyerang. Dan apabila penyerangan berhasil pada akun admin, hal tersebut dapat membahayakan seluruh aplikasi.

## Apakah kita dapat membuat elemen secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
Hal tersebut dapat dilakukan
- Caranya dengan membuat langsung form di HTML, dengan menggunakan tag `<form>``</form>`
- Lalu menambahkan atribut method http-request seperti `method="POST"` pada tag `<form>`
- Selanjutnya, menambahkan tag `<input>` diantara tag `<form>` dan `</form>`. Tag tersebut digunakan untuk menerima input dari user.
- Dalam tag `<input>` tambahkan atribut `name = <namaVariabel>`, supaya data input dapat diambil oleh `views.py`. Misalnya dengan menggunakan method `request.POST.get("username")` untuk mendapatkan input username.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimapanan pada database, hingga munculnya pada *template* HTML
- Setelah user menekan tombol submit, function yang ada pada `views.py` akan mendapatkan input dari user dengan perintah `request.POST.get("namaVariabel")` dan akan disimpan dalam suatu variabel.
- Dalam tugas kali ini, ada beberapa variabel inputan user seperti title dan description. Dari kedua input tersebut, akan dibuat object `Task` baru, yang nantinya akan disimpan dengan perintah `save()`
- Lalu, pada fungsi `show_todolist` kita dapat mengakses data yang tersimpan pada database Django sesuai dengan user-nya, dengan menggunakan perintah `Task.objects.filter(user=request.user)`.
- Selanjutnya, data tersebut akan disimpan dalam context dan akan di render ke HTML
- Pada template HTML, akan dilakukan iterasi pada data tersebut dan ditampilkan dalam bentuk tabel.

## Jelaskan bagaimana cara mengimplementasikan checklist di atas
1. Buat aplikasi django dengan perintah `python manage.py startapp todolist` pada terminal
2. Menambahkan path todolist di file `settings.py` dan file `urls.py` pada project_django
```shell
INSTALLED_APPS = [
    ...
    'katalog',
    'mywatchlist',
    'todolist',
]
```
```shell
    urlpatterns = [
        ...
        path('katalog/', include('katalog.urls')),
        path('mywatchlist/', include('mywatchlist.urls')),
        path('todolist/', include('todolist.urls')),
    ]
```

3. Membuat class Task pada models.py dengan beberapa field seperti user, date, title, dan description
```shell
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now = True)
    title = models.CharField(max_length=200)
    description = models.TextField()
```

4. Jalankan command untuk mempersiapkan migrasi model ke database Django lokal :
  ```shell
  python manage.py makemigrations
  ```
5. Jalankan command untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal :
  ```shell
  python manage.py migrate
  ```
6. Membuat fungsi `show_todolist` pada `views.py` untuk menampilkan todolist sesuai dengan kepemilikan user.

7. Membuat fungsi pada `views.py` untuk login, logout, dan register. Yang semuanya dapat diintegrasikan dengan HTML file pada template. Pada fungsi register buat form registrasi dengan `UserCreationForm()`.

8. Membuat fungsi `create-task` untuk membuat object Task baru dengan mengambil parameter-parameter `title` dan `description` dari inputan user di `create-task.html` dan `user=request.user`, lalu object tersebut di save ke database dengan method `save()`.

9. Berikan restriksi pada fungsi `create-task` dan `show-todolist` dengan menambahkan `@login_required(login_url='/todolist/login/')` di atas fungsi tersebut.

10. Membuat register.html, login.html yang kurang lebih sama dengan tugas lab sebelumnya. Lalu, membuat todolist.html untuk menampilkan detail dari tiap object Task pada tabel dengan cara melakukan iterasi untuk tiap Task-nya.

11. Pada `create-task.html`, buat form untuk pembuatan task secara manual dengan menggunakan method POST

12. Membuat routing pada `todolist/urls.py` sesuai dengan function yang ada di views.py.

13. Melakukan deployment ke Heroku. Lalu, buatlah 2 akun dummy beserta 3 dummy data pada website hasil deployment tersebut


## Akun Dummy
```shell
 1. username : apel123
    password : pbp2022.
```
```shell
 2. username : jeruk123
    password : pbp2022.
```

# Tugas 5 : Web Design Using HTML, CSS, and CSS Framework

## Apakah perbedaan Inline, Internal, dan External CSS

1. Inline CSS: Metode styling ini memanfaatkan atribut style dari tag HTML di dalam template. Contoh: `<h3 style="color:white;">Ini adalah contoh inline CSS</h3>`
    Kelebihan: Metode ini efektif digunakan jika hanya sebatas menambahkan styling pada 1 selector.
    Kekurangan: membuat HTML file terlihat berantakan apabila menambahkan banyak styling dan juga metode ini kurang cocok jika ingin membuat style yang ingin digunakan kembali.
2. Internal CSS:  Metode styling ini menggunakan tag <style> dan styling ditulis di dalam tag tersebut.
    Kelebihan: penambahan CSS tidak perlu dilakukan dengan file terpisah, langsung melakukan styling di file HTML yang sama.
    Kekurangan: meningkatkan loading time pada website karena styling yang ditambahkan langsung pada file HTML dan juga jika style yang ingin dibuat banyak akan memenuhi file template HTML.
3. External CSS: penerapan metode ini menggunakan tag `<link>` untuk menghubungkan HTML dengan CSS yang terpisah.
    Kekurangan : Website akan membutuhkan waktu yang lebih lama untuk loading karena styling pada website tersebut diletakkan di dalam file CSS tersendiri.
    Kelebihan: File HTML akan jadi lebih rapi, dan juga 1 file CSS tersebut dapat dipakai oleh HTML lain, selama di panggil dengan tag `<link>`.

## Penjelasan tag HTML5

* <header>          : membuat header pada website
* <nav>             : membuat navigasi pada website
* <h1> sampai <h6>  : membuat heading
* <p>               : teks yang diapit tag ini akan tampil dengan ukuran normal 
* <br>	            : memasukan satu baris kosong
* <a>               : teks yang diapit dengan tag ini akan jadi reference, dengan link ditentukan dengan atribut `href`
* <input>           : tag ini digunakan untuk menerima masukan pengguna, dengan atribut `type` sebagai jenis masukannya.
* <button>          : membuat sebuah tombol
* <form>            : membuat sebuah form HTML untuk menerima input pengguna
* <table>           : tag ini akan membuat table
* <div>             : tag ini berguna untuk membungkus dan memisahkan elemen dengan elemen lainnya

Dan masih banyak lagi

## Tipe-tipe CSS Selector

1. Universal Selector : Memilih semua elemen html. Syntax: *

2. Type Selector : Memilih semua elemen dengan tipe yang sesuai. Contoh: type selector `p` akan memilih semua elemen <p>

3. Class Selector : Memilih semua elemen yang punya attribut class yang sesuai. Contoh: `.btn` akan memilih semua elemen yang punya class `btn`

4. ID Selector : Memilih sebuah elemen berdasarkan nilai attribut idnya. Misalnya: `#header` akan memilih elemen yang punya id "header".

5. Attribut selector : Memilih semua elemen yang punya attribut yang sesuai. Contoh: [href] akan memilih semua elemen yang punya attribut href.

## Implementasi Checklist
1. Menambahkan bootstrap pada base.html di directory `templates`
