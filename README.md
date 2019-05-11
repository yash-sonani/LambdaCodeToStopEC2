# LambdaCodeToStopEC2
This Lambda Code Stop Running EC2 Instance which have specific Tag. 


## Steps to create Schedule to stop EC2 Instances in AWS

1. Create Lambda as per [lambda_function.py](https://github.com/yash-sonani/LambdaCodeToStopEC2/blob/master/lambda_function.py) code(Python 3.7)

2. Schedule CloudWatch Trigger in Lambda with Schedule expression: [cron(01 15 * * ? *)](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html) . This will trigger lambda function every day on 9:01 PM

3. Add Tag(Mention in cunstom_filter) in EC2 instace so that code identify the same.
