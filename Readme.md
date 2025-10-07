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
Django AuthenticationForm secara sederhana sebuah class yang menyediakan form untuk user login.
Jadi kita tidak perlu membuat class form yang baru di forms.py

Kelebihan :
Praktis dan Mudah diimplementasi
Keamanan Terjamin
Mudah dikustomisasi

Kekurangan:
Cukup kompleks untuk dipahami
Tidak dapat diimplementasi di luar project Django

Ref : https://medium.com/@alex-azimbaev/a-guide-to-popular-authentication-systems-for-websites-django-firebase-auth-and-more-9e25ba78b3dd

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi itu untuk memverifikasi siapa (user mana) yang menggunakan aplikasi
Otorisasi itu memverifikasi hak akses apa saja yang dimiliki suatu user
Implementasinya dalam Django itu digabung menjadi satu kesatuan authentication system. 
https://docs.djangoproject.com/en/4.2/topics/auth

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session Storage
Kelebihan :
Temporary Storage (Akan dihapus saat session berakhir)
Lebih aman untuk short-term data dibandingkan local storage
Kekurangan :
Tidak dapat bertahan dalam berbagai session browser
Rentan terhadap serangan XSS

Cookies
Kelebihan :
Mudah diimplementasi
Dapat bertahan dalam berbagai session browser
Kekurangan :
Mudah dieksploitasi jika tidak ditangani dengan baik
Storage Terbatas

Ref : https://dev.to/keshav___dev/frontend-session-management-from-cookies-to-jwts-3pb4
https://medium.com/@jananga1999/the-role-of-cookies-in-web-development-24775748b63e

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Selama kita konfigurasi dengan baik, kita dapat menghindari risiko keamanan.
Dalam Django untuk mencegah cookies bocor, kita dapat menkonfigurasi
SESSION_COOKIE_SECURE dan CSRF_COOKIE_SECURE settings menjadi True.
Ref : https://docs.djangoproject.com/en/5.2/topics/security/

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama, Kita membuat fitur login, register dan logout
Untuk fitur login dan register kita dapat menggunakan method dari class yang disediakan Django
yakni UserCreationForm dan AuthenticationForm agar mudah mengimplementasi form-nya.
Selain itu juga fitur login kita gunakan fitur bawaan dari Django
Lalu kita membuat laman untuk login/register dan menghubungkan urlnya. Selain itu, kita
membuat laman utama/katalog/produk/addProduk untuk tidak dapat diakses sebelum aplikasi
memverifikasi user dengan menggunakan wrapper dari function yang kita import login_required
Saat login juga kita set cookies kapan terakhir kali pengguna login untuk menyimpan session pengguna
Untuk fitur logout, kita gunakan fitur bawaan juga dari Django untuk melepas user dari session terakhir.
Selain itu juga, saat logout kita buat agar cookies last_login dihapus

Kedua, menghubungkan product dengan user
Di models kita tambahkan foreignkey pada models kita untuk menandakan bahwa suatu produk memiliki
hubungan pada suatu object lalu kita hubungkan dengan User yang membuat product tersebut.
Kita buat juga product tidak dapat dibuat jika terdapat user yang aktif, namun untuk product yang dibuat sebelum tugas 4 itu kita buat agar tidak terhapus dengan null=True
Lalu tinggal kita lakukan migrasi Model karena terdapat perubahan pada model kita

Ketiga, kita lakukan perubahan dibeberapa berkas html.
Tampilkan last login di halaman utama
tambah filter produk user dan all di catalogue
tampilkan product ini milik siapa di detail_product.

Terakhir kita jalankan aplikasi di lokal.
Lalu saya buat 2 akun dan masing-masing akun melakukan 3 kali add product

/// END TUGAS 4 ///

/// TUGAS 5 ///
 Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
 Terdapat 3 jenis css selector, yakni inline-style, internal style sheet, dan external style sheet
 Priority penentuannya yakni inline > internal > external

 Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
 Responsive design itu menyesuaikan tampilan web tergantung display perangkat masing-masing
 Responsive design itu penting dalam memberi UX yang baik bagi pengguna aplikasi
 Contoh Aplikasi dengan responsive design itu Youtube, pada mobile banyaknya video yang ditampilkan di grid hanya 1
 dibanding di komputer yang bisa 3-4 tergantung layar, selain itu sidebar youtube diganti menjadi button menu di mobile
 Contoh Aplikasi yg tidak responsive adalah tugas ini dalam fase tugas-2 karena hanya berupa html dan tidak terdapat css yang dapat membantu membuat desain responsive

 Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
 Basically anggap terdapat elemen-elemen yang terbungkus dalam box-nya masing-masing
 margin berguna untuk mendefinisikan jarak antar 'box' elemen satu dengan elemen lainnya
 border sebagai pembatas tepian box elemen
 padding itu anggap sebagai jarak isi elemen ke tepian box
 implementasinya dalam css kita menggunakan class dimana kita bisa atur margin,border,padding untuk masing-masing kontainer <div>

 Jelaskan konsep flex box dan grid layout beserta kegunaannya!
 flex box itu memudahkan kita menata kontainer dalam satu baris atau kolom
 sementara grid layout itu mirip namun lebih presisi serta dapat 2 arah (baris dan kolom)
 kegunaan flexbox seperti membuat navbar, sidebar, button menu
 kegunaan grid layout seperti untuk membuat galeri atau list produk seperti pada online shop

 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
 
 Pertama Kita tambah fitur baru untuk mengedit dan mendelete product kita
 seperti biasa logikanya kita buat di views.py lalu kita hubungkan dengan html kita dan juga urlnya

 Lalu Kita buat navbar dan juga membuat responsicve design agar dapat mudah diakses di mobile dengan menambahkan
 menu button,
 Selain itu kita buat semacam card product untuk membuat penampilan produk kita seperti di toko online seperti biasanya

 Selain itu kita buat folder static untuk menyimpan external style, gambar, fonts yang ingin kita gunakan di app kita hubungkan di settings agar file static dapat diakses.

 kita ambil modul scripts tailwind melalui link dan juga hubungkan external style sheet kita ke base html
 Lalu kita mengkustomisasi desain web kita dengan senang hati.
 Saya mengincar kombinasi warna indigo dan abu gelap sebagai warna dasar
 