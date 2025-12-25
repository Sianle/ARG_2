from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ARG-2</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #111;
            color: #fff;
            font-family: Arial, sans-serif;
        }

        .container {
            text-align: center;
        }

        input[type="password"] {
            width: 300px;
            height: 45px;
            font-size: 20px;
            padding: 5px 10px;
            text-align: center;
            margin-bottom: 15px;
        }

        button {
            width: 120px;
            height: 40px;
            font-size: 16px;
            cursor: pointer;
        }

        .shapes {
            display: flex;
            gap: 20px;
            justify-content: center;
            margin-top: 30px;
        }

        .shape {
            width: 80px;
            height: 80px;
            cursor: pointer;
        }

        #resultText {
            margin-top: 25px;
            font-size: 28px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <form method="post">
            <input type="password" name="password" placeholder="PASSWORD">
            <br>
            <button type="submit">확인</button>
        </form>

        {% if success %}
        <div class="shapes">
            <div class="shape" style="background-color:#FFFFFF" onclick="changeColor(this)"></div>
            <div class="shape" style="background-color:#FFFFFF" onclick="changeColor(this)"></div>
            <div class="shape" style="background-color:#FFFFFF" onclick="changeColor(this)"></div>
        </div>
        <div id="resultText"></div>
        {% endif %}

        {% if result %}
            <p>{{ result }}</p>
        {% endif %}
    </div>

<script>
    const colors = [
        "#FF0000", // 빨
        "#FFA500", // 주
        "#FFFF00", // 노
        "#00FF00", // 초
        "#0000FF", // 파
        "#800080", // 보
        "#FFFFFF"  // 흰
    ];

    function changeColor(elem) {
        let rgb = elem.style.backgroundColor;
        let hex = rgbToHex(rgb);
        let index = colors.indexOf(hex);
        let next = colors[(index + 1) % colors.length];
        elem.style.backgroundColor = next;
        checkCondition();
    }

    function rgbToHex(rgb) {
        let nums = rgb.match(/\\d+/g);
        return "#" + nums.map(n =>
            parseInt(n).toString(16).padStart(2, "0")
        ).join("").toUpperCase();
    }

    function checkCondition() {
        const shapes = document.querySelectorAll(".shape");
        const c1 = rgbToHex(shapes[0].style.backgroundColor);
        const c2 = rgbToHex(shapes[1].style.backgroundColor);
        const c3 = rgbToHex(shapes[2].style.backgroundColor);

        if (c1 === "#FFFFFF" && c2 === "#00FF00" && c3 === "#0000FF") {
            document.getElementById("resultText").innerText = "0223";
        }
    }
</script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    success = False

    if request.method == "POST":
        if request.form.get("password") == "110114111":
            success = True
        else:
            result = "Wrong Password"

    return render_template_string(HTML, result=result, success=success)

if __name__ == "__main__":
    app.run()