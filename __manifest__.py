{
    'name': "Fiscal POS (Rep. Dominicana)",
    'summary': """Incorpora funcionalidades de facturación con NCF al POS.""",
    'author': "lfernandez",
    'depends': [
        'base',
        'point_of_sale',
        'l10n_do_accounting',
    ],
    'data': [
        'data/data.xml',
    ],
    # 'assets': {
    #     'point_of_sale.assets': [
    #         'l10n_do_pos/static/src/scss/*',
    #         'l10n_do_pos/static/src/js/**/*.js',
    #         'l10n_do_pos/static/src/xml/**/*.xml',
    #     ],
    # },
}
