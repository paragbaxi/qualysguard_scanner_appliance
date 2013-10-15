qualysguard_scanner_appliance
=============================

Information on which asset groups scanner appliances are assigned to.

Writes asset groups with assigned scanners to sorted_by_asset_group.csv file.
Example file:
<pre>
Asset Group, Scanner 1, Scanner 2
All South Park Servers, db_scanner
Datacenters_rock, internal_latam, internal_na
</pre>

Writes scanners with assigned asset groups to sorted_by_scanners.csv file.
Example file:
<pre>
Scanner Appliance, Asset Group 1, Asset Group 2
Snowden_Scanner, Cisco IOS Platform, NSA's DB Platform
ZackMorrisScanner, Kelly
</pre>

Writes scanners not assigned to any asset groups to orphan_scanners.txt file.
Example file:
<pre>
Always_available_scanner
Lord_Voldemort
Superman_scanner
</pre>

Writes asset groups not assigned to any scanner to orphan_asset_groups.txt file.
Example file:
<pre>
Never_scanned
Reporting_asset_group
Wolverine
Mowgli
</pre>
