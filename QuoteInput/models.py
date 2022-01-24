from django.db import models

# Create your models here.

CBD_LEAD_NAMES = (
    ("Arlene Branham", "Arlene Branham"),
    ('John Smith', 'John Smith'),
    ("Sharron Harman", "Sharron Harman"),
    ('Harry Anderson', 'Harry Anderson'),
)

TERM_TYPE = (
    ("Cloud Subscription", "Cloud Subscription"),
    ("Cloud Perpetual", "Cloud Perpetual"),
    ("SaaS", "SaaS"),
)

PROD_NAME = (
    ('OpenText ContentSuite', 'OpenText ContentSuite'),
    ('OpenText Experience Suite', 'OpenText Experience Suite'),
    ('OpenText Process Suite', 'OpenText Process Suite'),
    ('OpenText Information Exchange Suite', 'OpenText Information Exchange Suite'),
    ('OpenText Discovery Suite', 'OpenText Discovery Suite'),
    ('OpenText Suite for SAP', 'OpenText Suite for SAP'),
    ('OpenText Suite for Oracle', 'OpenText Suite for Oracle'),
    ('OpenText Suite for Microsoft', 'OpenText Suite for Microsoft'),
    ('OpenText Appworks', 'OpenText Appworks'),
    ('OpenText Cloud', 'OpenText Cloud'),
)

BOOL_VAL = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

CDS_REP = (
    ('M1', 'CDS Rep 1'),
    ('M2', 'CDS Rep 2'),
    ('M3', 'CDS Rep 3'),
    ('M4', 'CDS Rep 4'),
    ('M5', 'CDS Rep 5')
)

