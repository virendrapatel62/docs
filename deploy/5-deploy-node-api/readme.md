# 🚀 Deploy Your Node API & Set Up a Reverse Proxy with Nginx

## 🛠️ Step 1: Create a Simple Node App

🔧 Install Node.js and npm on Ubuntu:

```bash
sudo apt install nodejs
sudo apt install npm
```

Clone the git repo in `/var/www`
login using ssh or personal token if repo is private

```bash
git clone https://github.com/virendrapatel62/dev-ops.git
```

📦 Go To The Project Folder & Install Essential Dependencies:

```bash
npm install i
```

⚙️ Install pm2 to Keep Your App Running:

```bash
npm install -g pm2
```

🚴‍♂️ Run the App with pm2:

```bash
pm2 start "npm run start" --name APP_NAME
```

APP_NAME can be used to restart app or stop the app

```bash
pm2 stop APP_NAME
pm2 restart APP_NAME
```

the cloned project here is already setup. start command will run the project with pm2

Your app is now live on port 3000! 🎉

## 🌐 Step 2: Set Up a Reverse Proxy with Nginx

🔄 Edit Nginx Configuration:

```bash
sudo vim /etc/nginx/sites-available/default
```

🔧 Configure the Server Block:

```nginx
server {
 listen 80;
 server_name localhost;

 location / {
     proxy_pass http://127.0.0.1:3000;
     proxy_set_header Host $host;
     proxy_set_header X-Real-IP $remote_addr;
     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     proxy_set_header X-Forwarded-Proto $scheme;
 }
}
```

✅ Test and Reload Nginx:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Now, when you visit http://<server_ip>, you'll see:

```json
{
  "message": "Api is working.."
}
```

when you visit http://<server_ip>/api/ping, you'll see:

```json
"pong"
```

🎉 Congrats! You've successfully deployed a Node API and set up a reverse proxy with Nginx! 🎊
