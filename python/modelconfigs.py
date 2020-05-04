#!/usr/bin/python3
import sys
import os
import argparse
import random
import time
import logging
import json
import datetime
import math

b6c96 = {
  "version":8,
  "support_japanese_rules":True,
  "use_fixup":True,
  "use_scoremean_as_lead":False,
  "trunk_num_channels":96,
  "mid_num_channels":96,
  "regular_num_channels":64,
  "dilated_num_channels":32,
  "gpool_num_channels":32,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","gpool"],
    ["rconv4","regular"],
    ["rconv5","gpool"],
    ["rconv6","regular"]
  ],
  "p1_num_channels":32,
  "g1_num_channels":32,
  "v1_num_channels":32,
  "sbv2_num_channels":48,
  "v2_size":64
}

b10c128 = {
  "version":8,
  "support_japanese_rules":True,
  "use_fixup":True,
  "use_scoremean_as_lead":False,
  "trunk_num_channels":128,
  "mid_num_channels":128,
  "regular_num_channels":96,
  "dilated_num_channels":32,
  "gpool_num_channels":32,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","gpool"],
    ["rconv6","regular"],
    ["rconv7","regular"],
    ["rconv8","gpool"],
    ["rconv9","regular"],
    ["rconv10","regular"]
  ],
  "p1_num_channels":32,
  "g1_num_channels":32,
  "v1_num_channels":32,
  "sbv2_num_channels":64,
  "v2_size":80
}

b15c192 = {
  "version":8,
  "support_japanese_rules":True,
  "use_fixup":True,
  "use_scoremean_as_lead":False,
  "trunk_num_channels":192,
  "mid_num_channels":192,
  "regular_num_channels":128,
  "dilated_num_channels":64,
  "gpool_num_channels":64,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","regular"],
    ["rconv7","gpool"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","regular"],
    ["rconv12","gpool"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"]
  ],
  "p1_num_channels":32,
  "g1_num_channels":32,
  "v1_num_channels":32,
  "sbv2_num_channels":80,
  "v2_size":96
}

b20c256 = {
  "version":8,
  "support_japanese_rules":True,
  "use_fixup":True,
  "use_scoremean_as_lead":False,
  "trunk_num_channels":256,
  "mid_num_channels":256,
  "regular_num_channels":192,
  "dilated_num_channels":64,
  "gpool_num_channels":64,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","regular"],
    ["rconv7","gpool"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","regular"],
    ["rconv12","gpool"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","regular"],
    ["rconv17","gpool"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"]
  ],
  "p1_num_channels":48,
  "g1_num_channels":48,
  "v1_num_channels":48,
  "sbv2_num_channels":96,
  "v2_size":112
}

b30c320 = {
  "version":8,
  "support_japanese_rules":True,
  "use_fixup":True,
  "use_scoremean_as_lead":False,
  "trunk_num_channels":320,
  "mid_num_channels":320,
  "regular_num_channels":224,
  "dilated_num_channels":96,
  "gpool_num_channels":96,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","gpool"],
    ["rconv7","regular"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","gpool"],
    ["rconv12","regular"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","gpool"],
    ["rconv17","regular"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"],
    ["rconv21","gpool"],
    ["rconv22","regular"],
    ["rconv23","regular"],
    ["rconv24","regular"],
    ["rconv25","regular"],
    ["rconv26","gpool"],
    ["rconv27","regular"],
    ["rconv28","regular"],
    ["rconv29","regular"],
    ["rconv30","regular"]
  ],
  "p1_num_channels":48,
  "g1_num_channels":48,
  "v1_num_channels":48,
  "sbv2_num_channels":112,
  "v2_size":128
}

b40c256 = {
  "version":8,
  "support_japanese_rules":True,
  "use_fixup":True,
  "use_scoremean_as_lead":False,
  "trunk_num_channels":256,
  "mid_num_channels":256,
  "regular_num_channels":192,
  "dilated_num_channels":64,
  "gpool_num_channels":64,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","gpool"],
    ["rconv7","regular"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","gpool"],
    ["rconv12","regular"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","gpool"],
    ["rconv17","regular"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"],
    ["rconv21","gpool"],
    ["rconv22","regular"],
    ["rconv23","regular"],
    ["rconv24","regular"],
    ["rconv25","regular"],
    ["rconv26","gpool"],
    ["rconv27","regular"],
    ["rconv28","regular"],
    ["rconv29","regular"],
    ["rconv30","regular"],
    ["rconv31","gpool"],
    ["rconv32","regular"],
    ["rconv33","regular"],
    ["rconv34","regular"],
    ["rconv35","regular"],
    ["rconv36","gpool"],
    ["rconv37","regular"],
    ["rconv38","regular"],
    ["rconv39","regular"],
    ["rconv40","regular"]
  ],
  "p1_num_channels":48,
  "g1_num_channels":48,
  "v1_num_channels":48,
  "sbv2_num_channels":112,
  "v2_size":128
}

b40c384 = {
  "version":8,
  "support_japanese_rules":True,
  "use_fixup":True,
  "use_scoremean_as_lead":False,
  "trunk_num_channels":384,
  "mid_num_channels":384,
  "regular_num_channels":256,
  "dilated_num_channels":128,
  "gpool_num_channels":128,
  "block_kind": [
    ["rconv1","regular"],
    ["rconv2","regular"],
    ["rconv3","regular"],
    ["rconv4","regular"],
    ["rconv5","regular"],
    ["rconv6","gpool"],
    ["rconv7","regular"],
    ["rconv8","regular"],
    ["rconv9","regular"],
    ["rconv10","regular"],
    ["rconv11","gpool"],
    ["rconv12","regular"],
    ["rconv13","regular"],
    ["rconv14","regular"],
    ["rconv15","regular"],
    ["rconv16","gpool"],
    ["rconv17","regular"],
    ["rconv18","regular"],
    ["rconv19","regular"],
    ["rconv20","regular"],
    ["rconv21","gpool"],
    ["rconv22","regular"],
    ["rconv23","regular"],
    ["rconv24","regular"],
    ["rconv25","regular"],
    ["rconv26","gpool"],
    ["rconv27","regular"],
    ["rconv28","regular"],
    ["rconv29","regular"],
    ["rconv30","regular"],
    ["rconv31","gpool"],
    ["rconv32","regular"],
    ["rconv33","regular"],
    ["rconv34","regular"],
    ["rconv35","regular"],
    ["rconv36","gpool"],
    ["rconv37","regular"],
    ["rconv38","regular"],
    ["rconv39","regular"],
    ["rconv40","regular"]
  ],
  "p1_num_channels":64,
  "g1_num_channels":64,
  "v1_num_channels":64,
  "sbv2_num_channels":128,
  "v2_size":144
}

config_of_name = {
  "b6c96": b6c96,
  "b10c128": b10c128,
  "b15c192": b15c192,
  "b20c256": b20c256,
  "b30c320": b30c320,
  "b40c256": b40c256,
  "b40c384": b40c384
}
