import json
import boto3

# This method Stop Running EC2 Intances
def stop_instance(client,id):
    response = client.stop_instances(
        InstanceIds=id
    )
    print('Response of stop_instance')
    print(response)


def lambda_handler(event, context):
  
    # Find All Running Instances
    
    ec2 = boto3.resource('ec2')
    ec2client = boto3.client('ec2')
    
    ec2List = []
    
    custom_filter = [{
    'Name':'tag:ScheduleStop',  # SechduleStop is sample tag, you can change as per your requirement.
    'Values': ['Y']},{          # Y is sample value, you can change as per your requirement.
    'Name':'instance-state-name',
    'Values':['running']
    }]

    # Find Status of Instances 
    
    descInstance = ec2client.describe_instances(Filters=custom_filter)
    
    runningInstanceList = []
    
    for items in descInstance['Reservations']:
        for item in items['Instances']:
            if (item['State']['Code'] == 16):     # This condition is no mandetory to add.
                runningInstanceList.append(item['InstanceId'])
    
    print('Running Instances: ')
    print(runningInstanceList)
    stop_instance(ec2client,runningInstanceList)
    
