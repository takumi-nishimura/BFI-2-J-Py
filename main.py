from datetime import datetime

import pandas as pd
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    RadioField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, NumberRange

questions = [
    line.strip()
    for line in open("static/BFI-2-J.csv", "r", newline="\n").readlines()
]

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"

bootstrap = Bootstrap5(app)


class SurveyForm(FlaskForm):
    expt_id = IntegerField(
        "実験ID",
        validators=[DataRequired(), NumberRange(min=1, max=50)],
    )

    name = StringField("氏名", validators=[DataRequired()])
    gender = RadioField(
        "性別",
        choices=[("male", "男性"), ("female", "女性"), ("other", "その他")],
        validators=[DataRequired()],
    )
    age = SelectField(
        "年齢",
        choices=[(str(i), str(i)) for i in range(15, 40)],
        validators=[DataRequired()],
    )

    for i, q in enumerate(questions):
        exec_command = f"q{i+1} = RadioField('Q{i+1}. {q}', choices=[(1, '1:全くあてはまらない'), (2, '2:あてはまらない'), (3, '3:どちらともいえない'), (4, '4:あてはまる'), (5, '5:とてもよくあてはまる')], validators=[DataRequired()])"
        exec(exec_command)

    submit = SubmitField("送信")


@app.route("/", methods=["GET", "POST"])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        form_data = {
            field.name: field.data
            for field in form
            if field.name not in ["submit", "csrf_token"]
        }
        form_data["datetime"] = datetime.now().strftime("%Y%m%d-%H%M%S")
        form_df = pd.DataFrame([form_data])

        result_df = pd.read_csv("data/result.csv", nrows=0)
        add_df = pd.concat([result_df, form_df])
        add_df.to_csv(
            "data/result.csv",
            mode="a",
            header=False,
            index=False,
        )
        print(add_df)

        return redirect(url_for("thank_you", name=form.name.data))

    return render_template("index.html", form=form)


@app.route("/thank_you")
def thank_you():
    name = request.args.get("name", "")
    return render_template("thank_you.html", name=name)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
