#!/bin/sh
cat <<END
Cache-Control: no-cache
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>Singapore Rasbperry PIs</title>
<link href=http://archpi.dabase.com/style.css rel=stylesheet>
</head>
<body>

<h1>FREE SG based IPv4 port forwarding / concentrator service for their Raspberry PI</h1>

<h2>Why?</h2>

<ul>
<li>Test you PI is online</li>
<li>Find the IP address of your PI</li>
<li>SSH back to your PI without needing to adjust the forwarding UI of your router</li>
</ul>

<p>Running <code>ssh-loop-sh</code> effectively "phones home" and allows you to connect to it, no matter how it's deployed.</p>
<pre>
NAME	PORT	MAC			LOCAL IP	ORIGIN IP	OPORT	HOST		HPORT		Notes
END

./info.sh

cat <<END
</pre>

<h3>Connecting to your PI</h3>
<pre>
port=\$(curl -s http://pi.dabase.com/\$NAME/ | tail -n1 | awk '{print \$3}')
test "\$port" && ssh pi.dabase.com -p \$port # -o "StrictHostKeyChecking no" -o UserKnownHostsFile=/dev/null
</pre>

<h3>Setup</h3>

<p>ssh-keygen without a password.</p>

<p>Send hendry@iki.fi your public key /root/.ssh/id_rsa.pub. Once he's added your key, run <a href=ssh-loop.sh>ssh-loop.sh</a>.</p>

<p>To keep it running add to /etc/rc.local like so:</p>

<pre>
#!/bin/sh -e
/root/ssh-loop.sh &
exit 0
</pre>

<p>or use a more "modern" systemd service file <a href=ssh-loop.service>ssh-loop.service</a>.</p>

<h3>How the server works</h3>

<pre><code>$ cat /home/pi/.ssh/authorized_keys
END
cat /home/pi/.ssh/authorized_keys
cat <<END

$ cat /home/pi/pilog
END
cat /home/pi/pilog
cat <<END
</code></pre>

<p>Tweaks to /etc/ssh/sshd_config to make it work:</p>

<pre><code>
GatewayPorts yes
TCPKeepAlive yes
ClientAliveInterval 10
</code></pre>

<p>For <a href="http://archpi.dabase.com/">more PI tricks and tips</a>.</p>

</body>
</html>
END
