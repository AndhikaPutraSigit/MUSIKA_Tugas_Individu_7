MUSIKA LEGACY - TUGAS INDIVIDU 7

Instalasi:
1. Buka folder project di VS Code.
2. Buat virtual environment (opsional): python -m venv venv
3. Aktifkan: .\venv\Scripts\activate (Windows)
4. Install: pip install -r requirements.txt
5. Jalankan: python app.py
6. Buka http://127.0.0.1:5000

Halaman tugas:
- Form Kontak: http://127.0.0.1:5000/kontak
- Dashboard Admin: http://127.0.0.1:5000/admin
- Form Tambah Produk: http://127.0.0.1:5000/admin/produk/tambah

Fitur TI 7:
- Flask-WTF untuk dua form.
- Validator DataRequired, Length, Email, NumberRange, Optional.
- CSRF aktif global dan token ada di kedua form melalui hidden_tag().
- Error ditampilkan di bawah field; data input dipertahankan oleh WTForms.
- PRG dengan redirect setelah data valid dan flash message.
- Bootstrap untuk Dashboard Admin dan form.

Catatan: data produk dan pesan disimpan di memori Python, sehingga kembali kosong saat server dimulai ulang. SECRET_KEY demo harus diganti dengan nilai rahasia dari environment variable sebelum deployment.
