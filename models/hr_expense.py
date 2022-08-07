# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrExpense(models.Model):
    _inherit = "hr.expense"
    
    supplier_id = fields.Many2one('res.partner', string="Proveedor")
    
    def action_expense_create_invoice(self):
        invoice_lines = [
            (
                0,
                0,
                {
                    "product_id": self.product_id.id,
                    "name": self.name,
                    "price_unit": self.unit_amount,
                    "quantity": self.quantity,
                    "account_id": self.account_id.id,
                    "analytic_account_id": self.analytic_account_id.id,
                    "tax_ids": [(6, 0, self.tax_ids.ids)],
                },
            )
        ]
        if not self.supplier_id:
            raise ValidationError('Este gasto no tiene establecido un proveedor para generar la factura.')
        invoice = self.env["account.move"].create(
            [
                {
                    "ref": self.reference,
                    "move_type": "in_invoice",
                    "invoice_date": self.date,
                    "invoice_line_ids": invoice_lines,
                    "partner_id": self.supplier_id.id,
                }
            ]
        )
        self.write(
            {
                "invoice_id": invoice.id,
                "quantity": 1,
                "tax_ids": False,
                "unit_amount": invoice.amount_total,
            }
        )
        return True