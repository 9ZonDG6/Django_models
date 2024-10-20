from django.db import models


# Create your models here.
class User(models.Model):
    nickname = models.CharField(verbose_name='Никнейм', max_length=50)
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=30)
    email = models.EmailField(verbose_name='Эл. почта', unique=True)
    profile_photo = models.ImageField(verbose_name='Аватарка', upload_to='avatars/', blank=True, null=True)
    birth_day = models.DateField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['surname', 'first_name']

    def __str__(self):
        return f'{self.nickname}'


class Message(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Отправлено'),
        ('read', 'Прочитано'),
    ]

    message_text = models.TextField(verbose_name='Сообщение')
    author = models.ForeignKey(
        User,
        verbose_name='Автор сообщения',
        related_name='author_messages',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        verbose_name='Получатель сообщения',
        related_name='recipient_messages',
        on_delete=models.CASCADE
    )
    dispatch_date = models.DateTimeField(verbose_name='Дата отправки', auto_now_add=True)
    status = models.CharField(verbose_name='Статус сообщения', max_length=10, choices=STATUS_CHOICES, default='sent')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['dispatch_date']

    def __str__(self):
        return f'Сообщение {self.author} -> {self.recipient}'


class Post(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор поста',
        related_name='posts',
        on_delete=models.CASCADE
    )
    post_subject = models.CharField(verbose_name='Тема поста', max_length=100)
    post_text = models.TextField(verbose_name='Текст поста')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return f'Пост: {self.post_subject}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name='Пост',
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        related_name='comments',
        on_delete=models.CASCADE
    )
    comment_text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']

    def __str__(self):
        return f'Комментарий {self.author} к {self.post}'


class Friendship(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('accepted', 'Принято'),
        ('declined', 'Отклонено'),
    ]

    sender = models.ForeignKey(
        User,
        verbose_name='Отправитель заявки на дружбу',
        related_name='friendship_sent',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        verbose_name='Получатель заявки на дружбу',
        related_name='friendship_recipient',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(verbose_name='Дата запроса дружбы', auto_now_add=True)

    class Meta:
        verbose_name = 'Дружба'
        verbose_name_plural = 'Дружбы'
        constraints = [
            models.UniqueConstraint(fields=['sender', 'recipient'], name='unique_friendship')
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f'Дружба: {self.sender} -> {self.recipient} ({self.status})'
