from django.forms import widgets
from django.utils.safestring import mark_safe

from models import Captcha

class CaptchaInput(widgets.Widget):
    def render(self, name, value, attrs = None):
        captcha = Captcha()
        
        raw_html = u'<input type="text" name="%s" />' % name
        raw_html = u'%s \r\n %s' % (raw_html, u'<img class="captcha" src="%s" />' % captcha.url)
        
        return mark_safe(raw_html)
