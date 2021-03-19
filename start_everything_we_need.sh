echo "[]" > home_assistant/db/db.json
docker start rabbit &&
node home_assistant/index.js &
sleep 2 &&
(python3 actuators/equipament_server.py actuator Ventinho 8080 &
python3 actuators/equipament_server.py actuator Friozinho 8081 &
python3 actuators/equipament_server.py actuator Brisinha 8082) &
(python3 sensors/rabbitMQ/init_sensor.py smoke Fumacinha 2020 &
python3 sensors/rabbitMQ/init_sensor.py light Farol 2020 &
python3 sensors/rabbitMQ/init_sensor.py temperature "Tá ficando quente" 2020)