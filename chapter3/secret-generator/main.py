from bottle import run, template, route, request
import secrets

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secret Generator</title>

    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: #f4f4f4;
            font-family: Arial, sans-serif;
        }

        .container {
            background: white;
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0 4px 18px rgba(0,0,0,0.12);
            text-align: center;
        }

        .label {
            font-size: 18px;
            margin-bottom: 10px;
            display: block;
            color: #444;
        }

        .secret-box {
            font-size: 24px;
            font-weight: bold;
            padding: 12px 20px;
            background: #eef0f5;
            border-radius: 8px;
            display: inline-block;
            margin-bottom: 20px;
        }

        button {
            padding: 10px 18px;
            font-size: 16px;
            border: none;
            border-radius: 6px;
            background: #007bff;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #0069d9;
        }
    </style>
</head>

<body>
    <div class="container">
        <span class="label">Your Secret Code</span>

        <div class="secret-box" id="secret-code">
            {{code}}
        </div>

        <br />

        <button onclick="copyCode()">Copy Code</button>
    </div>

    <script>
        function copyCode() {
            const text = document.getElementById('secret-code').innerText;
            navigator.clipboard.writeText(text).then(() => {
                alert('Code copied!');
            });
        }
    </script>
</body>
</html>

'''

@route("/")
def index():
    length = 32
    if query_length:= request.query.length:
        length = int(query_length)
    code = secrets.token_urlsafe(length)
    return template(HTML,code=code)

run(host="localhost", port=8080, reloader=True, debug=True)