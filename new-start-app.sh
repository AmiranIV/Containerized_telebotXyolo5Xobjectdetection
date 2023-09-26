echo "Starting ngrok and writing link to .secret file"
bash ngstart.sh  
echo
sleep 3
echo "Docker compose up..."
docker compose up
sleep 5
echo "Overwriting secrets.env..."
echo "TELEGRAM_TOKEN=<USE YOUR TELEGRAM TOKEN HERE> " > secrets.env
echo "TELEGRAM_APP_URL=<replacethis>" >> /home/ubuntu/secrets.env  ##DON't TOUCH THE <replacethis>
