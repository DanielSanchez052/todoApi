from django.dispatch import receiver
from django.db.models.signals import post_save
from api.to_do.models import Task

@receiver(post_save, sender=Task)
def send_action_ws(sender,instance,created,**kwargs):
    if(created):
        #Cuando se Crea algo en la base de datos
        print("Dentro")
    else:
        #Cuando algo ya esta creado en la base de datos
        print("Fuera")
