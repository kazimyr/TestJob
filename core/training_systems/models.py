from datetime import date
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=40, unique=True)
    date_start = models.DateTimeField(null=True, blank=True)
    min_users = models.SmallIntegerField(default=1)
    max_users = models.SmallIntegerField(default=1)
    
    
    def __str__(self):
        return f'Курс: {self.name} | Автор: {self.author}'


class Lesson(models.Model):
    name = models.CharField(max_length=128)
    video_link = models.URLField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return f'Урок: {self.name} | Курс: {self.product.name}'


class Group(models.Model):
    name = models.CharField(max_length=20)
    users_quantity = models.SmallIntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    # members = models.ManyToManyField(Users, db_table=tbl_group_MM_users)

    # def __init__(self, course, number):
    #     self.product = Product.objects.get(name = course)
    #     self.name = f'{Course} number'
    
    def __str__(self):
        return self.name

    # @classmethod
    # def add_group(cls, id_product):
    #     group_quantity = Group.objects.filter(product = id_product).count() + 1
    #     cls(Product.objects.filter(pk = id_product).name, group_quantity)
    
    @classmethod
    def add_user(cls, id_product):
        pr = Product.objects.get(pk = id_product)
        group_quantity = Group.objects.filter(product = pr).count()
        if group_quantity:
            gr = Group.objects.filter(product = pr).last()
            q = gr.users_quantity
            if gr.product.max_users > q:
                gr.users_quantity += 1
                gr.save()
            else:
                gr = Group(name=f'{pr.name} {group_quantity + 1}', product=pr)
                gr.save()
        else:
            gr = gr = Group(name=f'{pr.name} 1', product=pr)
            gr.save()
        return gr.name

    @classmethod
    def resort_users(cls):
        for pr in Product.objects.all():
            if pr.date_start.date() > date.today():
                mn = pr.min_users
                groups = Group.objects.filter(product = pr)
                gr_quantity = len(groups)
                if gr_quantity > 1:
                    user_qty = 0
                    for gr in groups:
                        user_qty += gr.users_quantity
                    body = (user_qty - mn * gr_quantity) // gr_quantity
                    tail = (user_qty - mn * gr_quantity) % gr_quantity
                    for gr in groups:
                        gr.users_quantity = mn + body
                        gr.save()
                        if tail:
                            gr.users_quantity += 1
                            gr.save()
                            tail -=1
        return

    


# class Users(models.Model):
#     fname = models.CharField(max_length=20)
#     lname = models.CharField(max_length=20)

