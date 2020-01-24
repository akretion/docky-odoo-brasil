# Copyright (C) 2020  Renato Lima - Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from anthem.lyrics.records import create_or_update


def create_partners(ctx):
    names = [('Partner Name', 'partner_1')]
    for name, xmlid in names:
        create_or_update(ctx, 'res.partner', xmlid, {'name': name})


def main(ctx):
    # create_partners(ctx)
