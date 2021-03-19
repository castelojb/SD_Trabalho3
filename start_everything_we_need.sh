echo "[]" > home_assistant/db/db.json
docker start rabbit &&
node home_assistant/index.js &
sleep 2 &&
(python3 actuators/equipament_server.py ar "Ar-condicionado" 8080 &
python3 actuators/equipament_server.py lampada "Lâmpada" 8081 &
python3 actuators/equipament_server.py sprinkler "Sprinkler" 8082) &
(python3 sensors/rabbitMQ/init_sensor.py smoke "Detector de Fumaça" 2020 &
python3 sensors/rabbitMQ/init_sensor.py light "Sensor de Luminosidade" 2020 &
python3 sensors/rabbitMQ/init_sensor.py temperature "Termômetro" 2020) &
python3 -m http.server -d ./front-end/build 3006