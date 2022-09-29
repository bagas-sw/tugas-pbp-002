# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

[TODOLIST Page](https://bagas-tugas-django.herokuapp.com/todolist/)
[Register Page](https://bagas-tugas-django.herokuapp.com/todolist/register/)
[Login Page](https://bagas-tugas-django.herokuapp.com/todolist/login/)
[Create New Task Page](https://bagas-tugas-django.herokuapp.com/todolist/create-task/)

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









## Akun Dummy
```shell
 1. username : apel123
    password : pbp2022.
 2. username : jeruk123
    password : pbp2022.
```
