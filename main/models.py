from django.db import models


class Catigori_woork(models.Model):
    name = models.CharField(verbose_name=("Названия катигория"), max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Катигория"
        verbose_name_plural = "Катигории"


class Sotrudnic(models.Model):
    img = models.ImageField(
        upload_to="Woor", verbose_name="Изображения сотрудника",
    )
    name = models.CharField(verbose_name="Имя", max_length=60)
    email = models.EmailField(verbose_name=("email"), max_length=254)
    jod = models.ForeignKey(
        to=Catigori_woork, on_delete=models.CASCADE, related_name="Sotrudnnic"
    )

    def __str__(self) -> str:
        return f'{self.name} -> {self.jod}'
        # return f'{self.name}->{self.img}'

    class Meta:
        verbose_name = "Сатрудник"
        verbose_name_plural = "Сатрудники"


class Task(models.Model):
    img = models.ImageField(upload_to='Woork', verbose_name="Изображения",)
    name = models.CharField(verbose_name="Названия задания",max_length=25)
    description = models.TextField(verbose_name="Описание")
    who_develops = models.ManyToManyField(to=Sotrudnic,related_name='devs')
    date_end = models.DateTimeField(
        verbose_name=("Срок до"), auto_now=False
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Зада́ние"
        verbose_name_plural = "Зада́ния"


