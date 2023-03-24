from odoo import models, api, fields
from odoo.http import request


class ProductGrade(models.Model):
    _inherit = "product.product"

    grade = fields.Selection(string='Grade',
                             selection=[('A', 'A'),
                                        ('B', 'B'), ('C', 'C')],
                             default='A')


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('grade')
        return result

