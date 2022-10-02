from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
from django.utils.datetime_safe import date


class Client(models.Model):
    PROVINCES = [
        ('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'),
        ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'),
        ('TG', 'Telangana'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CT', 'Chhattisgarh'),
        ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'),
        ('UT', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'),
        ('DH', 'Dadra and Nagar Haveli and Daman and Diu'), ('DL', 'Delhi'), ('JK', 'Jammu and Kashmir'),
        ('LD', 'Lakshadweep'), ('LA', 'Ladakh'), ('PY', 'Puducherry')
    ]

    unique_id = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    state = models.CharField(choices=PROVINCES, max_length=100)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    slug = models.SlugField(max_length=150)
    date_created = models.DateTimeField
    date_updated = models.DateTimeField

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.unique_id is None:
            self.unique_id = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.client_name, self.state, self.unique_id))
        self.slug = slugify('{} {} {}'.format(self.client_name, self.state, self.unique_id))
        self.date_created = timezone.localtime(timezone.now())
        self.last_updated = timezone.localtime(timezone.now())
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.client_name


class Invoice(models.Model):
    state_choices = [
        ('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('MH', 'Maharashtra'),
        ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('RJ', 'Rajasthan'), ('HP', 'Himachal Pradesh'),
        ('TG', 'Telangana'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CT', 'Chhattisgarh'),
        ('HR', 'Haryana'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OR', 'Odisha'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'),
        ('UT', 'Uttarakhand'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'),
        ('DH', 'Dadra and Nagar Haveli and Daman and Diu'), ('DL', 'Delhi'), ('JK', 'Jammu and Kashmir'),
        ('LD', 'Lakshadweep'), ('LA', 'Ladakh'), ('PY', 'Puducherry')
    ]
    invoice_id = models.CharField(max_length=200)
    client_name = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    vendor_code = models.IntegerField(null=True, blank=True)
    gstin_no = models.IntegerField(null=True, blank=True)
    pan_no = models.IntegerField(null=True, blank=True)
    cin_no = models.IntegerField(null=True, blank=True)
    iso_no = models.IntegerField(null=True, blank=True)
    reverse_charge = models.CharField(null=True, blank=True, max_length=200)
    invoice_serial_no = models.IntegerField(null=True, blank=True)
    invoice_date = models.DateField(default=date.today)
    state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    rfq_item_name = models.CharField(null=True, blank=True, max_length=200)
    name_of_goods = models.CharField(null=True, blank=True, max_length=200)
    hsn_no = models.IntegerField(null=True, blank=True)
    e_way_bill_no = models.CharField(null=True, blank=True, max_length=200)
    transportation_mode = models.CharField(null=True, blank=True, max_length=200)
    vehicle_no = models.IntegerField(null=True, blank=True)
    po_no = models.IntegerField(null=True, blank=True)
    po_date = models.IntegerField(null=True, blank=True)
    place_of_supply = models.CharField(null=True, blank=True, max_length=200)
    lr_no = models.IntegerField(null=True, blank=True)
    lr_date = models.IntegerField(null=True, blank=True)
    transporter_name = models.CharField(null=True, blank=True, max_length=200)
    dt_time_of_perparation = models.DateTimeField(default=timezone.now)
    dt_time_of_issuse = models.DateTimeField(default=timezone.now)
    details_of_reciv_bill_to = models.CharField(null=True, blank=True, max_length=200)
    name = models.CharField(null=True, blank=True, max_length=200)
    address = models.TextField(null=True, blank=True, max_length=200)
    reciv_gstin_no = models.IntegerField(null=True, blank=True)
    reciv_state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
    reciv_state_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(null=True, blank=True, max_length=200)
    details_of_consig_ship_to = models.CharField(null=True, blank=True, max_length=200)
    consig_name = models.CharField(null=True, blank=True, max_length=200)
    consig_adresss = models.TextField(max_length=255, null=True, blank=True)
    consig_gstin_no = models.IntegerField(null=True, blank=True)
    consig_state = models.CharField(choices=state_choices, max_length=255, null=True, blank=True)
    consig_state_code = models.IntegerField(null=True, blank=True)
    consig_country = models.CharField(null=True, blank=True, max_length=200)
    serial_no = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    tag_no = models.IntegerField(null=True, blank=True)
    qty_nos = models.IntegerField(null=True, blank=True)
    taxable_value_rs = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    invoice_value_in_words = models.CharField(null=True, blank=True, max_length=200)
    invoice_amt = models.IntegerField(null=True, blank=True)
    national_insur_policy_no = models.CharField(null=True, blank=True, max_length=200)
    frieght_terms = models.CharField(null=True, blank=True, max_length=200)
    basic_tot = models.IntegerField(null=True, blank=True)
    grand_tot = models.IntegerField(null=True, blank=True)
    terms_cond_for_sale = models.TextField(max_length=255, null=True, blank=True)
    electronic_refere_no = models.TextField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_no = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=150)
    date_created = models.DateTimeField
    date_updated = models.DateTimeField

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.invoice_id is None:
            self.invoice_id = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.client_name, self.state, self.invoice_id))
        self.slug = slugify('{} {} {}'.format(self.client_name, self.state, self.invoice_id))
        self.date_created = timezone.localtime(timezone.now())
        self.last_updated = timezone.localtime(timezone.now())
        super(Invoice, self).save(*args, **kwargs)
