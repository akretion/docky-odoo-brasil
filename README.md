## Ambiente Docker Compose para desenvolvimento de Odoo no Brasil

```
sudo pip install git+https://github.com/akretion/ak.git@v2
sudo pip install --upgrade docky
git clone https://github.com/akretion/odoo-brasil-docky.git
cd docky-odoo-brasil/odoo
ak --verbose build
cd ..
docky build
docky run
# vc agora esta dentro do mundo magico do container
odoo
```
aponta agora seu navegador para http://odoo-brasil.dy (sem https nessa configuração de dev)

Documentação adicional:

- https://github.com/akretion/ak/wiki
- https://akretion.github.io/docky/
