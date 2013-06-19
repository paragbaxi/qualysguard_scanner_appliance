qualysguard_scanner_appliance
=============================

Information on which asset groups scanner appliances are assigned to.

License: GPL (http://www.gnu.org/licenses/gpl.html)

Writes asset groups with assigned scanners to sorted_by_asset_group.csv file.
Example file:
Asset Group, Scanner 1, Scanner 2
All South Park Servers, db_scanner
Datacenters_rock, internal_latam, internal_na

Writes scanners with assigned asset groups to sorted_by_scanners.csv file.
Example file:
Scanner Appliance, Asset Group 1,	Asset Group 2
Snowden-Scanner, Cisco IOS Platform,	NSA's DB Platform
ZACScanner, SA SuSE11

Writes scanners not assigned to any asset groups to orphan_scanners.txt file.
Example file:
Ambivalent_scanner
Lonely_scanner
Sad_scanner
