__author__ = 'pbaxi'

import csv
from lxml import objectify, etree
from qualysconnect.util import build_v1_connector, build_v2_connector
from collections import defaultdict

# Connect to QualysGuard API v2.
qgc2 = build_v2_connector()
# Create request and download XML.
request = 'appliance/?action=list&output_mode=full'
xml_output = qgc2.request(request)
# Process XML.
root = objectify.fromstring(xml_output)
# XML:
# Scanner
# -- AG
# -- AG2
# Scanner2
# -- AG
#
# Change to:
# AG
#  -- SCANN
#
# Count number of uniquely assigned scanners & asset groups.
max_number_of_scanners = 0
max_number_of_asset_groups = 0
orphan_scanners = []
asset_groups = defaultdict(list)
scanners = defaultdict(list)
# Parse XML.
list_of_scanners = []
for appliance in root.RESPONSE.APPLIANCE_LIST.APPLIANCE:
    try:
        for asset_group in appliance.ASSET_GROUP_LIST.ASSET_GROUP:
            # For sorted by scanners.
            asset_groups[asset_group.NAME.text].append(appliance.NAME.text)
            max_number_of_scanners = max(len(asset_groups[asset_group.NAME.text])+1, max_number_of_scanners)
            # For sorted by asset group.
            scanners[appliance.NAME.text].append(asset_group.NAME.text)
            max_number_of_asset_groups = max(len(scanners[appliance.NAME.text])+1, max_number_of_asset_groups)
    except AttributeError, e:
        orphan_scanners.append(appliance.NAME.text + '\n')
# Write CSV for AG, Scanner_1, Scanner_2, Scanner_3...
with open('sorted_by_asset_group.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    # Write header.
    scanner_header = []
    for i in range(1,max_number_of_scanners):
        scanner_header.append('Scanner %s' % i)
    wr.writerow(['Asset Group'] + scanner_header)
    # Write data.
    for asset_group in sorted(asset_groups):
        wr.writerow([asset_group] + sorted(asset_groups[asset_group]))
print 'Successfully wrote asset groups with assigned scanners to sorted_by_asset_group.csv file.'
# Write CSV for Scanner, AG_1, AG_2, AG_3, ...
with open('sorted_by_scanners.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    # Write header.
    asset_group_header = []
    for i in range(1,max_number_of_asset_groups):
        asset_group_header.append('Asset Group %s' % i)
    wr.writerow(['Scanner Appliance'] + asset_group_header)
    # Write data.
    for scanner in sorted(scanners):
        wr.writerow([scanner] + scanners[scanner])
print 'Successfully wrote scanners with assigned asset groups to sorted_by_scanners.csv file.'
# Write orphan scanners to text file.
with open('orphan_scanners.txt', 'wb') as myfile:
    myfile.writelines(sorted(orphan_scanners))
print 'Successfully wrote scanners not assigned to any asset groups to orphan_scanners.txt file.'
