from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange, Optional

class ContactForm(FlaskForm):
    name = StringField("Nama", validators=[DataRequired(message="Nama wajib diisi."), Length(min=3, max=60, message="Nama harus 3–60 karakter.")])
    email = StringField("Email", validators=[DataRequired(message="Email wajib diisi."), Email(message="Format email tidak valid.")])
    subject = StringField("Subjek", validators=[Optional(), Length(max=100, message="Subjek maksimal 100 karakter.")])
    message = TextAreaField("Pesan", validators=[DataRequired(message="Pesan wajib diisi."), Length(min=10, max=1000, message="Pesan harus 10–1000 karakter.")])
    submit = SubmitField("Kirim Pesan")


class ProductForm(FlaskForm):
    name = StringField("Nama Produk", validators=[DataRequired(message="Nama produk wajib diisi."), Length(min=3, max=50, message="Nama produk harus 3–50 karakter.")])
    category = SelectField("Kategori", choices=[("1", "Electric Guitar"), ("2", "Acoustic Guitar"), ("3", "Bass Guitar"), ("4", "Drum Set"), ("5", "Keyboard"), ("6", "Amplifiers")], validators=[DataRequired(message="Pilih kategori produk.")])
    price = IntegerField("Harga (Rupiah)", validators=[DataRequired(message="Harga wajib diisi."), NumberRange(min=1, message="Harga harus lebih dari 0.")])
    stock = IntegerField("Stok", validators=[DataRequired(message="Stok wajib diisi."), NumberRange(min=0, message="Stok tidak boleh negatif.")])
    description = TextAreaField("Deskripsi", validators=[DataRequired(message="Deskripsi wajib diisi."), Length(min=10, max=300, message="Deskripsi harus 10–300 karakter.")])
    submit = SubmitField("Simpan Produk")