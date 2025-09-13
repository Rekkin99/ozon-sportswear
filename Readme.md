/// TUGAS 2 ///
1. Implementasi semua fitur yang dibutuhkan dalam tugas 2 dapat dipecah menjadi
beberapa tahapan.

Pertama, inisiasi proyek Django.
Tentukan dimana proyek akan disimpan/dikerjakan di komputer lokal.
Di sini kita akan menggunakan virtual enviroment untuk memastikan
versi dependencies (yang nanti dipakai) dan sebagainya tidak bertabrakan 
dengan versi yang terinstalasi di komputer lokal.
Setelah semua dependencies yang dibutuhkan terinstall, projek django dapat
dengan mudah dibuat melalui command python di powershell/cmd.

Kedua, Routing projek django ke PWS.
Sebelum routing ke PWS, kita harus mengkonfigurasi enviroment variables
baik di direktori lokal dan juga di web pws.
Lalu di dalam direktori proyek kita atur supaya jaringan lokal kita dapat
mengakses aplikasi. Selain itu kita setting juga untuk enviroments berbeda (lokal dan pws)
untuk menggunakan database yang berbeda. Mengapa ini dilakukan? Karena kita menggunakan pws.

Ketiga, Inisiasi Aplikasi.
Kita dapat membuat aplikasi baru pada proyek django dengan command di powershell/cmd.
Aplikasi pada projek django menggunakan konsep MTV (Models-Template-View).
Basically,
Model : Mengatur dan memproses data app
View : Logika perantara antara model dan template
Templates : Biasanya berkas html yang mengatur bagaimana data disajikan kepada user client

di dalam direktori aplikasi kita buat direktori yang mengatur templates aplikasi
disitu kita buat template html sementara untuk tugas 2

Pada direktori aplikasi yang dibuatkan sistem sudah tersedia berkas untuk model dan view jadi
kita tinggal modifikasi saja.
Setelah membuat models dengan atribut yang diminta, kita lakuka migrasi model untuk memberi
tahu projek django bahwa ada perubahan pada model database.
Untuk Sementara template html tugas 2 hanya meminta mengembalikan value diluar model jadi
berkas view hanya kita set untuk mengembalikan value yang diminta di template saja

Keempat Routing antara proyek Django dan Aplikasi Main
Untuk ini terdapat berkas urls.py yang diperlukan di tingkat proyek dan juga aplikasi
bedanya urls tingkat aplikasi mengakses rute url spesifik untuk fitur-fitur aplikasi
tingkat proyek itu mengimpor rute-rute dari berkas urls.py aplikasi-aplikasi
di tingkat aplikasi, kita mengonfigurasi satu urlpattern yang memanggil fungsi dari views
di tingkat projek, kita menambahkan urlpattern untuk menuju berkas urls.py di aplikasi

Terakhir, karena sebelumnya kita sudah menghubungkan ke pws
Jadi tinggal kita update saja ke pws.

2. Bagan Request dari client ke server
Untuk gambar dan penjelesan bisa menuju ke https://drive.google.com/file/d/1cQxpTLNTwhHvQNFDbq9u9YysKCTo6knq/view?usp=sharing
Sumber refrensi dari laman web pbp dan juga slides yang disediakan dan 
juga (berusaha menyimpulkan) kode proyek ini

3. Peran settings.py
Peran berkas settings.py dalam proyek django adalah sebagai konfigurasi variable-variable pada proyek django
kita dapat menentukan apa saja aplikasi yang dapat diakses proyek, jaringan mana yang dapat mengakses proyek,
database apa yang digunakan ketika mengakses proyek dan sebagainya
ref : https://www.geeksforgeeks.org/python/django-settings-file-step-by-step-explanation/

4. Migrasi Database
Migrasi database pada django dilakukan untuk melacak perubahan pada model database pada models.py di aplikasi
Migrasi database akan mengubah struktur database yang digunakan dalam aplikasi
pada django kita melakukan migrasi database setiap terdapat perubahan di models.py
Hanya 2 langkah
pertama, di command line pertama kita memberi command python manage.py makemigrations untuk membuat
berkas berisi perubahan pada model database yang belum diaplikasikan
kedua, di command line kita beri command python manage.py migrate untuk mengaplikasikan
perubahan model database sesuai berkas terbaru

5. Mengapa Django untuk pembelajaran PBP
ini hanya opini saja kemungkinan pertama karena sesuai juga dengan kurikulum
prasayarat pbp itu ddp 1 yang sama-sama menggunakan bahasa python
Dosen saya, pak daya juga sempat menjelaskan bagaimana django itu lumayan cepat dan juga
lebih aman juga, tetapi saya tidak begitu memahami konsep mengapa suatu framework 
bisa lebih aman atau cepat

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Karena waktu tutorial 1 online jadi saya blm bisa terlalu menilai sih, tetapi bagus sih walaupun
online juga tetap stanby 2 jam. So Thanks All!

/// END TUGAS 2 ///

/// TUGAS 3 ///

/// END TUGAS 3 ///