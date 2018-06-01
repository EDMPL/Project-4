# -*- coding: utf-8 -*-
from odoo import models, fields, api
class Payable(models.Model):
	_name = 'payable.forecast'
	_description = 'payable'
	
	nama = fields.Char('Nama', required=True)
	kategori = fields.Many2one('category.forecast', 'Category')
	keterangan = fields.Char('Keterangan', required=True)
	tanggal_peminjaman = fields.Date('Tanggal Peminjaman')
	tenggat_waktu = fields.Date('Tenggat Waktu', required=True)
	total_biaya  = fields.Integer('Total Biaya')