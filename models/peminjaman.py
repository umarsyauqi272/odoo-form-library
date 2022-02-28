from odoo import models, fields, api


class library_management_class_peminjaman(models.Model):
    _name = 'library_management.peminjaman'
    _description = 'Data Peminjaman'

    kode_peminjaman = fields.Char(string="Kode Peminjaman")
    nama_peminjam = fields.Many2one('library_management.member', string="Nama Peminjam")
    buku_pinjaman = fields.Many2one('library_management.peminjaman', string="Buku Pinjaman")
    tanggal_pinjam_awal = fields.Date(string="Tanggal Peminjaman")
    tanggal_pinjam_akhir = fields.Date(string="Tanggal Pengembalian")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('dipinjam', 'Dipinjam'),
        ('sudah_kembali', 'Sudah Dikembalikan'),
        ('batal', 'Batal'),],
        "State", default='draft', readonly=True, copy=False)

    # @api.onchange('kode_peminjaman')
    # def action_confirm(self):
    #     self.state = "dipinjam"
 
    # @api.onchange
    # def action_cancel(self):
    #     self.state = "batal"
 
    # @api.onchange
    # def action_close(self):
    #     self.state = "sudah_kembali"