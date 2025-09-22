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

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery berguna bagi aplikasi untuk dapat mengakses, mentransfer dan melihat 
data-data dari database

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Tentu sulit untuk menentukan mana yang lebih baik diantara XML atau JSON tanpa alat ukur yang adil.
Menurut saya, JSON lebih baik untuk pemula karena lebih mudah dan enak dibaca saja.
Berdasarkan artikel https://medium.com/@gopi_ck/7082f8c2edec,
JSON lebih popular selain karena mudah dibaca juga, JSON lebih ringan dan cepat. Selain itu juga, JSON
terdapat built-in support pada beberapa bahasa pemrograman, terlebih lagi terdapat sinergi dengan javascript

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() berfungsi untuk mengecek validitas dari data-data yang telah diisi di form.
is_valid() dibutuhkan untuk mencegah kesalahan pengisian data oleh user.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token berguna untuk mengecek apakah suatu laman diakses melalui url yang dipercaya yang telah 
ditentukan di setting.py . Jika diakses dari tempat tidak terpercaya akan mengembalikkan error
403 forbidden.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama kita bikin sebuah form untuk dapat menambah data-data produk ke database, kita bikin forms.py
bikin sebuah class untuk menambah pbjek Product yang dimana kita dapat masukkan atribut-atributnya, kecuali
id-nya. Lalu kita bikin alur requestnya di views.py dan kita routing urlnya

Kedua, membuat halaman untuk menampilkan semua produk dan juga detailnya serta page untuk menambah produk.
kita bikin alur requestnya di views.py setelah itu kita routing urlnya, karena ini page baru. Kita
buat juga template baru untuk menyesuaikan, kita buat template menyesuaikan dengan data-data dari model dan
juga menggunakan base template yang di sebelumnya kita buat. Untuk page add product, untuk menjaga keamanan
kita memakai csrf_token dan mengatur sumber mana saja yang dipercaya di settings.py 

Ketiga, untuk dapat melihat data kita dapat menyajikan dalam bentuk xml/json
untuk keduanya kita bikin function baru di views.py dan juga mengimpor httpresponse dan serializers
untuk memudahkan memformatnya. Selain itu kita membuat fungsi untuk mengembalikan data dengan id tertentu
Jika id tidak exist, kembalikkan error 404. Setelah itu kita routing url seperti biasa

6. Feedback Asdos
Asdos membantu saya untuk mencari kesalahan pada proyek django saya dan stanby di discord. Overall 5/5.

7. Postman
https://drive.google.com/drive/folders/1sS8bCrdpCjzb5oNVLXOKkPMfb_vOYkFe?usp=sharing

/// END TUGAS 3 ///

/// TUDAS 4 ///
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.


2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?


3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).



/// END TUGAS 4 ///