CURRENCY_TABLE = (
    ('USD', 'USD'),
    ('AED', 'AED'),
    ('AFN', 'AFN'),
    ('ALL', 'ALL'),
    ('AMD', 'AMD'),
    ('ANG', 'ANG'),
    ('AOA', 'AOA'),
    ('ARS', 'ARS'),
    ('AUD', 'AUD'),
    ('AZN', 'AZN'),
    ('BAM', 'BAM'),
    ('BBD', 'BBD'),
    ('BDT', 'BDT'),
    ('BGN', 'BGN'),
    ('BHD', 'BHD'),
    ('BIF', 'BIF'),
    ('BMD', 'BMD'),
    ('BND', 'BND'),
    ('BOB', 'BOB'),
    ('BRL', 'BRL'),
    ('BSD', 'BSD'),
    ('BTN', 'BTN'),
    ('BWP', 'BWP'),
    ('BZD', 'BZD'),
    ('CAD', 'CAD'),
    ('CDF', 'CDF'),
    ('CHF', 'CHF'),
    ('CLP', 'CLP'),
    ('CNH', 'CNH'),
    ('CNY', 'CNY'),
    ('COP', 'COP'),
    ('CRC', 'CRC'),
    ('CVE', 'CVE'),
    ('CYP', 'CYP'),
    ('CZK', 'CZK'),
    ('DJF', 'DJF'),
    ('DKK', 'DKK'),
    ('DOP', 'DOP'),
    ('DZD', 'DZD'),
    ('EEK', 'EEK'),
    ('EGP', 'EGP'),
    ('ETB', 'ETB'),
    ('EUR', 'EUR'),
    ('FJD', 'FJD'),
    ('GBP', 'GBP'),
    ('GEL', 'GEL'),
    ('GHS', 'GHS'),
    ('GIP', 'GIP'),
    ('GMD', 'GMD'),
    ('GNF', 'GNF'),
    ('GTQ', 'GTQ'),
    ('GYD', 'GYD'),
    ('HKD', 'HKD'),
    ('HNL', 'HNL'),
    ('HRK', 'HRK'),
    ('HTG', 'HTG'),
    ('HUF', 'HUF'),
    ('IDR', 'IDR'),
    ('ILS', 'ILS'),
    ('INR', 'INR'),
    ('IRR', 'IRR'),
    ('ISK', 'ISK'),
    ('JMD', 'JMD'),
    ('JOD', 'JOD'),
    ('JPY', 'JPY'),
    ('KES', 'KES'),
    ('KGS', 'KGS'),
    ('KHR', 'KHR'),
    ('KMF', 'KMF'),
    ('KRW', 'KRW'),
    ('KWD', 'KWD'),
    ('KYD', 'KYD'),
    ('KZT', 'KZT'),
    ('LAK', 'LAK'),
    ('LBP', 'LBP'),
    ('LKR', 'LKR'),
    ('LSL', 'LSL'),
    ('LTL', 'LTL'),
    ('LVL', 'LVL'),
    ('MAD', 'MAD'),
    ('MDL', 'MDL'),
    ('MGA', 'MGA'),
    ('MKD', 'MKD'),
    ('MMK', 'MMK'),
    ('MNT', 'MNT'),
    ('MOP', 'MOP'),
    ('MRO', 'MRO'),
    ('MTL', 'MTL'),
    ('MUR', 'MUR'),
    ('MVR', 'MVR'),
    ('MWK', 'MWK'),
    ('MXN', 'MXN'),
    ('MYR', 'MYR'),
    ('MZN', 'MZN'),
    ('NAD', 'NAD'),
    ('NGN', 'NGN'),
    ('NIO', 'NIO'),
    ('NOK', 'NOK'),
    ('NPR', 'NPR'),
    ('NZD', 'NZD'),
    ('OMR', 'OMR'),
    ('PAB', 'PAB'),
    ('PEN', 'PEN'),
    ('PGK', 'PGK'),
    ('PHP', 'PHP'),
    ('PKR', 'PKR'),
    ('PLN', 'PLN'),
    ('PYG', 'PYG'),
    ('QAR', 'QAR'),
    ('RON', 'RON'),
    ('RSD', 'RSD'),
    ('RUB', 'RUB'),
    ('RWF', 'RWF'),
    ('SAR', 'SAR'),
    ('SBD', 'SBD'),
    ('SCR', 'SCR'),
    ('SDG', 'SDG'),
    ('SEK', 'SEK'),
    ('SGD', 'SGD'),
    ('SIT', 'SIT'),
    ('SKK', 'SKK'),
    ('SLL', 'SLL'),
    ('SRD', 'SRD'),
    ('STD', 'STD'),
    ('SVC', 'SVC'),
    ('SYP', 'SYP'),
    ('SZL', 'SZL'),
    ('THB', 'THB'),
    ('TJS', 'TJS'),
    ('TND', 'TND'),
    ('TOP', 'TOP'),
    ('TRY', 'TRY'),
    ('TTD', 'TTD'),
    ('TWD', 'TWD'),
    ('TZS', 'TZS'),
    ('UAH', 'UAH'),
    ('UGX', 'UGX'),
    ('UYU', 'UYU'),
    ('UZS', 'UZS'),
    ('VEF', 'VEF'),
    ('VND', 'VND'),
    ('VUV', 'VUV'),
    ('WST', 'WST'),
    ('XAF', 'XAF'),
    ('XCD', 'XCD'),
    ('XOF', 'XOF'),
    ('XPF', 'XPF'),
    ('YER', 'YER'),
    ('ZAR', 'ZAR'),
    ('ZMW', 'ZMW'),
)

CLOUD_HOSTING = (
    ('OpenText', 'OpenText'),
    ('OpenText Australia', 'OpenText Australia'),
    ('OpenText Canada', 'OpenText Canada'),
    ('GCP', 'GCP'),
    ('Azure', 'Azure'),
    ('AWS', 'AWS'),
    ('Customer', 'Customer'),
)

