#!/usr/bin/env python
# ---------------------------
# Created by Richard Barrett
# Date: 02/07/2019
# ============================

# ============================
#         **NOTES**
# ============================

# Script will check all OSDs 'ceph osd df tree'
# Script needs to detect at least 10 OSDs that are least and greatest filled
# Script will gather and sort into two lists: Least & Greatest OSDs filled
# Script will invoke another script that is watching cluster health status "watch ceph -s"
# Script will start reblancing act and sort OSD rebalance on 

# Notes from CEPH SME:Konstiantyn Donilov
# =======================================
# First check that crush has only one rule.
# Order doesn't matter
# Take top ~10 osd's, decrease their weight by 5-10%
# Do 'ceph osd crush reweigt' one by one and wait for rebalance to complete before starting the next one 
# Than take ~10 least loaded. Repeat until difference between most and least loaded will be in ~10% range.


# For 10 Least filled increase weight
# -----------------------------------
# Script will increase the weights of the least OSDs first
# Script collect a list of these OSDs and rebalance each one that is least filled and wait for cluster rebalance

# For 10 Most filled decrease weight
# ----------------------------------
# Script needs to detect at least OSDs are least and greatest filled
# Script will increase the weights of the least OSDs first
# Script collect a list of these OSDs and rebalance each one that is least filled and wait for cluster rebalance
# ==============================================================================================================

# Script will check OSD DF and put into a file
ceph osd df tree >> ceph_osd_free.log

# Set variables for greatest and least filled OSDs
ceph_osd_least = "$command that parses cep_osd_free.log"
ceph_osd_greatest = "$command that parses cep_osd_free.log"

