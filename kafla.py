from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic',
                         group_id='my_group',
                         bootstrap_servers=['localhost:9092'])

for message in consumer:
    print(f"{message.topic}:{message.partition}:{message.offset}: {message.value}")
