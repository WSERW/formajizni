from django.utils.translation import gettext_lazy as _
from django.db import models


class ContactInfo(models.Model):
    phone1 = models.CharField(max_length=20, verbose_name="Телефон")
    phone2 = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.TextField(verbose_name="Адрес")
    working_hours = models.CharField(
        max_length=100, verbose_name="Часы работы")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактные информации"

    def __str__(self):
        return f"Контактная информация - {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}"


class Lead(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания")

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка от {self.name} ({self.phone})"


class FAQ(models.Model):
    question = models.CharField(max_length=255, help_text="Введите вопрос")
    answer = models.TextField(help_text="Введите ответ")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
        ordering = ['question']


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            help_text="Название категории")
    image = models.ImageField(
        upload_to='categories/', blank=True, null=True, help_text="Изображение категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Work(models.Model):
    image = models.ImageField(
        upload_to='works/', help_text="Изображение работы")
    title = models.CharField(max_length=255, help_text="Название работы")
    category = models.ForeignKey(
        Category, related_name='works', on_delete=models.CASCADE, help_text="Категория работы")
    location = models.CharField(max_length=255, help_text="Место изготовления")
    date_of_creation = models.CharField(
        max_length=255, help_text="Дата изготовления (текстом)")
    materials = models.TextField(
        help_text="Материалы (список, можно использовать пунктирный список)")
    advantages = models.TextField(
        help_text="Преимущества (список, можно использовать пунктирный список)")
    for_decoration = models.TextField(
        help_text="Для оформления (список, можно использовать пунктирный список)")
    care_and_use = models.TextField(
        help_text="Уход и эксплуатация (большой текст)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"
        ordering = ['title']
