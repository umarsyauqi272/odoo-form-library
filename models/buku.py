from odoo import models, fields, api


class library_management_class_buku(models.Model):
    _name = 'library_management.buku'
    _description = 'Data Buku'

    judul_buku = fields.Char(string="Judul Buku")
    kategori_buku = fields.Char(string="Kategori")
    penulis_buku = fields.Char(string="Penulis")
    penerbit_buku = fields.Char(string="Penerbit")
    tahun_terbit = fields.Char(string="Tahun")
    kode_buku = fields.Char(string="Kode Buku")
    