# Tugas 6: Javascript dan AJAX

* [Register Page](https://bagas-tugas-django.herokuapp.com/todolist/register/)</br>
* [Login Page](https://bagas-tugas-django.herokuapp.com/todolist/login/)</br>
* [TODOLIST Page](https://bagas-tugas-django.herokuapp.com/todolist/)</br>
* [JSON Todolist Page](https://bagas-tugas-django.herokuapp.com/todolist/json/)</br>

## Asynchronous vs Synchronous Programming

* Asynchronous Programming
  - Multi thread, artinya yang artinya operasi atau program dapat berjalan secara paralel
  - Non-blocking, dapat mengirimkan lebih dari multiple request ke server
  - Lebih cepat

* Synchronous Programming
  - Single thread,  hanya satu operasi yang berjalan tiap waktu
  - Blocking, hanya dapat mengirimkan satu request dan harus menunggu response
  - Lebih lambat dan lebih rumit

## Penerapan paradigma _Event-Driven Programming_

Event-Driven programming dapat didefinisikan sebagai suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya.

Artinya Event-Driven Programming adalah paradigma pemrograman yang terjadi apabila ada penyebab atau kejadian. 
Contoh yang dapat kita temukan dalam tugas ini adalah proses POST data yang kita lakukan, apabila kita sudah mengisi semua data pada form di modal dan menekan tombol `Tambah`, maka kita bisa melihat bahwa akan ada data baru yang muncul.

## Penerapan asynchronous programming pada AJAX

Pemanggilan ajax bisa dilakukan pada tag <scripts> </scripts>. Pada proses kali ini saya akan menjelaskan proses POST pada AJAX.
Pada proses POST, pada ajax saya memanggil kode ini:

```shell
  $("#createTaskForm").on("submit", function(e){
    e.preventDefault();
    var date = new Date();
    var current_date = date.getFullYear() + "-" + (date.getMonth()+1) + "-" +date.getDate();
    var title = $("#title").val();
    var description= $("#description").val();
   
    $.ajax({
      method: "POST",
      url: "/todolist/add/",  
      data: {"title":title, "description":description},
    }).done(function(resp) {
      console.log(resp)
      $("#todolistCard").append(`
        <div class="card text-center zoom">
          <div class="card-header card-bg-rv"> Date Created: ${current_date} </div>
          <div class="image-box card-bg-rv">
            <img src="https://i.ibb.co/b1tTPqm/todolist.webp" height="200"></img>
            <div class="card responsive-card">
            <div class="card-body card-bg-rv">
              <h5 class="card-title"> ${resp.title} </h5>
              <p class="card-text"> ${resp.description} </p>
            </div>
          </div>
          </div>
        </div>`
      )
      $("#createTaskModal").modal("hide")
    })
  })
```

Akan di proses terlebih dahulu apakah button sudah ditekan atau belum, apabila sudah ditekan maka akan dipanggil perintah AJAX yang menerima tipe POST dan URL yang telah disediakan. Lalu, data pada form diubah ke dalam bentuk JSON.
Lalu jika sukses akan dipanggil method alternatif selain `success` yaitu `.done()`, lalu menambahkan data yang diterima pada tag dengan id `todolistCard`. Setelah itu data akan keluar.

## Implementasi Checklist

1.  Buat path /todolist/json pada urls.py dengan function yg sesuai untuk mengembalikan seluruh data task dalam bentuk json dan pada template `todolist.html` ditambahkan script jQuery yang dibungkus `$(document).ready(function{})` agar script langsung jalan saat halaman di-load. Script yang digunakan adalah `$getJSON()` untuk menerima json dari `todolist/json/` dan `$each()` yang melakukan iterasi untuk tiap object task pada database. Pada tiap iterasi, data dengan tampilan card akan di-append ke HTML pada tag `<div>` dengan id = `todolistCard`.

  * show_json pada `views.py`

```Javascript
@login_required(login_url='/todolist/login/')
def show_json(request):
    todolist = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", todolist), content_type="application/json")
```

  * AJAX GET

```Javascript
$(document).ready(function(){
  $.getJSON("{% url 'todolist:show_json' %}", function(data) {
    $.each(data, function(index, value) {
      console.log(value)
      $("#todolistCard").append(`
        <div class="card text-center zoom">
          <div class="card-header card-bg-rv"> Date Created: ${value.fields.date} </div>
          <div class="image-box card-bg-rv">
            <img src="https://i.ibb.co/b1tTPqm/todolist.webp" height="200"></img>
            <div class="card responsive-card">
            <div class="card-body card-bg-rv">
              <h5 class="card-title"> ${value.fields.title} </h5>
              <p class="card-text"> ${value.fields.description} </p>
            </div>
          </div>
          </div>
        </div>`
      )
    })
  })
```

2.  Membuat sebuah modal yang memiliki form menggunakan Bootstrap dari [https://getbootstrap.com/docs/5.2/components/modal/](https://getbootstrap.com/docs/5.2/components/modal/)

3.  Membuat function `ajax_create_task()` yang akan membuat object Task dari form `createTaskForm` jika method dari request adalah POST. Setelah itu, function ini akan mengembalikan response dalam bentuk JSON sebagai status keberhasilan data yang ditambahkan. Lalu akan dibuat path /todolist/add yang mengarah ke view yang baru telah dibuat. Selanjutnya, hubungkan form yang telah dibuat ke dalam modal ke path /todolist/add
    
4. Ketika form `createTaskForm` disubmit, Jquery akan memanggil request ajax dengan method POST ke url todolist/add yang sebelumnya ditambahkan. Agar data baru tampil secara asinkronus atau tanpa reload seluruh page, maka data baru dengan tampilan card akan di-append ke HTML pada tag `<div>` dengan id = `todolistCard`.

```Javascript
$("#createTaskForm").on("submit", function(e){
    e.preventDefault();
    var date = new Date();
    var current_date = date.getFullYear() + "-" + (date.getMonth()+1) + "-" +date.getDate();
    var title = $("#title").val();
    var description= $("#description").val();
   
    $.ajax({
      method: "POST",
      url: "/todolist/add/",  
      data: {"title":title, "description":description},
    }).done(function(resp) {
      console.log(resp)
      $("#todolistCard").append(`
        <div class="card text-center zoom">
          <div class="card-header card-bg-rv"> Date Created: ${current_date} </div>
          <div class="image-box card-bg-rv">
            <img src="https://i.ibb.co/b1tTPqm/todolist.webp" height="200"></img>
            <div class="card responsive-card">
            <div class="card-body card-bg-rv">
              <h5 class="card-title"> ${resp.title} </h5>
              <p class="card-text"> ${resp.description} </p>
            </div>
          </div>
          </div>
        </div>`
      )
      $("#createTaskModal").modal("hide")
    })
  })
```
