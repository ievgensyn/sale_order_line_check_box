import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_check_box = fields.Boolean(
        string='Check Box', default=False)
