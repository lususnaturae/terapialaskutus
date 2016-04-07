Teknologiademo Terapialaskutus (Therapy Invoicing)
==============================

Kelan hyväksymä psykoterapeutti voi hallita asiakastietoja, asiakastapaamisia ja luoda laskut asiakkaalle. Lisäksi sovelluksella voi luoda viralliset Kelan tilitykset ja asiakaskohtaiset Kela laskut.

Kelan sivuilla Kuntoutuspsykoterapia_.

.. _Kuntoutuspsykoterapia: http://www.kela.fi/tyoikaisille_kuntoutuspsykoterapia


Teknologiademon rakennuspalikat:

* Terapialaskutus on Python kielellä toteutettu Django_ 1.9 alustan päälle.
* Projektipohjana on käytetty cookiecutter-django_.
* Tietokantana käytössä Postgres_.
* Käyttöliittymässä on käytössä Bootstrap_ v4.
* Testauksessa käytetty factoryboy_, unittest_, test_plus_ ja UI testauksessa Selenium_.
* Asennusohjeet sisältävät ohjeet asennukseen Heroku_ alustalle.


.. _cookiecutter-django: http://cookiecutter-django.readthedocs.org/en/latest/
.. _Heroku: https://www.heroku.com/
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _test_plus: http://django-test-plus.readthedocs.org/en/latest/#
.. _Selenium: http://selenium-python.readthedocs.org/index.html
.. _factoryboy: https://factoryboy.readthedocs.org/en/latest/
.. _Postgres: http://www.postgresql.org/
.. _Django: https://www.djangoproject.com/
.. _Bootstrap: http://blog.getbootstrap.com/2015/08/19/bootstrap-4-alpha/

Ohjelmassa on neljä perus modulia:

1. **customers** asiakastietojen ja tapaamisten hallintaan
2. **customerinvoicing** asiakaslaskujen luontiin
3. **kelainvoicing** kelatilitysten ja asiakaskohtaisten kelalaskujen luontiin
4. **api** tarjoamaan kuukausilaskutustiedot d3.js komponentille toteutuneen laskutuksen pylväsgrafiikan muodostamiseen

Asennus
-------

Tuotantoympäristön asennus Heroku alustalle (Production installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

docs/deploy.rst

Demoympäristö asennus Heroku alustalle (Demosite installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

docs/install_demosite.rst

Kehitysympäristön asennus paikalliseen työasemaan (Development installation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

docs/install_dev.rst






