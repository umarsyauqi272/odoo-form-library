from odoo import models, fields, api


class library_management_class_member(models.Model):
    _name = 'library_management.member'
    _description = 'Data Siswa Member'

    nomor_induk = fields.Char(string="NIS")
    nama_siswa = fields.Char(string="Nama Siswa")
    tingkat = fields.Selection([('10','X'),('11','XI'),('12','XII')], string="Tingkat")
    jurusan = fields.Selection([('ipa','IPA'),('ips','IPS')], string="Jurusan")
    kelas = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], string="Kelas")
    tempat_lahir = fields.Char(string="Tempat Lahir")
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    alamat = fields.Char(string="Alamat")
    histori_pinjaman = fields.Char(string="Histori Pinjaman")
    no_telepon = fields.Char(string="Nomor Telepon")