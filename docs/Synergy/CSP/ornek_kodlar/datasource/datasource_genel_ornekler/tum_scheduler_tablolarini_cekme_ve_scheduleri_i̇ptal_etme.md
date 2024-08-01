# Tüm Scheduler Tablolarını Çekme ve Scheduler'ı İptal Etme

```
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_BLOB_TRIGGERS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_CRON_TRIGGERS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_FIRED_TRIGGERS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_JOB_DETAILS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_LOCKS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_PAUSED_TRIGGER_GRPS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_SCHEDULER_STATE
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_SIMPLE_TRIGGERS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_SIMPROP_TRIGGERS
SELECT * FROM [dbo].SchedulerTestProject_QRTZ_TRIGGERS
```

Proje adı bilgileri değiştirilerek kullanılabilir, proje üzerinde bulunan tüm Scheduler verileri görüntülenebilir. Bir proje üzerindeki Scheduler'ı iptal etmek için bu tablolara **DELETE** sorgusu atılır. Örnek:

```
DELETE FROM [dbo].SchedulerTestProject_QRTZ_TRIGGERS
```