Blank = '--------------'
OpenText_1 = 'OT - US Twins'
OpenText_2 = 'OT - EMEA Twins'
OpenText_3 = 'OT - Japan Twins'
OpenText_AUSTRALIA = 'OT - Sydney'
OpenText_CANADA = 'OT - Toronto'
GCP_1 = 'GCP - US'
GCP_2 = 'GCP - NA-NE'
GCP_3 = 'GCP - Europe'
GCP_4 = 'GCP - Australia'
GCP_5 = 'GCP - Asia'
GCP_6 = 'GCP - Asia-East'
GCP_7 = 'GCP - Asia-NE'
GCP_8 = 'GCP - Brazil'
AZURE_1 = 'Central US'
AZURE_2 = 'East US'
AZURE_3 = 'East US 2'
AZURE_4 = 'North Central US'
AZURE_5 = 'South Central US'
AZURE_6 = 'West Central US'
AZURE_7 = 'West US'
AZURE_8 = 'West US 2'
AZURE_9 = 'North Europe'
AZURE_10 = 'West Europe'
AZURE_11 = 'East Asia'
AWS_1 = 'US East (N.Virginia)'
AWS_2 = 'US East (Ohio)'
AWS_3 = 'US West (Oregon)'
AWS_4 = 'US West (N. Calif.)'
AWS_5 = 'Africa (Cape Town)'
AWS_6 = 'Asia Pacific (Hong Kong)'
AWS_7 = 'Asia Pacific (Mumbai)'
AWS_8 = 'Asia Pacific (Osaka-Local)'
AWS_9 = 'Asia Pacific (Seoul)'
AWS_10 = 'Asia Pacific (Singapore)'
AWS_11 = 'Asia Pacific (Sydney)'
AWS_12 = 'Asia Pacific (Tokyo)'
AWS_13 = 'Canada (Central)'
AWS_14 = 'Europe (Frankfurt)'
AWS_15 = 'Europe (Ireland)'
AWS_16 = 'Europe (London)'
AWS_17 = 'Europe (Milan)'
AWS_18 = 'Europe (Paris)'
AWS_19 = 'Europe (Stockholm)'
AWS_20 = 'Middle East (Bahrain)'
AWS_21 = 'South America (Sao Paulo)'
AWS_22 = 'AWS GovCloud (US-East)'
AWS_23 = 'AWS GovCloud (US-West)'
Customer_1 = 'Customer DC'
RTO_RPO_1 = 'RTO 7days / RPO 24hrs'
RTO_RPO_2 = 'RTO 8hrs / RPO 8hrs'
RTO_RPO_3 = 'RTO 4hrs / RPO 4hrs'

LOCATION = (
    (Blank, Blank),
    (OpenText_1, OpenText_1),
    (OpenText_2, OpenText_2),
    (OpenText_3, OpenText_3),
    (OpenText_AUSTRALIA, OpenText_AUSTRALIA),
    (OpenText_CANADA, OpenText_CANADA),
    (GCP_1, GCP_1),
    (GCP_2, GCP_2),
    (GCP_3, GCP_3),
    (GCP_4, GCP_4),
    (GCP_5, GCP_5),
    (GCP_6, GCP_6),
    (GCP_7, GCP_7),
    (GCP_8, GCP_8),
    (AZURE_1, AZURE_1),
    (AZURE_2, AZURE_2),
    (AZURE_3, AZURE_3),
    (AZURE_4, AZURE_4),
    (AZURE_5, AZURE_5),
    (AZURE_6, AZURE_6),
    (AZURE_7, AZURE_7),
    (AZURE_8, AZURE_8),
    (AZURE_9, AZURE_9),
    (AZURE_10, AZURE_10),
    (AZURE_11, AZURE_11),
    (AWS_1, AWS_1),
    (AWS_2, AWS_2),
    (AWS_3, AWS_3),
    (AWS_4, AWS_4),
    (AWS_5, AWS_5),
    (AWS_6, AWS_6),
    (AWS_7, AWS_7),
    (AWS_8, AWS_8),
    (AWS_9, AWS_9),
    (AWS_10, AWS_10),
    (AWS_11, AWS_11),
    (AWS_12, AWS_12),
    (AWS_13, AWS_13),
    (AWS_14, AWS_14),
    (AWS_15, AWS_15),
    (AWS_16, AWS_16),
    (AWS_17, AWS_17),
    (AWS_18, AWS_18),
    (AWS_19, AWS_19),
    (AWS_20, AWS_20),
    (AWS_21, AWS_21),
    (AWS_22, AWS_22),
    (AWS_23, AWS_23),
    (Customer_1, Customer_1),
)

