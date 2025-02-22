# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Analysis(models.Model):
    analysisid = models.AutoField(db_column='AnalysisId', primary_key=True)  # Field name made lowercase.
    analysisdate = models.DateField(db_column='AnalysisDate', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stateid = models.ForeignKey('Analysisstate', models.DO_NOTHING, db_column='StateId', blank=True, null=True)  # Field name made lowercase.
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='SampleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Analysis'


class Analysisstate(models.Model):
    stateid = models.AutoField(db_column='StateID', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnalysisState'


class Assignment(models.Model):
    assignmentid = models.AutoField(db_column='AssignmentId', primary_key=True)  # Field name made lowercase.
    assignmentdate = models.DateField(db_column='AssignmentDate', blank=True, null=True)  # Field name made lowercase.
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='SampleId', blank=True, null=True)  # Field name made lowercase.
    analystid = models.ForeignKey('Users', models.DO_NOTHING, db_column='AnalystId', blank=True, null=True)  # Field name made lowercase.
    managerid = models.ForeignKey('Users', models.DO_NOTHING, db_column='ManagerId', related_name='assignment_managerid_set', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Assignment'


class Bulletin(models.Model):
    bulletinid = models.AutoField(db_column='BulletinId', primary_key=True)  # Field name made lowercase.
    issuancedate = models.DateField(db_column='IssuanceDate', blank=True, null=True)  # Field name made lowercase.
    isprivate = models.BooleanField(db_column='IsPrivate', blank=True, null=True)  # Field name made lowercase.
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='SampleId', blank=True, null=True)  # Field name made lowercase.
    employeeid = models.ForeignKey('Users', models.DO_NOTHING, db_column='EmployeeId', blank=True, null=True)  # Field name made lowercase.
    content = models.BinaryField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bulletin'


class Categorysample(models.Model):
    categoryid = models.OneToOneField('Categorys', models.DO_NOTHING, db_column='CategoryId', primary_key=True)  # Field name made lowercase. The composite primary key (CategoryId, SampleId) found, that is not supported. The first column is selected.
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='SampleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategorySample'
        unique_together = (('categoryid', 'sampleid'),)


class Categorys(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categorys'


class Documentation(models.Model):
    documentid = models.AutoField(db_column='DocumentId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    publicationdate = models.DateField(db_column='PublicationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Documentation'


class Employeerole(models.Model):
    roleid = models.OneToOneField('Roles', models.DO_NOTHING, db_column='RoleId', primary_key=True)  # Field name made lowercase. The composite primary key (RoleId, EmployeeId) found, that is not supported. The first column is selected.
    employeeid = models.ForeignKey('Users', models.DO_NOTHING, db_column='EmployeeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeeRole'
        unique_together = (('roleid', 'employeeid'),)


class Files(models.Model):
    fileid = models.AutoField(db_column='FileId', primary_key=True)  # Field name made lowercase.
    certificadoregistromercantil = models.BooleanField(db_column='CertificadoRegistroMercantil', blank=True, null=True)  # Field name made lowercase.
    poderrepresentacion = models.BooleanField(db_column='PoderRepresentacion', blank=True, null=True)  # Field name made lowercase.
    certificadomarca = models.BooleanField(db_column='CertificadoMarca', blank=True, null=True)  # Field name made lowercase.
    permisosanitario = models.BooleanField(db_column='PermisoSanitario', blank=True, null=True)  # Field name made lowercase.
    contratofabricacion = models.BooleanField(db_column='ContratoFabricacion', blank=True, null=True)  # Field name made lowercase.
    contratoacondicionamiento = models.BooleanField(db_column='ContratoAcondicionamiento', blank=True, null=True)  # Field name made lowercase.
    listadoingredientes = models.BooleanField(db_column='ListadoIngredientes', blank=True, null=True)  # Field name made lowercase.
    analisisoriginalproducto = models.BooleanField(db_column='AnalisisOriginalProducto', blank=True, null=True)  # Field name made lowercase.
    analisisoriginalmateriales = models.BooleanField(db_column='AnalisisOriginalMateriales', blank=True, null=True)  # Field name made lowercase.
    estudioestabilidad = models.BooleanField(db_column='EstudioEstabilidad', blank=True, null=True)  # Field name made lowercase.
    especificacionempaque = models.BooleanField(db_column='EspecificacionEmpaque', blank=True, null=True)  # Field name made lowercase.
    diagramaflujo = models.BooleanField(db_column='DiagramaFlujo', blank=True, null=True)  # Field name made lowercase.
    arteetiqueta = models.BooleanField(db_column='ArteEtiqueta', blank=True, null=True)  # Field name made lowercase.
    recibopagoservicios = models.BooleanField(db_column='ReciboPagoServicios', blank=True, null=True)  # Field name made lowercase.
    sampleid = models.ForeignKey('Samples', models.DO_NOTHING, db_column='SampleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Files'


class Info(models.Model):
    infoid = models.AutoField(db_column='InfoId', primary_key=True)  # Field name made lowercase.
    rnc = models.CharField(db_column='RNC', max_length=20, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Info'


class Resultstatehistory(models.Model):
    historyid = models.AutoField(db_column='HistoryId', primary_key=True)  # Field name made lowercase.
    statechangedate = models.DateField(db_column='StateChangeDate', blank=True, null=True)  # Field name made lowercase.
    correctiondescription = models.TextField(db_column='CorrectionDescription', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    requestchangedate = models.DateField(db_column='RequestChangeDate', blank=True, null=True)  # Field name made lowercase.
    analysisid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='AnalysisId', blank=True, null=True)  # Field name made lowercase.
    newstateid = models.ForeignKey(Analysisstate, models.DO_NOTHING, db_column='NewStateId', blank=True, null=True)  # Field name made lowercase.
    previousstateid = models.ForeignKey(Analysisstate, models.DO_NOTHING, db_column='PreviousStateId', related_name='resultstatehistory_previousstateid_set', blank=True, null=True)  # Field name made lowercase.
    changedby = models.ForeignKey('Users', models.DO_NOTHING, db_column='ChangedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultStateHistory'


class Roles(models.Model):
    roleid = models.AutoField(db_column='RoleId', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    roledescription = models.TextField(db_column='RoleDescription', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Samples(models.Model):
    sampleid = models.AutoField(db_column='SampleId', primary_key=True)  # Field name made lowercase.
    comercialname = models.CharField(db_column='ComercialName', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    productbrand = models.CharField(db_column='ProductBrand', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    batchcode = models.CharField(db_column='BatchCode', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    productiondate = models.DateField(db_column='ProductionDate', blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    quantityunits = models.IntegerField(db_column='QuantityUnits', blank=True, null=True)  # Field name made lowercase.
    isrejected = models.BooleanField(db_column='IsRejected', blank=True, null=True)  # Field name made lowercase.
    origincountry = models.CharField(db_column='OriginCountry', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    collectiondate = models.DateField(db_column='CollectionDate', blank=True, null=True)  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    specialconditions = models.TextField(db_column='SpecialConditions', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    isrequest = models.BooleanField(db_column='IsRequest')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Samples'


class Subcategorysample(models.Model):
    subcategoryid = models.OneToOneField('Subcategorys', models.DO_NOTHING, db_column='SubcategoryId', primary_key=True)  # Field name made lowercase. The composite primary key (SubcategoryId, SampleId) found, that is not supported. The first column is selected.
    sampleid = models.ForeignKey(Samples, models.DO_NOTHING, db_column='SampleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubcategorySample'
        unique_together = (('subcategoryid', 'sampleid'),)


class Subcategorys(models.Model):
    subcategoryid = models.AutoField(db_column='SubcategoryId', primary_key=True)  # Field name made lowercase.
    subcategoryname = models.CharField(db_column='SubcategoryName', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subcategorys'


class Users(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    cedula = models.CharField(db_column='Cedula', max_length=11, db_collation='Modern_Spanish_CI_AS')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=12, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    rnc = models.CharField(db_column='RNC', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comercialcompanyname = models.CharField(db_column='ComercialCompanyName', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=255, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ismaster = models.BooleanField(db_column='IsMaster', blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Users'


class UsersGroups(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Users_groups'


class UsersUserPermissions(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Users_user_permissions'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
