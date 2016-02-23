from django.db import models


class FabricModel(models.Model):
	SKIN = 'skin'
	FABRIC = 'fabric'
	CARPETING = 'carpeting'

	FABRIC_CHOICE = (
		(SKIN, 'кожа',),
		(FABRIC, 'ткань',),
		(CARPETING, 'ковролин',),
	)

	type_of_fabric = models.CharField(max_length=9, choices=FABRIC_CHOICE, default=SKIN)
	image = models.ImageField()
	name = models.CharField(max_length=100, db_index=True)
	description = models.TextField()

	def __str__(self):
		return self.name

	class Meta:
		unique_together = ('name', 'type_of_fabric',)