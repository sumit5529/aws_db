from celery import shared_task
# import logging

# logger = logging.getLogger(__name__)

@shared_task
def process_food_task(food_id):
    print(f"Started processing Food ID {food_id}")
    from .models import Food
    try:
        food = Food.objects.get(id=food_id)
        print(f"Processing food: {food.name}, price: {food.price}")
        # Add any custom business logic here
    except Food.DoesNotExist:
        print(f"Food ID {food_id} does not exist")

@shared_task
def process_food_task_wrapper():
    # Example: Process the most recent food
    from .models import Food
    latest_food = Food.objects.first()
    if latest_food:
        # process_food_task.delay(latest_food.id)
        print(f"Scheduled task for latest food ID: {latest_food.id}")
    else:
        print("No food records to process")