# Flask Dashboard Deployment on AWS

A production-ready deployment of a Python Flask dashboard on AWS EC2 using Nginx, Gunicorn, and Ansible for automated configuration.

## 🚀 Project Overview

This project demonstrates how to deploy a Flask-based dashboard application to AWS EC2 with a production-ready setup including:

- **Flask** web application with dashboard interface
- **AWS EC2** cloud hosting
- **Nginx** as reverse proxy server
- **Gunicorn** as WSGI HTTP server
- **Ansible** for automated server configuration
- **Production deployment** best practices

## 📋 Prerequisites

Before starting, ensure you have:

- AWS account with EC2 access
- Ansible installed on local machine (`pip install ansible`)
- Basic command line familiarity
- SSH client available
- Git (optional, for version control)

## 🏗️ Architecture

```
Internet → AWS EC2 → Nginx (Port 80) → Gunicorn → Flask App
```

- **Nginx**: Handles static files, SSL termination, and proxies requests
- **Gunicorn**: WSGI server that runs the Flask application
- **Flask**: Web application framework serving the dashboard
- **Systemd**: Manages Gunicorn as a system service

## 📁 Project Structure

```
flask-deployment/
├── app.py                    # Main Flask application
├── wsgi.py                  # WSGI entry point
├── requirements.txt         # Python dependencies
├── deploy.yml              # Ansible playbook
├── inventory.ini           # Ansible inventory file
├── ansible.cfg             # Ansible configuration
├── templates/
│   ├── dashboard.html      # Dashboard HTML template
│   ├── gunicorn.service.j2 # Systemd service template
│   └── nginx.conf.j2       # Nginx configuration template
└── README.md              # This file
```

## 🛠️ Installation & Deployment

### Step 1: AWS EC2 Setup

1. **Launch EC2 Instance:**
   - Navigate to AWS EC2 Console
   - Launch Ubuntu Server 22.04 LTS (t2.micro for free tier)
   - Create/download key pair (.pem file)
   - Configure Security Group:
     - SSH (22) from your IP
     - HTTP (80) from anywhere (0.0.0.0/0)

2. **Note the public IP address** for later use

### Step 2: Local Environment Setup

1. **Clone/Download project files** to your local machine

2. **Install Ansible:**
   ```bash
   pip install ansible
   ```

3. **Configure SSH key permissions:**
   ```bash
   chmod 400 ~/.ssh/your-key.pem
   ```

4. **Update inventory.ini** with your EC2 details:
   ```ini
   [webservers]
   YOUR_EC2_PUBLIC_IP ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/your-key.pem
   ```

### Step 3: Test Connectivity

1. **Test SSH connection:**
   ```bash
   ssh -i ~/.ssh/your-key.pem ubuntu@YOUR_EC2_PUBLIC_IP
   ```

2. **Test Ansible connectivity:**
   ```bash
   ansible webservers -m ping
   ```

### Step 4: Deploy Application

1. **Run the Ansible playbook:**
   ```bash
   ansible-playbook deploy.yml
   ```

2. **Monitor deployment progress** - Ansible will:
   - Update system packages
   - Install Python, pip, nginx
   - Create application directory
   - Install Python dependencies
   - Configure Gunicorn service
   - Configure Nginx
   - Start and enable services

## 🔍 Verification

### Check Services Status

```bash
# Check Gunicorn service
ansible webservers -m shell -a "sudo systemctl status flask_dashboard"

# Check Nginx service
ansible webservers -m shell -a "sudo systemctl status nginx"

# Check application logs
ansible webservers -m shell -a "sudo journalctl -u flask_dashboard -n 20"
```

### Access Application

1. **Main Dashboard:** `http://YOUR_EC2_PUBLIC_IP`
2. **API Endpoint:** `http://YOUR_EC2_PUBLIC_IP/api/data`
3. **Health Check:** `http://YOUR_EC2_PUBLIC_IP/health`

## 🐛 Troubleshooting

### Common Issues

1. **Connection refused:**
   - Check security group allows port 80
   - Verify services are running: `sudo systemctl status nginx flask_dashboard`

2. **502 Bad Gateway:**
   - Check Gunicorn service: `sudo systemctl restart flask_dashboard`
   - Review logs: `sudo journalctl -u flask_dashboard`

3. **Ansible connection issues:**
   - Verify SSH key path and permissions
   - Check EC2 instance is running
   - Confirm security group allows SSH (port 22)

### Useful Commands

```bash
# Restart services
sudo systemctl restart flask_dashboard nginx

# View logs
sudo journalctl -u flask_dashboard -f
sudo tail -f /var/log/nginx/error.log

# Check port usage
sudo netstat -tlnp | grep :80
sudo netstat -tlnp | grep :8000
```

## 🔧 Configuration Details

### Gunicorn Configuration
- Runs on `127.0.0.1:8000`
- Uses 3 worker processes
- Managed by systemd service
- Auto-restarts on failure

### Nginx Configuration
- Listens on port 80
- Proxies requests to Gunicorn
- Serves static files directly
- Includes security headers

### Flask Application Features
- Dashboard with metrics display
- REST API endpoint
- Health check endpoint
- Responsive HTML interface

## 📊 Monitoring

The dashboard displays sample metrics:
- User count: 1,250
- Sales: $45,780
- Orders: 892
- Revenue: $12,345

API endpoint returns JSON data for external integrations.

## 🔒 Security Considerations

- Nginx configured with security headers
- Application runs as non-root user
- SSH key-based authentication
- Security group restricts access appropriately

## 🚀 Production Enhancements

For production use, consider:

- **SSL/TLS**: Add HTTPS with Let's Encrypt certificates
- **Database**: Replace sample data with real database
- **Monitoring**: Add application monitoring (e.g., Prometheus/Grafana)
- **Logging**: Centralized logging solution
- **Backup**: Automated backup strategy
- **Scaling**: Load balancer for multiple instances
- **CI/CD**: Automated deployment pipeline

## 📝 Learning Outcomes

This project demonstrates:

1. **Cloud Infrastructure**: AWS EC2 instance management
2. **Web Server Configuration**: Nginx reverse proxy setup
3. **WSGI Deployment**: Gunicorn for Flask applications
4. **Configuration Management**: Ansible for automated deployment
5. **Production Best Practices**: Service management, logging, security
6. **DevOps Skills**: Infrastructure as code, automation

## �� Contributing

To modify or extend this project:

1. Update Flask application in `app.py`
2. Modify Ansible playbook in `deploy.yml`
3. Adjust configuration templates as needed
4. Test changes before deploying to production

## 📄 License

This project is for educational purposes. Use at your own risk in production environments.

## 🆘 Support

For issues or questions:

1. Check the troubleshooting section
2. Review AWS EC2 and security group settings
3. Verify Ansible inventory configuration
4. Check service logs for detailed error messages

---

**Deployment Date:** $(date)  
**EC2 Instance:** Ubuntu 22.04 LTS  
**Python Version:** 3.10+  
**Flask Version:** 2.3.3
