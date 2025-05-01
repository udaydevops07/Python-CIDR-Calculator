from flask import Flask, render_template_string, request
import ipaddress

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>IPv4 CIDR Calculator</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f2f2f2; }
        .container { max-width: 600px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; }
        input[type=text] { width: 100%; padding: 10px; margin: 10px 0; }
        input[type=submit] { padding: 10px 20px; }
        .output { margin-top: 20px; background: #e8f5e9; padding: 15px; border-radius: 5px; }
        .guide { margin-top: 30px; background: #fff3cd; padding: 15px; border-left: 6px solid #ffcc00; border-radius: 5px; }
        code { background: #f0f0f0; padding: 2px 4px; border-radius: 4px; }
    </style>
</head>
<body>
<div class="container">
    <h2>IPv4 CIDR Calculator</h2>
    <form method="post">
        <label>Enter CIDR (e.g., 192.168.1.0/24):</label>
        <input type="text" name="cidr" required value="{{ cidr if cidr else '' }}">
        <input type="submit" value="Calculate">
    </form>
    {% if output %}
    <div class="output">
        <strong>Results for {{ cidr }}</strong><br><br>
        {% for key, value in output.items() %}
            {{ key }}: {{ value }}<br>
        {% endfor %}
    </div>
    {% endif %}

    <div class="guide">
        <h3>📘 CIDR Manual Calculation Steps</h3>
        <ol>
            <li><strong>Understand CIDR Format:</strong> CIDR is written as <code>IP_address/prefix_length</code> (e.g., <code>192.168.1.0/26</code>).</li>
            <li><strong>Convert Prefix to Subnet Mask:</strong> /26 = <code>255.255.255.192</code>. This is calculated by converting 26 bits to binary and grouping by 8.</li>
            <li><strong>Calculate Block Size:</strong> Subtract the last subnet octet from 256. For /26: 256 - 192 = <code>64</code>.</li>
            <li><strong>Determine Network Address:</strong> Start of the block, e.g., <code>192.168.1.0</code>.</li>
            <li><strong>Determine Broadcast Address:</strong> Last address in the block: <code>192.168.1.63</code>.</li>
            <li><strong>Usable Host Range:</strong> Between network and broadcast: <code>192.168.1.1 - 192.168.1.62</code>.</li>
            <li><strong>Number of Usable Hosts:</strong> <code>2^(32 - prefix) - 2</code>. For /26: <code>62</code> hosts.</li>
        </ol>
        <p><strong>Example:</strong><br>
        CIDR: <code>192.168.1.0/28</code><br>
        Subnet Mask: <code>255.255.255.240</code><br>
        Block Size: <code>16</code><br>
        Host Range: <code>192.168.1.1 - 192.168.1.14</code><br>
        Broadcast: <code>192.168.1.15</code><br>
        Usable Hosts: <code>14</code></p>
    </div>
</div>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def cidr_calc():
    output = {}
    cidr = ""
    if request.method == 'POST':
        cidr = request.form['cidr']
        try:
            net = ipaddress.ip_network(cidr, strict=False)
            hosts = list(net.hosts())
            output = {
                "Network Address": net.network_address,
                "Broadcast Address": net.broadcast_address,
                "Subnet Mask": net.netmask,
                "Wildcard Mask": net.hostmask,
                "Total Hosts": net.num_addresses,
                "Usable Hosts": max(net.num_addresses - 2, 0),
                "Host Range": f"{hosts[0]} - {hosts[-1]}" if len(hosts) > 1 else f"{hosts[0]}"
            }
        except ValueError:
            output = {"Error": "Invalid CIDR format. Please try again."}
    return render_template_string(TEMPLATE, output=output, cidr=cidr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
