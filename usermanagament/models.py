from django.db import models

BOT_USERNAME = 'markettesttest_bot'


class Profile(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    points = models.IntegerField(default=0)
    referral_link = models.CharField(max_length=500, blank=True, null=True)
    referred_by = models.IntegerField(default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.referral_link:
            self.referral_link = f"https://t.me/{BOT_USERNAME}?start={self.telegram_id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username if self.username else str(self.telegram_id)
