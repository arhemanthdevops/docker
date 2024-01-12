import boto3

# Create an EC2 resource and a client
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

# Prompt the user for the necessary inputs
region = input("Enter the region name: ")
az = input("Enter the availability zone: ")
ami_id = input("Enter the AMI ID: ")
instance_type = input("Enter the instance type: ")
key_name = input("Enter the key pair name: ")
sg_name = input("Enter the security group name: ")

# Create and run an EC2 instance
instance = ec2.create_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1,
    SecurityGroups=[sg_name],
    Placement={
        'AvailabilityZone': az
    }
)[0]

# Wait until the instance is running
instance.wait_until_running()

# Get the instance ID
instance_id = instance.id

# Print the instance ID
print(f"Created and launched EC2 instance with ID: {instance_id}")

# Prompt the user for EBS volume details
volume_size = input("Enter the volume size in GB: ")
volume_type = input("Enter the volume type: ")
volume_tag = input("Enter the volume tag: ")

# Create an EBS volume
volume = ec2.create_volume(
    AvailabilityZone=az,
    Size=int(volume_size),
    VolumeType=volume_type,
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': volume_tag
                }
            ]
        }
    ]
)

# Wait until the volume is available
waiter = client.get_waiter('volume_available')
waiter.wait(VolumeIds=[volume.id])

# Get the volume ID
volume_id = volume.id

# Print the volume ID
print(f"Created EBS volume with ID: {volume_id}")

# Prompt the user for the device name
device_name = input("Enter the device name (e.g., /dev/sdh): ")

# Attach the EBS volume to the EC2 instance
attachment = client.attach_volume(
    Device=device_name,
    InstanceId=instance_id,
    VolumeId=volume_id
)

# Print the attachment state
print(f"Attached EBS volume to EC2 instance with state: {attachment['State']}")

