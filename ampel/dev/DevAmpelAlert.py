#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : ampel/dev/DevPhotoAlert.py
# License           : BSD-3-Clause
# Author            : matteo giomi <matteo.giomi@desy.de>
# Date              : 13.06.2018
# Last Modified Date: 04.07.2018
# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>

from ampel.alert.PhotoAlert import PhotoAlert

class DevPhotoAlert(PhotoAlert):
	"""
	Subclass of PhotoAlert, containing cutouts and additional attributes that are
	useful for plotting and inspecting the alert content.
	"""

	cutout_names = ('cutoutScience', 'cutoutTemplate', 'cutoutDifference')
	
	
	@staticmethod
	def load_from_avro_content(avro_content):
		"""
			return a DevPhotoAlert from a dictionary with the avro alert content.
		"""
		
		# parse detections and upper limits
		if avro_content.get('prv_candidates') is not None:
			pps = [avro_content['candidate']]
			pps.extend( 
				[el for el in avro_content['prv_candidates'] if el.get('candid') is not None]
					)
			uls = [el for el in avro_content['prv_candidates'] if el.get('candid') is None]
		else:
			pps = [avro_content['candidate']]
			uls = None
		
		# get image cutouts
		co_dict = {}
		for co_name in DevPhotoAlert.cutout_names:	#TODO: or classmethod?
			co_dict[co_name] = avro_content.get(co_name, {}).get('stampData')
		
		# return the DevPhotoAlert
		return DevPhotoAlert(avro_content['objectId'], pps, uls, co_dict)



	def __init__(self, tran_id, list_of_pps, list_of_uls=None, cutout_dict=None):
		"""
		DevPhotoAlert constructor.
		
		Parameters:
		-----------
		
		alertid:
			unique identifier of the alert (for ZTF: candid of most recent photopoint)
		
		tran_id:
			the astronomical transient object ID, for ZTF IPAC alerts 'objectId'
		
		list_of_pps:
			a flat list of photopoint dictionaries.
		
		cutout_dict:
			dict with the three cutouts ('cutoutScience', 'cutoutTemplate', 'cutoutDifference')
		"""
		
		PhotoAlert.__init__(self, tran_id, list_of_pps, list_of_uls)
		
		# add the cutouts if available
		if cutout_dict is None:
			cutout_dict = {}
		else:
			self.cutout_dict = cutout_dict


	def get_cutout(self, which):
		"""
			return cutout staps for given image product
		"""
		if which not in DevPhotoAlert.cutout_names:
			raise KeyError("requested cutout for %s. Available are %s"%
				(which, ", ".join(DevPhotoAlert.cutout_names)))
		return self.cutout_dict.get(which)

	def retrieve_cutouts_from_db(self, source):
		"""
			retrieve the cutouts for this alert from the Ampel Database
		"""
		pass


