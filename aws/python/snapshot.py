import boto3

# Initialize a Boto3 client for Auto Scaling
autoscaling_client = boto3.client('autoscaling')

# Define your launch configuration
launch_config_name = 'my-launch-config'
image_id = 'ami-123456'  # Replace with your AMI ID
instance_type = 't2.micro'

# Create a launch configuration
autoscaling_client.create_launch_configuration(
    LaunchConfigurationName=launch_config_name,
    ImageId=image_id,
    InstanceType=instance_type,
)

# Define your Auto Scaling group parameters
auto_scaling_group_name = 'my-auto-scaling-group'
min_size = 1
max_size = 3
desired_capacity = 1
vpc_zone_identifier = 'subnet-12345'  # Replace with your subnet ID

# Create Auto Scaling group
autoscaling_client.create_auto_scaling_group(
    AutoScalingGroupName=auto_scaling_group_name,
    LaunchConfigurationName=launch_config_name,
    MinSize=min_size,
    MaxSize=max_size,
    DesiredCapacity=desired_capacity,
    VPCZoneIdentifier=vpc_zone_identifier,
)

# Define scale up policy
scale_up_policy = autoscaling_client.put_scaling_policy(
    AutoScalingGroupName=auto_scaling_group_name,
    PolicyName='ScaleUp',
    ScalingAdjustment=1,
    AdjustmentType='ChangeInCapacity',
    Cooldown=300,
)

# Define scale down policy
scale_down_policy = autoscaling_client.put_scaling_policy(
    AutoScalingGroupName=auto_scaling_group_name,
    PolicyName='ScaleDown',
    ScalingAdjustment=-1,
    AdjustmentType='ChangeInCapacity',
    Cooldown=300,
)

# Initialize CloudWatch client
cloudwatch_client = boto3.client('cloudwatch')

# Create CloudWatch alarm for scale up
cloudwatch_client.put_metric_alarm(
    AlarmName='High CPU Utilization',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Threshold=70.0,
    Period=300,
    EvaluationPeriods=1,
    ComparisonOperator='GreaterThanThreshold',
    Dimensions=[
        {
            'Name': 'AutoScalingGroupName',
            'Value': auto_scaling_group_name
        },
    ],
    AlarmActions=[
        scale_up_policy['PolicyARN']
    ],
)

# Create CloudWatch alarm for scale down
cloudwatch_client.put_metric_alarm(
    AlarmName='Low CPU Utilization',
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Threshold=30.0,  # Adjust this threshold as needed
    Period=300,
    EvaluationPeriods=1,
    ComparisonOperator='LessThanThreshold',
    Dimensions=[
        {
            'Name': 'AutoScalingGroupName',
            'Value': auto_scaling_group_name
        },
    ],
    AlarmActions=[
        scale_down_policy['PolicyARN']
    ],
)

print("Auto Scaling setup with scale-up and scale-down policies is complete.")

