from croniter import croniter
import datetime

def calculate_cron_executions(cron_schedule, start_time, end_time):
    # Convert start_time and end_time to datetime objects
    start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    # Initialize the number of cron job executions
    count = 0
    
    # Get the current time
    current_time = start_time
    
    # Use croniter to create the cron job
    cron = croniter(cron_schedule, current_time)
    
    # While the current time is less than the end time
    while current_time <= end_time:
        next_time = cron.get_next()
        next_time = datetime.datetime.fromtimestamp(next_time)
        # If the next scheduled execution time is less than the end time
        if next_time <= end_time:
            # Increment the count
            count += 1
        # Set the current time to the next scheduled execution time
        current_time = next_time
    return count

cron_schedule = "20,40 10 * * *"
start_time = "2022-01-01 00:00:00"
end_time = "2025-01-01 23:59:59"

executions = calculate_cron_executions(cron_schedule, start_time, end_time)
print(executions)
