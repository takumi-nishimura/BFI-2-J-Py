import pandas as pd

domain_df = pd.DataFrame(columns=["domain", "ドメイン", "q_no_list"])
domain_df["domain"] = [
    "Extraversion",
    "Agreeableness",
    "Conscientiousness",
    "Negative Emotionality",
    "Open-Mindedness",
]
domain_df["ドメイン"] = [
    "外向性",
    "協調性",
    "勤勉性",
    "否定的情動性",
    "開放性",
]
domain_df.at[
    domain_df.index[domain_df["domain"] == "Extraversion"][0], "q_no_list"
] = [
    "1",
    "6",
    "11R",
    "16R",
    "21",
    "26R",
    "31R",
    "36R",
    "41",
    "46",
    "51R",
    "56",
]
domain_df.at[
    domain_df.index[domain_df["domain"] == "Agreeableness"][0], "q_no_list"
] = [
    "2",
    "7",
    "12R",
    "17R",
    "22R",
    "27",
    "32",
    "37R",
    "42R",
    "47R",
    "52",
    "57",
]
domain_df.at[
    domain_df.index[domain_df["domain"] == "Conscientiousness"][0], "q_no_list"
] = [
    "3R",
    "8R",
    "13",
    "18",
    "23R",
    "28R",
    "33",
    "38",
    "43",
    "48R",
    "53",
    "58R",
]
domain_df.at[
    domain_df.index[domain_df["domain"] == "Negative Emotionality"][0],
    "q_no_list",
] = [
    "4R",
    "9R",
    "14",
    "19",
    "24R",
    "29R",
    "34",
    "39",
    "44R",
    "49R",
    "54",
    "59",
]
domain_df.at[
    domain_df.index[domain_df["domain"] == "Open-Mindedness"][0], "q_no_list"
] = [
    "5R",
    "10",
    "15",
    "20",
    "25R",
    "30R",
    "35",
    "40",
    "45R",
    "50R",
    "55R",
    "60",
]

facet_df = pd.DataFrame(columns=["facet", "ファセット", "q_no_list"])
facet_df["facet"] = [
    "Sociability",
    "Assertiveness",
    "Energy Level",
    "Compassion",
    "Respectfulness",
    "Trust",
    "Organization",
    "Productiveness",
    "Responsibility",
    "Anxiety",
    "Depression",
    "Emotional Volatility",
    "Intellectual Curiosity",
    "Aesthetic Sensitivity",
    "Creative Imagination",
]

facet_df["ファセット"] = [
    "社交性",
    "自己主張性",
    "活力",
    "思いやり",
    "敬意",
    "信用",
    "秩序",
    "生産性",
    "責任感",
    "不安",
    "抑うつ",
    "情緒不安定性",
    "知的好奇心",
    "美的感性",
    "創造的想像力",
]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Sociability"][0], "q_no_list"
] = ["1", "16R", "31R", "46"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Assertiveness"][0], "q_no_list"
] = ["6", "21", "36R", "51R"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Energy Level"][0], "q_no_list"
] = ["11R", "26R", "41", "56"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Compassion"][0], "q_no_list"
] = ["2", "17R", "32", "47R"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Respectfulness"][0], "q_no_list"
] = ["7", "22R", "37R", "52"]

facet_df.at[facet_df.index[facet_df["facet"] == "Trust"][0], "q_no_list"] = [
    "12R",
    "27",
    "42R",
    "57",
]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Organization"][0], "q_no_list"
] = ["3R", "18", "33", "48R"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Productiveness"][0], "q_no_list"
] = ["8R", "23R", "38", "53"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Responsibility"][0], "q_no_list"
] = ["13", "28R", "43", "58R"]

facet_df.at[facet_df.index[facet_df["facet"] == "Anxiety"][0], "q_no_list"] = [
    "4R",
    "19",
    "34",
    "49R",
]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Depression"][0], "q_no_list"
] = ["9R", "24R", "39", "54"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Emotional Volatility"][0], "q_no_list"
] = ["14", "29R", "44R", "59"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Intellectual Curiosity"][0],
    "q_no_list",
] = ["10", "25R", "40", "55R"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Aesthetic Sensitivity"][0],
    "q_no_list",
] = ["5R", "20", "35", "50R"]

facet_df.at[
    facet_df.index[facet_df["facet"] == "Creative Imagination"][0], "q_no_list"
] = ["15", "30R", "45R", "60"]


def calc_domain_score(q_data: pd.Series):
    domain_score_df = pd.DataFrame(columns=["domain_name", "score"])
    for domain_name in domain_df["domain"]:
        score = 0
        for q_no in domain_df.query("domain == @domain_name")[
            "q_no_list"
        ].values[0]:
            _no = q_no[:-1] if "R" in q_no else int(q_no)
            if "R" in q_no:
                score += 6 - q_data[f"q{_no}"]
            else:
                score += q_data[f"q{_no}"]
        score = score / 12
        domain_score_df = pd.concat(
            [
                domain_score_df,
                pd.DataFrame(
                    data=[[domain_name, score]],
                    columns=domain_score_df.columns,
                ),
            ],
            ignore_index=True,
        )
    return domain_score_df


def calc_facet_score(q_data: pd.Series):
    facet_score_df = pd.DataFrame(columns=["facet_name", "score"])
    for facet_name in facet_df["facet"]:
        score = 0
        for q_no in facet_df.query("facet == @facet_name")["q_no_list"].values[
            0
        ]:
            _no = q_no[:-1] if "R" in q_no else int(q_no)
            if "R" in q_no:
                score += 6 - q_data[f"q{_no}"]
            else:
                score += q_data[f"q{_no}"]
        score = score / 4
        facet_score_df = pd.concat(
            [
                facet_score_df,
                pd.DataFrame(
                    data=[[facet_name, score]],
                    columns=facet_score_df.columns,
                ),
            ],
            ignore_index=True,
        )
    return facet_score_df


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from plot_radar import RadarChart

    df = pd.read_csv("data/result.csv")

    for idx, q_data in df.iterrows():
        domain_score_df = calc_domain_score(q_data)
        facet_score_df = calc_facet_score(q_data)

        print(f"Name: {q_data['name']}")
        print(domain_score_df)
        print(facet_score_df)

    ### Visualize by Radar Chart
    radar_chart = RadarChart(
        labels=domain_score_df["domain_name"], y_range=(0, 5)
    )
    radar_chart.plot(
        values=domain_score_df["score"].tolist(),
        linewidth=1,
        linestyle="solid",
        label="score",
    )
    plt.show()
