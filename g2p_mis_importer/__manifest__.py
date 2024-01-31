# Part of openG2P. See LICENSE file for full copyright and licensing details.

{
    "name": "G2P MIS Importer",
    "category": "G2P",
    "version": "17.0.1.0.0",
    "author": "OpenG2P",
    "website": "https://github.com/OpenG2P/openg2p-auth",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": ["g2p_registry_rest_api", "g2p_programs", "queue_job"],
    "data": [
        "security/ir.model.access.csv",
        "views/mis_config_views.xml",
        "views/mis_menu.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
