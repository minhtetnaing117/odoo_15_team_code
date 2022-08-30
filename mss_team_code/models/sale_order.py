from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    city_name_id = fields.Many2one('city.team', string="City Team")
    code_id = fields.Char(string='Code ID')

    


    @api.onchange('user_id')
    def onchange_user_id(self):
    	city_name = self.env['city.team'].search([('user_id', '=', self.user_id.id)])
    	# print('---------city_name----------',city_name)
    	for i in self:
    	    if i.user_id:
    	        # print('---------user_id----------',i.user_id['name'])
    	        i.city_name_id = city_name


    @api.onchange('partner_id')
    def onchange_partner_id(self):
    	# print('-------partner_id----------',self.partner_id.display_name)
    	# print('-------partner_id----------',self.partner_id.code_id)
    	self.code_id = self.partner_id.code_id