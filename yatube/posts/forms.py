from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        labels = {
            'text': _('Текст поста'),
            'group': _('Группа')
        }
        help_texts = {
            'text': _('Напишите что-нибудь здесь!'),
            'group': _('Группа в которой будет пост'),
            'image': _('Добавьте картинку')
        }
        error_messages = {
            'text': {
                'required_field': _('Это обязательное поле!')
            }
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'text',
        )
        labels = {
            'text': _('Текст комментария'),
        }