Yes = 'Yes'
No = 'No'

Zero = 0
One = 1

BOOL = (
    (Yes, Yes), (No, No),
)

SLA_PERCENTAGE = (
    (99, 99), (99.50, 99.50), (99.90, 99.90)
)

DR_SLA = (
    (RTO_RPO_1, RTO_RPO_1),
    (RTO_RPO_2, RTO_RPO_2),
    (RTO_RPO_3, RTO_RPO_3),
)

DR_HRS1 = 16.67

DR_HRS = (
    (Blank, Blank),
    (DR_HRS1, DR_HRS1)
)

ZERO_ONE = (
    (Zero, Zero),
    (One, One),
)

OT_Standard = 'OT - Standard'
OT_EDR_via_Twin_DCs = 'OT - EDR via Twin DCs'
OT_DC_with_GCP_for_EDR = 'OT DC with GCP for EDR'
GCP_Single_region_Multi_Zone_DR = 'GCP Single-region Multi-Zone DR'
GCP_Multi_region_EDR_geographic_separation = 'GCP Multi-region EDR (geographic separation)'
Azure_Single_region_Multi_Zone_DR = 'Azure Single-region Multi-Zone DR'
Azure_Multi_region_EDR_geographic_separation = 'Azure Multi-region EDR (geographic separation)'
AWS_Single_region_Multi_Zone_DR = 'AWS Single-region Multi-Zone DR'
AWS_Multi_region_EDR_geographic_separation = 'AWS Multi-region EDR (geographic separation)'

DR_OPTIONS = (
    (Blank, Blank),
    (OT_Standard, OT_Standard),
    (OT_EDR_via_Twin_DCs, OT_EDR_via_Twin_DCs),
    (OT_DC_with_GCP_for_EDR, OT_DC_with_GCP_for_EDR),
    (GCP_Single_region_Multi_Zone_DR, GCP_Single_region_Multi_Zone_DR),
    (GCP_Multi_region_EDR_geographic_separation, GCP_Multi_region_EDR_geographic_separation),
    (Azure_Single_region_Multi_Zone_DR, Azure_Single_region_Multi_Zone_DR),
    (Azure_Multi_region_EDR_geographic_separation, Azure_Multi_region_EDR_geographic_separation),
    (AWS_Single_region_Multi_Zone_DR, AWS_Single_region_Multi_Zone_DR),
    (AWS_Multi_region_EDR_geographic_separation, AWS_Multi_region_EDR_geographic_separation),
)

FULL_PARTIAL = (
    ('Full', 'Full'),
    ('Partial', 'Partial'),
)

RESPONSE_TIME = (
    ('24x7', '24x7'),
    ('10x5', '10x5'),
)

FIREWALL = (
    ('Multiple Access Points', 'Multiple Access Points'),
    ('Single Access Point', 'Single Access Point'),
)

# 1. Inputs


class CloudDeskSpecialistModel(models.Model):
    name = models.CharField(max_length=54)

    def __str__(self):
        return self.name


class LocalCurrencyModel(models.Model):
    name = models.CharField(max_length=5)
    exchangeRate = models.FloatField(max_length=156, null=True, blank=False)

    def __str__(self):
        return f"{self.name}: {self.exchangeRate}"


# 2. Hosting


