# Boxwise

Boxwise is an open-source web-app,
which makes it easy for organisations
to source, store and distribute
donated goods to people in need
in a fair and dignified way.

This is a new version of [the original Drop App used by Drop In The Ocean](https://www.drapenihavet.no/en/the-drop-app-2/). The [original app](https://bitbucket.org/wishingtree/themarket/src/master/) was limited to just managing a single organization. This is a rewrite to support multiple organizations on a centrally hosted system.

Check out [our webpage](https://www.boxwise.co) for more information!

## Contributing

We are always looking for help. Working on this project is an opportunity to use your skills to help thousands of refugees. [Our contributing guide](CONTRIBUTING.md) has more information.

Please also check out our [Code of Conduct](CODE_OF_CONDUCT.md)!

## Community

[We have a Slack for discussing development and to get support. Join the #dev and #support channel.](https://join.slack.com/t/boxwise/shared_invite/enQtMzE4NzExMjkxNTM2LTk0MzY2Mjg0MTY5ZmJjMjI1ODNmODZiNmJlNTAwM2Y4MmJkZDJjZWEyNzk0YTQyZGI0ZTYxMTc2NTgxNjk1ZTM)

## Setting up development environment

1.  Install odoo v11. We created [a Boxwise dev-setup](https://github.com/boxwise/boxwise-doodba). It is based on a docker environment for development and production of odoo by Tecnativa. It should just be 5 commands and you are ready to go. You have to have [docker](https://docs.docker.com/install/) and docker-compose installed for this dev-setup.

2.  Clone this folder into the [private src folder](https://github.com/boxwise/boxwise-doodba/tree/11.0_wms/odoo/custom/src/privates) of your setup. **Please do NOT rename the boxwise_wms repository!**

    `git clone https://github.com/boxwise/boxwise_wms.git`

3.  We recommend that you create your own database before you log in. There you can choose your own log in credentials and leave out the demo data of the default installation. 

    - Open up odoo, e.g. `http://localhost:11069/web/database/manager`
    - Click "Create Database"

4. Activate the developer mode! There two ways:

    1. Add `debug` in the url --> `localhost:11069/web?debug#....` or
    2. Go to settings and click the link hidden beneath the credentials on the far right! 

5.  Install the `boxwise_wms` module!

    - Go to the Apps menu!
    - Click in the left-hand menu `Update Apps List`!
    - Search for boxwise_wms! Remove the `Apps` filter from the search bar to see all custom modules available!
    - Click `Install`!
    
The following steps are required if [Issue #13](https://github.com/boxwise/boxwise_wms/issues/13) and [Issue #15](https://github.com/boxwise/boxwise_wms/issues/15) are not yet solved.

6.  Check out the links above and enable the settings / user rights by hand.

## Useful Links

We are using the open source ERP system odoo as the base for Boxwise. 

**First, here are some links about odoo itself:**

1. Dev doc:
https://www.odoo.com/documentation/11.0/index.html
2. Dev doc about creating a module: 
https://www.odoo.com/documentation/11.0/howtos/backend.html
3. Books:
https://drive.google.com/drive/folders/1AB18OISimJ5jewCBXJuTi6EDVwd84lXW
4. odoo github
https://github.com/odoo
5. odoo code search to find all official modules
http://odoo-code-search.com/

**And the odoo community:**

1. OCA webpage
https://odoo-community.org/
2. OCA Contributing Guidelines
https://odoo-community.org/page/contributing
3. OCA github
https://github.com/OCA
4. OCA maintainer tools
https://github.com/OCA/maintainer-tools
5. OCA maintainer tools wiki
https://github.com/OCA/maintainer-tools/wiki
6. OCA module template
https://github.com/OCA/maintainer-tools/tree/master/template/module

**The odoo JS framework:**

1. Introduction video from odoo conference:
https://www.youtube.com/watch?v=H-iFhOh1tOE
2. JS Dev Doc:
https://www.odoo.com/documentation/11.0/reference/javascript_reference.html
3. JS Command Index:
https://www.odoo.com/documentation/11.0/reference/javascript_api.html
4. JS Quick ref:
https://www.odoo.com/documentation/11.0/reference/javascript_cheatsheet.html 
