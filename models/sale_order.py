import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_express_shipping = fields.Boolean(
        string='Express Shipping', default=False)
