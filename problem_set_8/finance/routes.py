import os
import requests

from flask import flash, jsonify, redirect, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from helpers import apology, login_required, lookup, usd
from application import app, db, session
from models import Users, Transaction


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = Users.query.filter_by(id=session["user_id"]).first()
    api_key = os.environ.get("API_KEY")
    url = "https://cloud-sse.iexapis.com/stable/stock/{}/quote?token={}"
    transactions = user.transactions

    stocks = list()
    grand_total = float(0)

    for stock in transactions:
        if stock.sold == False:
            symbol = stock.symbol
            name = stock.name
            count = stock.count
            price = requests.get(url.format(symbol, api_key)).json()["latestPrice"]
            total = '{:.2f}'.format(price * count)

            stocks.append([symbol.upper(), name, count, price, total])
            grand_total += float(total)

    return render_template('index.html', stocks=stocks, cash=user.cash, total=round(grand_total+user.cash, 2))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").lower()
        shares = int(request.form.get("shares"))
        
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud-sse.iexapis.com/stable/stock/{symbol}/quote?token={api_key}"

        r = requests.get(url)
        res = r.json()
        
        if r.status_code != 200:
            return apology("An error occured")

        cost = res["latestPrice"] * shares
        user = Users.query.filter_by(id=session["user_id"]).first()

        if cost <= user.cash:
            transaction = Transaction(
                    user_id = user.id,
                    symbol = symbol.upper(),
                    name = res["companyName"],
                    price = res["latestPrice"],
                    count = shares
            )

            user.cash = user.cash - (res["latestPrice"] * shares)

            db.session.add(transaction)
            db.session.commit()
            db.session.close()
            return redirect('/')
        else:
            return apology("Unable to complete transaction")
    
    else: # Method == GET
        return render_template('buy.html')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        # rows = db.execute("SELECT * FROM users WHERE username = :username",
        #                   username=request.form.get("username"))

        # Ensure username exists and password is correct
        user = Users.query.filter_by(username=request.form.get("username")).first()

        if check_password_hash(user.password_hash, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user.id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol").lower()
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud-sse.iexapis.com/stable/stock/{symbol}/quote?token={api_key}"

        try:
            res = requests.get(url).json()
            return render_template('quoted.html', data=res)
        except:
            return apology("Please enter a valid Symbol")

    else:
        return render_template('quote.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403) 

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        
        # Ensure password and confirmation password match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 403)

        user_query = Users.query.filter_by(username=request.form.get("username")).first()
        if user_query:
            return apology("username already exists", 403)

        # Hash password
        password_hash = generate_password_hash(request.form.get("password"))

        # Add to user to database
        user = Users(username=request.form.get("username"), password_hash=request.form.get("password")) 
        db.session.add(user)
        db.session.commit()

        # Redirect user to login page
        return redirect("/login")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
