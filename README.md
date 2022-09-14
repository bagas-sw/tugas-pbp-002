# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Link aplikasi Heroku : [https://bagas-tugas-002.herokuapp.com/katalog/](https://bagas-tugas-002.herokuapp.com/katalog/)

## Struktur MTV pada Django

![Bagan _request_ client ke web aplikasi berbasis Django](https://1.bp.blogspot.com/-u-n0WYPhc3o/X9nFtvNZB-I/AAAAAAAADrE/kD5gMaz4kNQIZyaUcaJJFVpDxdKrfoOwgCLcBGAsYHQ/s602/3.%2BPython%2BDjango%2B-%2BModul%2B2_Page2_Image5.jpg)

Django adalah salah satu web framework yang berbasis MTV. MTV merupakan kependekan dari Model, Template, dan View. Nantinya, Model akan terhubung ke database, Template akan terhubung ke _web browser_ dan View yang akan menghubungkan Model dan Template.

* Model pada 'models.py' merupakan bagian yang berfungsi untuk melakukan interaksi dengan basis data. Interaksi model dan database berlangsung dua arah, selain mengambil data, model juga akan melakukan _updating_ dan _inserting_ data.
* Template adalah bagian representatif dari web. Bagian ini merupakan representasi tentang bagaimana _web_ akan ditampilkan. Template akan berisi HTML, CSS, dan JavaScript. Django mengakses file template melalui 'views.py' dengan menggunakan JINJA templating.
* View akan berjalan sesuai dengan file python lainnya yaitu 'urls.py'. URL routing berguna untuk menunjukan view yang akan digunakan berdasarkan routing. View juga akan berhubungan dengan Models, yang mana Models juga terhubung dengan database. File model ini memberi kemudahan dalam pengaksesan database, karena kita tidak perlu menggunakan syntax-syntax SQL dan manajemen database.

## Penggunaan _virtual environment_ dalam project Django

_Virtual environment_ adalah sebuah tools untuk membuat suatu _environment_ pada python lokal yang berbeda dengan _environment_ python pada sistem . Program python yang berjalan dalam 'virtualenv' akan memiliki modul-modulnya sendiri dan tidak bisa diakses oleh program luar. Sedangkan, jika program python berjalan tanpa 'virtualenv' hanya bisa menggunakan modul-modul global saja, yaitu modul yang terinstall di sistem, dan semua aplikasi bisa mengakses dan menggunakannya.

Dalam penggunaanya, disarankan untuk memakai _virtual environment_ ini setiap kali mempunyai project baru. Hal ini bertujuan untuk memastikan versi sebuah _library_ yang dipakai di suatu project tidak akan berubah apabila kita melakukan update pada _library_ yang sama di project lainnya.

Aplikasi web tetap dapat dibuat walau tanpa menggunakan _virtual environment_. Akan tetapi, penggunaan _virtual environment_ sangat direkomendasikan, karena mempunyai banyak keuntungan, diantaranya versi _library_ tetap konsisten walaupun bekerja di perangkat yang berbeda dan jika kita bekerja di banyak project versi _library_ nya dapat menyesuaikan kebutuhan masing-masing project.
