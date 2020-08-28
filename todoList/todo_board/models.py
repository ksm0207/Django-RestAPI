from django.db import models


class ProjectCode(models.Model):
    pcode = models.CharField(db_column="PCODE", primary_key=True, max_length=4)
    pname = models.CharField(db_column="PNAME", max_length=100)

    class Meta:
        managed = False
        db_table = "project_code"


class TodoList(models.Model):
    no = models.AutoField(db_column="NO", primary_key=True)
    pcode = models.CharField(db_column="PCODE", max_length=4)
    user_id = models.CharField(
        db_column="USER_ID", max_length=50, blank=True, null=True
    )
    title = models.CharField(db_column="TITLE", max_length=200, blank=True, null=True)
    content = models.CharField(
        db_column="CONTENT", max_length=1000, blank=True, null=True
    )
    is_complete = models.IntegerField(db_column="IS_COMPLETE", blank=True, null=True)
    priority = models.IntegerField(db_column="PRIORITY", blank=True, null=True)
    end_date = models.DateField(db_column="END_DATE", blank=True, null=True)
    test = models.BooleanField()

    class Meta:
        managed = False
        db_table = "todo_list"

