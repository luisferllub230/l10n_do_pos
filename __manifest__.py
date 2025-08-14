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
        'views/res_config_settings_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'l10n_do_pos/static/src/app/models/*.js',
        ],
    },
}
