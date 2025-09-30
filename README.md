# Babies Data Processor 🍼

Selamat datang di proyek **Babies Data Processor**. Proyek ini adalah alat berbasis Python yang dirancang untuk memproses dan menganalisis data kesehatan bayi dari database MySQL. Dengan menggunakan pustaka `pandas`, proyek ini dapat mengubah data mentah menjadi tabel pivot yang terstruktur, memudahkan analisis seperti melacak berat badan, tinggi badan, dan riwayat imunisasi seiring bertambahnya usia bayi.

Proyek ini menggunakan **Poetry** untuk manajemen dependensi dan `.env` untuk mengelola kredensial database dengan aman.

---

### Fitur Utama

* **Ekstraksi Data**: Menggunakan `mysql-connector` untuk terhubung ke database dan mengambil data kesehatan bayi.
* **Transformasi Data**: Memanfaatkan `pandas` untuk melakukan pivoting data, membuat tabel yang mudah dibaca dan dianalisis.
* **Penyaringan Data**: Menyaring data berdasarkan kriteria tertentu, seperti riwayat pemeriksaan atau usia.
* **Manajemen Proyek Efisien**: Menggunakan Poetry untuk instalasi dependensi yang mudah dan konsisten.
* **Konfigurasi Aman**: Menyimpan kredensial database dalam file `.env` yang tidak akan diunggah ke Git.

---

### Persyaratan

Pastikan Anda memiliki hal-hal berikut terinstal di sistem Anda:

* **Python 3.10** atau lebih baru
* **Poetry**
* **Database MySQL** dengan skema yang sesuai (misalnya, `iposyandu`)

### Instalasi

Ikuti langkah-langkah di bawah ini untuk menginstal dan menyiapkan proyek:

1.  **Clone repositori Git** ke komputer Anda:
    ```bash
    git clone [https://github.com/username/babies-data-processor.git](https://github.com/username/babies-data-processor.git)
    cd babies-data-processor
    ```
2.  **Instal dependensi** menggunakan Poetry:
    ```bash
    poetry install
    ```
    Ini akan membaca file `pyproject.toml` dan menginstal semua pustaka yang diperlukan.

3.  **Buat file konfigurasi `.env`**:
    Salin file `.env.example` (jika ada) atau buat file baru bernama `.env` di direktori root proyek. Masukkan detail koneksi database Anda di dalamnya.
    ```env
    DB_HOST=127.0.0.1
    DB_DATABASE=iposyandu
    DB_USER=root
    DB_PASSWORD=
    ```

---

### Cara Menggunakan

Proyek ini telah dikonsolidasikan menjadi satu skrip utama yang menjalankan seluruh alur kerja. Untuk menjalankan semua proses (ekstraksi, pivoting, dan penyaringan), cukup jalankan skrip dari terminal:

```bash
poetry run python babies_data_processor/main.py
