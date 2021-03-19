echo "[]" > home_assistant/db/db.json
docker start rabbit &&
node home_assistant/index.js &
sleep 2 &&
(python3 actuators/equipament_server.py ar Ventinho 8080 &
python3 actuators/equipament_server.py lampada Luz 8081 &
python3 actuators/equipament_server.py sprinkler Chuveirinho 8082) &
(python3 sensors/rabbitMQ/init_sensor.py smoke Fumacinha 2020 &
python3 sensors/rabbitMQ/init_sensor.py light Farol 2020 &
python3 sensors/rabbitMQ/init_sensor.py temperature Termômetro 2020)