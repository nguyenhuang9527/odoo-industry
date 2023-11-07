# -*- coding: utf-8 -*-
{
    'name': 'Hardware Shop',
    'version': '1.0',
    'category': 'Retail',
    'description': """
For Hardware shops that carry a large selection of products: plumbing, machinery, household, gardening, carpenter and electrical, etc.
Using Point of Sale, Inventory, Sales, Purchase, Accounting, Contact, Employee, Dashboard, Barcode, and Documents and E-commerce to grow their business.
    """,
    'author': 'Odoo S.A.',
    'depends': [
        'base_geolocalize',
        'knowledge',
        'pos_sale',
        'purchase_stock',
        'sale_margin',
        'sale_planning',
        'sale_project',
        'sale_purchase',
        'stock_delivery',
        'website_sale_comparison',
        'website_sale_loyalty',
        'website_sale_product_configurator',
        'website_sale_stock',
        'theme_kiddo',
    ],
    'data': [
        'data/res_config_setting.xml',
        'data/ir_attachment_pre.xml',
        'data/ir_ui_view.xml',
        'data/product_public_category.xml',
        'data/product_category.xml',
        'data/pos_category.xml',
        'data/product_template.xml',
        'data/product_attribute.xml',
        'data/product_attribute_value.xml',
        'data/product_pricelist.xml',
        'data/pos_config.xml',
        'data/product_template_attribute_line.xml',
        'data/product_template_attribute_value.xml',
        'data/product_product.xml',
        'data/product_image.xml',
        'data/knowledge_cover.xml',
        'data/knowledge_article.xml',
    ],
    'demo': [
        'demo/website.xml',
        'demo/res_partner.xml',
        'demo/product_supplierinfo.xml',
        'demo/website_attachment.xml',
        'demo/website_view.xml',
        'demo/purchase_order.xml',
        'demo/purchase_order_line.xml',
        'demo/purchase_order_confirm.xml',
        'demo/pos_config.xml',
        'demo/sale_order.xml',
        'demo/sale_order_line.xml',
        'demo/sale_order_confirm.xml',
        'demo/ir_attachment_post.xml',
        'demo/website_theme_apply.xml',
    ],
    'application': False,
    'license': 'OPL-1',
    'images': ['images/main.png'],
}