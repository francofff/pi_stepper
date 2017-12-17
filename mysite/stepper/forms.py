from django import forms
from stepper.models import Angle

class AngleForm(forms.ModelForm):
	set_angle = forms.IntegerField()

	class Meta:
		model = Angle
		fields = ('set_angle',)
