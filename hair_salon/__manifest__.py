# -*- coding: utf-8 -*-
{
    'name': 'Hair Salon',
    'version': '1.0',
    'category': 'Services',
    'description': """
        This module is for hair salons providing hair-related services such as hair cutting, brushing, coloring, hair and
        scalp treatments, beard and mustache shaping.
    """,
    'author': 'Odoo S.A.',
    'depends': [
        'account_edi_ubl_cii',
        'base_geolocalize',
        'hr_hourly_cost',
        'knowledge',
        'pos_loyalty',
        'project_enterprise',
        'project_sms',
        'sales_team',
        'website_appointment',
        'theme_orchid',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/project_task_type.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/product_pricelist_item.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/knowledge_article.xml',
        'data/knowledge_article_member.xml',
        'data/appointment_type.xml',
    ],
    'demo': [
        'demo/website.xml',
        'demo/res_partner.xml',
        'demo/res_users.xml',
        'demo/hr_employee.xml',
        'demo/appointment_type.xml',
        'demo/loyalty_program.xml',
        'demo/loyalty_rule.xml',
        'demo/calendar_event.xml',
        'demo/website_ir_attachment.xml',
        'demo/website_view.xml',
        'demo/website_page.xml',
        'demo/website_menu.xml',
        'demo/website_theme_apply.xml',
    ],
    'application': False,
    'license': 'OPL-1',
    'images': ['images/main.png'],
}
