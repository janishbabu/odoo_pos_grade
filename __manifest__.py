{
    'name': "Product Grade",
    'version': "16.0.1.0.0",
    'sequence': -20,
    'summary': 'POS',
    'author': 'CYBROSYS',
    'installable': True,
    'application': True,

    'depends': ['base', 'point_of_sale'],
    'data': ['views/product_grade.xml'],
    'assets': {
        'point_of_sale.assets': [
            'product_grade/static/src/js/custom.js',
            'product_grade/static/src/xml/pos_screen.xml',
            'product_grade/static/src/xml/pos_recipt.xml',

        ],

    },
}
