from odoo import api, fields, models , _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    team_code_id = fields.Char(size=64, index=True, tracking=True)

    @api.model
    def create(self, values):
        res = super(ResPartner, self).create(values)
        # print('----------res--------------',res)

        # if values.get('team_code_id', 'New') == 'New':
        #     type_code = values.get('type_code', False)

        #     if type_code == 'hit':
        #         values['team_code_id'] = self.env['ir.sequence'].next_by_code('res.partner3')
        #         print('---------type_code----------',type_code)

        #     if type_code == 'dun':
        #         values['team_code_id'] = self.env['ir.sequence'].next_by_code('res.partner4')



        if not res.city_group:
            print('--------city_group---------------')
            pass
        else:
            sequence =self.env['ir.sequence'].next_by_code('res.partner1')
            # sequence1 = self.env['ir.sequence'].next_by_code('res.partner3')
            # sequence2 = self.env['ir.sequence'].next_by_code('res.partner4')
            # search_team_code = res.team_code_id
            # print('------search_team_code----------',search_team_code)

            search_code = self.env['res.partner'].search([('team_code_id', 'ilike', f'%{res.team_code_id}%')])
            for s in search_code:
                    print('------search_code----------',s.team_code_id)

            for r in res:
                print('---------r_team_code----------------',r.city_group['team_code'])
                # print('---------team_code----------------',r.search([('team_code_id', 'ilike', f'%{res.team_code_id}%')]))
                # search_code = s.search([('team_code_id', 'ilike', f'%{values}%')])
                team_code = r.city_group['team_code']

                # if r.type_code == 'hit':
                #     r.team_code_id = sequence1

                # if r.type_code == 'dun':
                #     r.team_code_id = sequence2


                team_code_id = team_code + sequence 
                print('------team_code_id----------',team_code_id)

                r.team_code_id = team_code_id

                # search_code = self.env['res.partner'].search([('team_code_id', 'ilike', "%s%s"%(team_code_id, '-'))])
                # for s in search_code:
                #         print('------search_code----------',s.team_code_id)
                        
                #         if s.team_code_id == r.team_code_id:
                #             print('-----------s.team_code_id------------------')
                #             # r.team_code_id = team_code_id
                #             sequence1 =self.env['ir.sequence'].next_by_code('res.partner2') or 'New'
                #             team_code_id = team_code + sequence1

                #             r.team_code_id = team_code_id

        return res

    # @api.model
    # def write(self, vals):
    #     res = super(ResPartner, self).write(vals)

    #     if not 'city_group' in vals:
    #         pass
    #     elif 'city_group' in vals:
    #         if not self.city_group:
    #             pass           
    #         else:
    #             print('-----------vals-----------',self.city_group)
    #             sequence =self.env['ir.sequence'].next_by_code('res.partner1') or 'New'
    #             print('-------sequence-------',sequence)
    #             for r in self:
    #                 print('---------r----------------',r.city_group['team_code'])
    #                 team_code = r.city_group.team_code
    #                 print('---------team_code----------------',team_code)

    #                 ref = r.code_id
    #                 print('----------team_ref---------------',ref)

    #                 # code_id = partner_code[:2] + ' ' + sequence + partner_code[2:]
    #                 # code_id = ref
    #                 # print('------code_id----------',code_id)
    #                 r.write({'code_id': ref})
    #     return res

