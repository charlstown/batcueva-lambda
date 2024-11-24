# Libraries
import json
import datetime
from croniter import croniter
from murci import Murci

# Main code
def lambda_handler(event, context) -> dict:
    """
    Main lambda function generated by default.

    :param event: The data from the event that triggered the function
    :param contex: The data about the execution environment of the function
    :param return: json body and status code
    """
    # Load murci bot
    murci = Murci()
    
    # Load the file
    config_file = 'config.json'
    
    with open(config_file) as file:
        dct = json.load(file)
    print(f"Loaded file {config_file}")
    print(dct)
    
    # Sum the total expends for the next month
    monthly_expenses = dict()
    total_expenses = 0
    for k, v in dct.items():
    
        # Extract payment month
        cron = v['frecuencia']
        executed = executed_this_month(cron)
        
        # Add to total expenses if executed next month
        if executed:
            total_expenses += v["importe"]
            monthly_expenses[v["nombre"]] = v["importe"]
    print("Monthly expenses filtered successfully")
    
    if total_expenses > 0:
        # Generate message to send
        message = f"**RECIBOS EXTRAORDINARIOS ESTE MES**‼️ \nEn el próximo mes se estima un gasto extraordinario de **{total_expenses} € 💸**\n---"
        
        for k, v in monthly_expenses.items():
            message_expense = f"- El gasto de {k}: {v} €"
            message = message + "\n" + message_expense
        
        # Send message
        print(f"Message send: {message}")
        murci.send_message(message)

    return {
        'statusCode': 200,
        'body': None
    }


def executed_this_month(cron: str) -> bool:
    """
    Check if the next planned run matches the next month

    :param cron: cron string in unix format (5 digits)
    :return: True if the next run matches the next month
    """
    
    # Generates the first day of the next month as datetime
    now = datetime.datetime.now()
    now_date = datetime.datetime(now.year, now.month + 1, 1, 00, 00)
    
    # Generates the next cron date from the next month datetime
    cron = croniter(cron, now_date)
    next_date = cron.get_next(datetime.datetime)
    
    return (now_date.year == next_date.year) & (now_date.month == next_date.month)


# Local run
if __name__ == "__main__":
    # Run lambda function
    lambda_handler(None, None)