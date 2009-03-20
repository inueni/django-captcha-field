from django.conf import settings
from django.db import models
from image import CaptchaImage

import md5

class Captcha(models.Model):
    solution = models.CharField(max_length = 32)
    date_generated = models.DateTimeField(auto_now_add = True)
    
    def __init__(self, *args, **kwargs):
        super(Captcha, self).__init__(*args, **kwargs)
        
        captchaObj = CaptchaImage()
        
        self.filename = '%s.png' % md5.new(captchaObj.solution.lower()).hexdigest()
        self.url = u'%s%s' % (settings.CAPTCHA_IMAGES_URL, self.filename)
        
        img = captchaObj.render()
        img.save(u'%s%s' % (settings.CAPTCHA_IMAGES_PATH, self.filename))
        
        self.solution = md5.new(captchaObj.solution.lower()).hexdigest()
        self.save()
