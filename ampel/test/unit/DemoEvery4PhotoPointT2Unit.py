#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : Ampel-photometry/ampel/test/unit/DemoEvery4PhotoPointT2Unit.py
# License           : BSD-3-Clause
# Author            : vb <vbrinnel@physik.hu-berlin.de>
# Date              : 25.03.2020
# Last Modified Date: 28.03.2020
# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>

from time import time
from typing import Dict, ClassVar
from ampel.t2.T2UnitResult import T2UnitResult
from ampel.content.DataPoint import DataPoint
from ampel.abstract.AbsPointT2Unit import AbsPointT2Unit


class DemoEvery4PhotoPointT2Unit(AbsPointT2Unit):

	ingest: ClassVar[Dict] = {'eligible': {'pps': (3, None, 4)}}

	def run(self, datapoint: DataPoint) -> T2UnitResult:
		return {'result': {"time": time()}}