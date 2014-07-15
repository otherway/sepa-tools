# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2009 EduSense BV (<http://www.edusense.nl>).
#              (C) 2011 - 2013 Therp BV (<http://therp.nl>).
#    Copyright (C) 2014 Acysos S.L. (<http://acysos.com>).
#    @author: Ignacio Ibeas <ignacio@acysos.com>
#            
#    All other contributions are (C) by their respective contributors
#
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Account Payment - Payments Export Infrastructure',
    'version': '0.1.164',
    'license': 'AGPL-3',
    'author': 'Account Payment community',
    'website': 'https://launchpad.net/account-payment',
    'category': 'Banking addons',
    'depends': [
        'account_payment',
        'account_payment_extension',
        'base_iban',  # for manual_bank_tranfer
        ],
    'data': [
        'view/account_payment.xml',
        'view/bank_payment_manual.xml',
        'data/payment_type.xml',
    ],
    'description': '''
        Infrastructure to export payment orders.

        This technical module provides the base infrastructure to export 
        payment orders for electronic banking. It provides the following
        technical features:
        * a new payment.mode.type model
        * payment.mode now has a mandatory type
        * a better implementation of payment_mode.suitable_bank_types() based on payment.mode.type
        * the "make payment" button launches a wizard depending on the payment.mode.type
        * a manual payment mode type is provided as an example, with a default "do nothing" wizard
        
        Adapted to account_payment_extension by Acysos S.L. <info@acysos.com>
    ''',
    'auto_install': True,
    'installable': True,
}