class HostingProviderModel(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class LocationModel(models.Model):
    hostingProvider = models.ForeignKey(HostingProviderModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class QuoteInputModel(models.Model):
    # Inputs

    hostingProvider = models.ForeignKey(HostingProviderModel, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(LocationModel, on_delete=models.SET_NULL, null=True)

    quoteName = models.CharField(max_length=56, null=True)
    salesForceCloudOpportunityID = models.CharField(max_length=120)
    customerName = models.CharField(max_length=120, null=True)
    cloudOpportunityURL = models.URLField(max_length=200, help_text='copy and paste SFDC Opportunity URL', null=True,
                                          blank=True)
    cloudDeskSpecialist = models.ForeignKey(CloudDeskSpecialistModel, on_delete=models.SET_NULL, null=True, blank=False)
    cloudOpportunityType = models.CharField(max_length=56, choices=TERM_TYPE, null=True)
    leadingProduct = models.CharField(max_length=120, choices=PROD_NAME, null=True)
    nonStandardTermsOrPenalties = models.CharField(max_length=10, choices=BOOL_VAL, null=True, blank=True)
    hasTheEnterpriseCloudManagedServicesBeenExcludedByaCDSRep = models.CharField(max_length=56, choices=BOOL_VAL,
                                                                                 null=True)
    managedServicesRep = models.CharField(max_length=56, choices=CDS_REP, null=True)

    localCurrency = models.ForeignKey(LocalCurrencyModel, on_delete=models.SET_NULL, null=True, blank=False)
    requireTimelineBasedChanges = models.CharField(max_length=10, choices=BOOL_VAL, null=True)
    inRegionNAEMEAPersonnelOnly = models.CharField(max_length=10, choices=BOOL_VAL, null=True)
    changeRequestOrAddOnOnly = models.CharField(max_length=10, choices=BOOL_VAL, null=True)
    ifCRAddOnGCPAlreadyProvisionedNetAppCVO = models.CharField(max_length=10, choices=BOOL_VAL, null=True)
    cloudTermMonths = models.IntegerField(default=36)
    subscriptionSoftwareOTDirectDiscount = models.FloatField(default=85)  # change to floats - 7 decimals
    subscriptionSoftwareThirdPartyDiscount = models.FloatField(default=30)  # change to floats - 7 decimals
    perpetualSoftwareOTDirectDiscount = models.FloatField(default=10)  # change to floats - 7 decimals
    perpetualSoftwareThirdPartyDiscount = models.FloatField(default=5)  # change to floats - 7 decimals
    CPSCostRateUSDhr = models.FloatField(default=80.00)
    CDMCostRateUSDhr = models.FloatField(default=80.00)
    DRPlanningLaborCostRateUSDhr = models.FloatField(default=100.00)
    cloudMargin = models.FloatField(default=47.00)
    annualPriceAdjustment = models.FloatField(default=3.00)
    incrementalECMSHeadcountRequiredAsPartOfTheECMS = models.CharField(max_length=10, choices=BOOL_VAL, null=True)
    CPSMonthlyHours = models.PositiveIntegerField(help_text='30hrs is the minimum, approvals required for less', null=True)
    CDSMonthlyHours = models.PositiveIntegerField(help_text='15hrs is the minimum, approvals required for less', null=True)
    manualInstallationCost = models.FloatField(max_length=28, help_text='If populated, this overrides the automation '
                                                                        'of installation costs within the VM tab. Use'
                                                                        ' for Daas', null=True)
    endOfFirstYearUsersOfTotal = models.FloatField(max_length=10, null=True)
    annualUsersIncreaseOfTotal = models.FloatField(max_length=10, null=True)
    totalUsersOverTerm = models.IntegerField(null=True)
    removeAmortized10kUSDFee100Margin = models.CharField(max_length=5, choices=BOOL_VAL, null=True)

    # Hosting

    multipleActiveRegions = models.CharField(max_length=5, choices=BOOL, default='No')
    customerRequestedPrimaryDC = models.CharField(max_length=56, null=True)
    customerRequestedSecondaryOrMoreDCs = models.CharField(max_length=56, null=True)
    explanationOfMultipleActiveRegions = models.CharField(max_length=56, null=True)
    customerRequestedApplicationAvailabilitySLA = models.FloatField(max_length=10, choices=SLA_PERCENTAGE, null=True)
    disasterRecovery = models.CharField(max_length=56, choices=DR_OPTIONS, null=True)
    customerRequestedRTORPOSLA = models.CharField(max_length=56, choices=DR_SLA, null=True)
    enhancedDRPlanningHrsPcm = models.FloatField(max_length=50, choices=DR_HRS, null=True)
    isThisADaaSBasedCloudService = models.CharField(max_length=10, choices=BOOL, null=True)
    requiresEUDataProtectionZoneEUDPZ = models.CharField(max_length=10, choices=BOOL, null=True)
    backupNonProductionEnvironments = models.CharField(max_length=10, choices=BOOL, null=True)
    encryptionAtRest = models.CharField(max_length=10, choices=BOOL, null=True)
    numberOfSiteToSiteVPNs = models.CharField(max_length=5, choices=ZERO_ONE, null=True)
    numberOfClientBasedVPNs = models.IntegerField(null=True)
    willTheCustomerUseMPLSVPLSCircuitsToConnect = models.CharField(max_length=10, choices=BOOL, null=True)
    GCPSoleTenantNodesVCPUs96RAM624GBPerSTN = models.IntegerField(null=True)
    additionalCloudDeliveryOpsCostsPcmUSD = models.FloatField(max_length=13, null=True)
    additionalCloudDeliveryOpsCostsOneTimeUSD = models.FloatField(max_length=13, null=True)
    thirdPartyAzureRemoteAccess = models.CharField(max_length=10, choices=BOOL, null=True)
    OSPatching = models.CharField(max_length=10, choices=FULL_PARTIAL, null=True)
    threatManagementAndSecurityScans = models.CharField(max_length=10, choices=BOOL, null=True)
    problemEscalationAndResponse = models.CharField(max_length=10, choices=RESPONSE_TIME, null=True)
    loadBalancing = models.CharField(max_length=10, choices=BOOL, null=True)
    firewall = models.CharField(max_length=50, choices=FIREWALL, null=True)
    databaseAdministrationAndTuning = models.CharField(max_length=10, choices=BOOL, null=True)
    activeActiveDBRequired = models.CharField(max_length=10, choices=BOOL, null=True)
    applicationMonitoringRequiredNewRelic = models.CharField(max_length=10, choices=BOOL, null=True)

    def __str__(self):
        return f"{self.quoteName}: {self.customerName}: {self.quoteName}"

    def get_testCostCalculation(self):
        return self.cloudTermMonths * self.cloudMargin


# HOSTING ##################### HOSTING ####################### HOSTING ########## HOSTING ###################

def get_ot_strings():
    ot_strings = [
        Blank, OpenText_1, OpenText_2, OpenText_3,
    ]
    return ot_strings


def get_au_strings():
    au_strings = [
        Blank, OpenText_AUSTRALIA
    ]
    return au_strings


def get_ca_strings():
    ca_strings = [
        Blank, OpenText_CANADA
    ]
    return ca_strings


def get_gcp_strings():
    gcp_strings = [
        Blank, GCP_1, GCP_2, GCP_3, GCP_4, GCP_5, GCP_6, GCP_7, GCP_8
    ]
    return gcp_strings


def get_az_strings():
    az_strings = [
        Blank, AZURE_1, AZURE_2, AZURE_3, AZURE_4, AZURE_5, AZURE_6, AZURE_7, AZURE_8, AZURE_9, AZURE_10, AZURE_11
    ]
    return az_strings


def get_aw_strings():
    aw_strings = [
        Blank, AWS_1, AWS_2, AWS_3, AWS_4, AWS_5, AWS_6, AWS_7, AWS_8, AWS_9, AWS_10, AWS_11,
        AWS_12, AWS_13, AWS_14, AWS_15, AWS_16, AWS_17, AWS_18, AWS_19, AWS_20, AWS_21, AWS_22, AWS_23
    ]
    return aw_strings


def get_cu_strings():
    cu_strings = [
        Customer_1
    ]
    return cu_strings


def get_multi_strings():
    multi_strings = [
        Blank, Yes, No
    ]
    return multi_strings


def get_usemea_strings():
    usemea_strings = [
        Blank, OT_Standard, OT_EDR_via_Twin_DCs, OT_DC_with_GCP_for_EDR
    ]
    return usemea_strings


def get_japan_strings():
    japan_strings = [
        Blank, OT_Standard, OT_EDR_via_Twin_DCs
    ]
    return japan_strings


def get_sydney_strings():
    sydney_strings = [
        Blank, OT_Standard, OT_EDR_via_Twin_DCs
    ]
    return sydney_strings


def get_canada_strings():
    canada_strings = [
        Blank, OT_Standard
    ]
    return canada_strings


# _______ GCP ___________ #


def get_gcpus_strings():
    gcpus_strings = [
        Blank, GCP_Single_region_Multi_Zone_DR, GCP_Multi_region_EDR_geographic_separation
    ]
    return gcpus_strings


def get_gcpnane_strings():
    gcpnane_strings = [
        Blank, GCP_Single_region_Multi_Zone_DR
    ]
    return gcpnane_strings


def get_gcpeurope_strings():
    gcpeurope_strings = [
        Blank, GCP_Single_region_Multi_Zone_DR, GCP_Multi_region_EDR_geographic_separation
    ]
    return gcpeurope_strings


def get_gcpaustralia_strings():
    gcpaustralia_strings = [
        Blank
    ]
    return gcpaustralia_strings


def get_gcpasia_strings():
    gcpasia_strings = [
        Blank, GCP_Single_region_Multi_Zone_DR, GCP_Multi_region_EDR_geographic_separation
    ]
    return gcpasia_strings


def get_gcpasiaeast_strings():
    gcpasiaeast_strings = [
        Blank, GCP_Single_region_Multi_Zone_DR, GCP_Multi_region_EDR_geographic_separation
    ]
    return gcpasiaeast_strings


def get_gcpasiane_strings():
    gcpasiane_strings = [
        Blank, GCP_Single_region_Multi_Zone_DR, GCP_Multi_region_EDR_geographic_separation
    ]
    return gcpasiane_strings


def get_gcpbrazil_strings():
    gcpbrazil_strings = [
        Blank, GCP_Single_region_Multi_Zone_DR, GCP_Multi_region_EDR_geographic_separation
    ]
    return gcpbrazil_strings


# ______ END OF GCP ______ #

# _________ AWS ___________ #


def get_awsall_strings():
    awsall_strings = [
        Blank, AWS_Single_region_Multi_Zone_DR, AWS_Multi_region_EDR_geographic_separation
    ]
    return awsall_strings


# _________ END OF AWS ___________ #


def get_drhrs_strings():
    drhrs_strings = [
        DR_HRS1
    ]
    return drhrs_strings


def get_drsla1_srings():
    drsla1_strings = [
        RTO_RPO_1
    ]
    return drsla1_strings


def get_drsla2_srings():
    drsla2_strings = [
        RTO_RPO_2, RTO_RPO_3
    ]
    return drsla2_strings


def get_drsla3_srings():
    drsla3_strings = [
        RTO_RPO_1, RTO_RPO_2, RTO_RPO_3
    ]
    return drsla3_strings


def get_encatrest_strings():
    encatrest_strings = [
        No
    ]
    return encatrest_strings


def get_s2svpns_strings():
    s2svpns_strings = [
        Zero
    ]
