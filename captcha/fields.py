from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.forms import fields, ValidationError

from models import Captcha
import widgets

from datetime import datetime, timedelta
import md5

class CaptchaField(fields.Field):
    widget = widgets.CaptchaInput
    
    def clean(self, value):
        try:
            solution = md5.new(value.lower()).hexdigest()
            min_datetime = datetime.now() - timedelta(seconds = 300)
            captcha = Captcha.objects.get(solution = solution, date_generated__gte = min_datetime)
            
            captcha.delete()
            
            return True
            
        except Captcha.DoesNotExist:
            raise ValidationError(_('Wrong code!'))
