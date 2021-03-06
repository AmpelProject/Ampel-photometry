#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : Ampel-photometry/ampel/demo/unit/base/DemoEvery3PhotoPointT2Unit.py
# License           : BSD-3-Clause
# Author            : vb <vbrinnel@physik.hu-berlin.de>
# Date              : 25.03.2020
# Last Modified Date: 07.08.2020
# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>

from time import time
from typing import Dict
from ampel.type import T2UnitResult
from ampel.content.DataPoint import DataPoint
from ampel.abstract.AbsPointT2Unit import AbsPointT2Unit


class DemoEvery3PhotoPointT2Unit(AbsPointT2Unit):

	ingest: Dict = {'eligible': {'pps': (2, None, 3)}}

	def run(self, datapoint: DataPoint) -> T2UnitResult:
		return {"id": datapoint['_id'], "time": time()}
