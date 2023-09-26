#!/bin/sh

# Set local port from command line arg or default to 8080
LOCAL_PORT=${1-8443}

echo "Start ngrok in background on port [ $LOCAL_PORT ]"
nohup ngrok http "$LOCAL_PORT" &>/dev/null &

echo -n "Extracting ngrok public url ."
NGROK_PUBLIC_URL=""
while [ -z "$NGROK_PUBLIC_URL" ]; do
  # Run 'curl' against ngrok API and extract public URL (using 'sed' command)
  NGROK_PUBLIC_URL=$(curl --silent --max-time 10 --connect-timeout 5 \
    --show-error http://127.0.0.1:4040/api/tunnels | \
    sed -nE 's/.*public_url":"(https:..[^"]*).*/\1/p')
  sleep 1
  echo -n "."
done

echo
echo "NGROK_PUBLIC_URL => [ $NGROK_PUBLIC_URL ]"

# Read the current contents of secrets.env
SECRETS_FILE="/home/ubuntu/secrets.env"
CURRENT_CONTENTS=$(cat "$SECRETS_FILE")

# Replace <replacethis> with the ngrok URL and write it back to secrets.env
NEW_CONTENTS="${CURRENT_CONTENTS/<replacethis>/$NGROK_PUBLIC_URL}"
echo "$NEW_CONTENTS" > "$SECRETS_FILE"
