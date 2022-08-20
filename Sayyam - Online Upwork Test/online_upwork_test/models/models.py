# -*- coding: utf-8 -*-

from odoo import models, fields, api
from googletrans import Translator


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    languages_id = fields.Many2one('res.lang', domain="[('active', 'in', (False,True))]")
    language_result = fields.Char('Translated', translate=True)

    @api.onchange('name_backup', 'languages_id', 'name')
    def _onchange_name_translate(self):
        self.language_result = False
        if self.languages_id:
            source_language = 'en'
            destination_language = self.languages_id.url_code
            text_in = self.name
            translator = Translator()
            result = translator.translate(text_in, src=source_language, dest=destination_language)
            self.language_result = result.text
