# 🎉 Server Setup Party 🚀

Welcome to the ultimate guide for setting up your server! Let’s make this setup process as smooth and enjoyable as possible. 😎

🗝️ 1. Log In with SSH 🌐

First things first, log in to your server with SSH:

```bash
ssh root@172.105.60.205
```

🍎 2. Keep Your Packages Fresh
Before upgrading, always update your package list to get the latest and greatest:

```bash
apt update
apt upgrade
```

🔑 3. Change the Root Password (Optional)
Want to keep things extra secure? Change the root password:

```bash
passwd
```

👤 4. Create a Non-Root User & Give Sudo Access
Add a new user and grant them sudo privileges:

```bash
adduser <username>
usermod -aG sudo <username>
```

🔒 5. Set a Password for Your New User
Update the password for your new user:

```bash
sudo passwd <username>
```

💻 6. Connect with Your New User
Log in with your new user credentials:

```bash
ssh <username>@192.IP.IP.IP
```

🔑✨ 7. Set Up SSH Key Authentication
Generate a shiny new SSH key pair on your local machine:

```bash
ssh-keygen -t ed25519 -C "user@gmail.com"
```

View your brand-new public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

🌍 8. Add Your Public Key to the Server
On your server, create a .ssh directory (if it doesn’t exist) and add your public key to authorized_keys:

```bash
mkdir -p ~/.ssh
nano ~/.ssh/authorized_keys
```

Paste your public key into the authorized_keys file and save it.

🔐 9. Add Key to SSH Agent
On your local machine, add your SSH key to the agent:

```bash
ssh-add -k ~/.ssh/id_ed25519
```

Now you can log in without needing a password. 🎉

🚫🔐 10. Disable Password Login for Extra Security
Edit the SSH configuration to disable password login:

```bash
sudo nano /etc/ssh/sshd_config
```

Find PasswordAuthentication and set it to no. Optionally, you can also set PermitRootLogin to no to prevent root logins.

Restart SSH to apply your changes:

```bash
sudo service ssh restart
```

🔥 11. Configure the Firewall
Install and set up UFW to manage your firewall:

```bash
sudo apt install ufw
```

Allow traffic on ports 80 (HTTP), 443 (HTTPS), and 22 (SSH):

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
```

Enable UFW:

```bash
sudo ufw enable
```

Check the status to ensure the rules are applied:

```bash
sudo ufw status
```

For detailed instructions on enabling and disabling ports, check out the UFW documentation.
